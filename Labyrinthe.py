from Cellule import *
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Labyrinthe:
    #Constructeur du labyrinthe
    def __init__(self, nbLig, nbCol):
        
        #Nombre de ligne
        self.ligs = nbLig
        
        #Nombre de colonnes
        self.cols = nbCol
        
        #Construction du labyrinthe avec des cellules (non connectées entre eux)
        self.lab = [[cellule(lig, col) for col in range(nbCol)] for lig in range(nbLig)]
        
        #Mettre à jour les voisines de chaque cellule du labyrinthe
        for lig in range(nbLig):
            for col in range(nbCol):
                if lig>0:
                    self.getCellule(lig, col).setCellulesVoisines("haut", self.getCellule(lig-1, col))
                if lig < nbLig - 1 :
                    self.getCellule(lig, col).setCellulesVoisines("bas", self.getCellule(lig+1, col))
                if col > 0:
                    self.getCellule(lig, col).setCellulesVoisines("gauche", self.getCellule(lig, col-1))
                if col < nbCol - 1:
                    self.getCellule(lig, col).setCellulesVoisines("droite", self.getCellule(lig, col+1))
                    
    #Accesseur en écriture pour récupérer la case à la position (lig,col)  
    def getCellule(self, lig, col):
        return self.lab[lig][col] 
     
    #Méthode pour générer le Labyrinthe en utilisant le DFS           
    def genererLabyrinthe(self):
        #Initialisation de la pile et ajouter la première cellule du Labyrinthe
        pile = [self.getCellule(0,0)]
        
        #Marquer la première cellule comme visitée
        self.getCellule(0, 0).visitee = True
        
        #Tant que notre pile contien de cellules à parcourir
        while pile:
            
            #Récupérer le sommet de la pile
            cellule_courante = pile[-1]
            
            #Récupérer les cases voisines non visitées de cellule
            voisines = cellule_courante.getVoisinesNonVisitees()

            #Si on a trouvé des cases voisines non visitées
            if voisines:
                
                #On récupère une case aléatoire (suivante)
                #Et de quelle côté est positionnée par rapport à la cellule courante (cote)
                cote, suivante = random.choice(voisines)
                
                #Marquer la cellule choisie comme visitee
                suivante.visitee = True
                
                #Supprimer le mur entre les deux cellules (cellule_courante et suivante)
                cellule_courante.supprimer_Mur(suivante, cote)
                
                #Empiler la case visitée dans la pile 
                pile.append(suivante)
            
            #Si on n'a pas de cases voisines non visitées
            else:
                #On dépile pour faire la backtracking
                pile.pop() 
            
            #Marquer la cellule de la fin comme sortie pour une utilisation ultérieur (Optionel)
            self.getCellule(self.ligs - 1, self.cols - 1).sortie = True
            
            #Des prints pour les déboggage
            '''
            print(f"Current Cell: ({cellule_courante.lig}, {cellule_courante.col})")
            print(cellule_courante.murs) 
            print(f"Suivante: {suivante.lig}, {suivante.col }")  
            '''
 
    #Parcour main droite
    def parcourir_main_droite(self):   
        
        #Initialisation de la direction vers la "droite"  
        direction = "droite"
        
        #Initialiser la pile avec la première cellule du labyrinthe
        pile = [self.getCellule(0,0)]
        
        #Tant qu'il reste des cellules à parcourir 
        while pile:  
            #Récuérer le sommet de la liste (dernière cellule empiler) sans la dépiler        
            cellule_courante = pile[-1] 
            
            #On la marque comme parcourue
            cellule_courante.parcourue = True 
            
            #On teste si la sortie et atteinte
            if cellule_courante.estSortie():
                
                #indiquer que la sortie est trouvée
                print("Sortie trouvée!!")
                
                #Sortir de la méthode
                return
            
            #Si le mur entre la case courante dans la direction indiquée est False (supprimé)
            if not cellule_courante.murs[direction]:
                
                # Si la cellule courante n'a aucune voisine non parcourue       
                if cellule_courante.getVoisinesNonParcourues() == []:
                    
                    # Dépiler pour retourner en arrière
                    pile.pop()
                    
                    # Remettre la direction vers la droite
                    direction = "droite"
                    
                    # Print pour le débogage
                    print(f" BACKTRACKING")
                else:
                    #Récupérer la cellule voisine dans cette direction
                    suivante = cellule_courante.getVoisineDir(direction)
                
                    #Si On peut avancer vers la cellule suivante 
                    if suivante is not None and not suivante.parcourue:
                         #Avancer vers la cellule voisine
                        cellule_courante = suivante
                    
                        #Empiler la nouvelle cellule courante
                        pile.append(cellule_courante)

                        #Print pour le déboggage
                        print(f"Position actuelle = {cellule_courante.lig}, {cellule_courante.col}")  
            
                    # Si la case suivante est parcourue ou bien n'existe pas   
                    else :
                        print(f"Cellule parcourue - direction {direction}")
                        
                        # Changer la direction   
                        direction = self.tourner_a_droite(direction)
                        
                        print(f"Tourner à droite - direction {direction}") 
                                            
            # Si le mur est fermé dans cette direction
            # Et même si on a des cellules voisines non parcourues on change d'abord la direction
            else:
                direction = self.tourner_a_droite(direction)
                print(f"Tourner à droite - direction {direction}")
                print(f"Position actuelle = {cellule_courante.lig}, {cellule_courante.col}")  

                           
    
    # Méthode pour changer la direction        
    def tourner_a_droite(self, direction):
        # J'ai fait en sorte qu'on tourner toujours à droite
        directions = ["haut", "droite", "bas", "gauche"]
        
        # Récupérer l'indice de la cellule courante
        index = directions.index(direction)
        
        # Expression arithmétique pour avancer dans le tableau sans dépasser la taille
        new_index = (index + 1) % 4
        
        # Récupérer la nouvelle direction
        return directions[new_index] 
      
    def matrice_distances(self):  
        # Initialisation de la matrice des distances
        mat = [[float('inf') for _ in range(self.cols)] for _ in range(self.ligs)]
        
        # mettre à jour de la distance de la première case 
        mat[0][0] = 0
        
        # initialiser une file pour stocker les tuples des cases
        file = [(0,0)]
        
        # Tant qu'on est pas retourner au départ
        while file:
            
            # récupérer le premier élément ajouté à la file
            x, y = file.pop(0)
            
            #Si le cellule courante est la sortie
            if (x, y) == (self.ligs - 1, self.cols - 1):
                #On retourne la matrice des distances (sans parcourir les cellules restantes)
                return mat
            
            #Récupérer la cellule corréspendante
            cellule = self.getCellule(x, y)
            
            #Parcourir la liste des cases voisines de la cellule
            for x_voisine, y_voisine in cellule.getVoisines():
                
                #Pour chaque cellule Traversée on rajoute 1 à la distance
                nouvelle_distance = mat[x][y] + 1

                #Si la nouvelle distance
                #est plus petite que la valeur courante de la distance
                if nouvelle_distance < mat[x_voisine][y_voisine]:
                    #On la met à jour
                    mat[x_voisine][y_voisine] = nouvelle_distance
                    
                    #On rajoute la cellule voisine à la file
                    file.append((x_voisine, y_voisine))
        
        #retourner la matrice résultante
        return mat
    
    
    def chemin_sortie(self):
        #Récupérer la matrice des distances
        matrice = self.matrice_distances()
        
        # Les coordonnées de la sortie
        x, y = self.ligs - 1, self.cols - 1
        
        #Initialiser la tableau de tuples formants le chemin
        chemin = [(x, y)]
        
        #Récupérer la distance entre la sortie et le départ
        dist_totale = matrice[x][y] 
        
        #Tant qu'on est pas retourner vers la cellule de depart
        while dist_totale > 0:
            
            #résupérer les cellules voisines de la case courante
            voisines = self.getCellule(x, y).getVoisines()
            
            #Parcourir toutes les cellules voisines
            for xv, yv in voisines:
                
                #Si la distance de case voisine est plus petite que la distance courante
                if matrice[xv][yv] == dist_totale - 1:
                    
                    #Ajouter cette case au chemin (insertion au début)
                    chemin.insert(0, (xv, yv))
                    
                    #Mettre à jour la cellule courante
                    x, y = xv, yv
                    
                    #Diminuer la distance totale
                    dist_totale -= 1
                              
        # retourner le tableau de tuples (chemin)
        return chemin
                         
    def AfficheLabyrinthe(self):
        # Création de la figure et l'axe pour le tracer 
        fig, ax = plt.subplots()
        
        # Récupérer le chemin de sortie (optimisé) pour l'afficher avec une couleur differente
        chemin = self.chemin_sortie()
        
        #Parcourir les cellules du labyrinthe
        for lig in range(self.ligs):
            for col in range(self.cols):
                
                #Récupérer la cellule actuelle
                cellule = self.getCellule(lig, col)
                
                #Coorndonnées de la cellule sur le graphique
                x, y = col, self.ligs - 1 - lig
                
                # placer les graduations de l'axe des x en haut
                ax.xaxis.tick_top()
                
                #Couleur de la cellule
                cell_color = ''
                
                
                # Si la cellule fait partie du chemin optimisé vers la sortie
                if (lig, col) in chemin:
                    # La colorer en orange
                    cell_color = 'lightcoral'
                
                #Si la cellule a été parcourue par l'algorithme de la main droite
                elif cellule.parcourue :
                    # la colorer en vert 
                    cell_color = 'gold'
                
                #Si non
                else: 
                    # la couleur est blanche
                    cell_color = 'white'
                    
                # Afficher les murs en fonction de la présence ou absence des murs
                if cellule.murs["haut"]:
                    ax.plot([x, x + 1], [y + 1, y + 1], color='black')
                if cellule.murs["bas"]:
                    ax.plot([x, x + 1], [y, y], color='black')
                if cellule.murs["gauche"]:
                    ax.plot([x, x], [y, y + 1], color='black')
                if cellule.murs["droite"]:
                    ax.plot([x + 1, x + 1], [y, y + 1], color='black')     
                    
                # Ajouter un rectangle pour affiche la cellule avec sa couleur           
                ax.add_patch(patches.Rectangle((x, y), 1, 1, fill=True, edgecolor='none', facecolor=cell_color))
                
        # Ajuster l'aspect du graphique       
        plt.gca().set_aspect('equal', adjustable='box')
        
        #Désactiver l'affichage des axes
        plt.axis('off')
        
        #Ajouter un titre à la figure
        fig.suptitle("~~~~ Labyrinthe ~~~~")
        
        # Afficher le graphique
        plt.show()


# ===== J E U X     D ' E S S A I ========
'''
 L'affichage est un labyrinthe avec les chemins vers la sortie
 
    - Le chemin obtenu avec le parcour à la main droite est l'union du chemin coloré
    en jaune et en rose
    - le chemin optimal est le chemin rose
    
 Donc la partie jaune est le chemin où y'avait le backtracking lors de la méthode de la main droite
 
    - Les figures ne s'affiches pas toutes au même temps, 
    donc il faut fermer la figure courante pour que la suivante puisse s'afficher 
'''

laby = []
# Labyrinthe Carré
# ///////// Parcour main droite //////////
lab1 = Labyrinthe(10, 10)
lab1.genererLabyrinthe()
lab1.parcourir_main_droite()

# /////// Chemin optimisé ////////
lab1.genererLabyrinthe()
chemin1 = lab1.chemin_sortie()
print(chemin1)
laby.append(lab1)


# Labyrinthe rectangulaire
# ///////// Parcour main droite //////////
lab3 = Labyrinthe(10,15)
lab3.genererLabyrinthe()
lab3.parcourir_main_droite()

# /////// Chemin optimisé ////////

#lab4 = Labyrinthe(5, 8)
lab3.genererLabyrinthe()
chemin3 = lab3.chemin_sortie()
print(chemin3)
laby.append(lab3)

for l in laby:
    l.AfficheLabyrinthe()