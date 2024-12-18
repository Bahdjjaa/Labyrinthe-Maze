# Classe pour modéliser la cellule d'unn labyrinthe
class cellule:
    def __init__(self, x, y):
        # Ligne de la cellule 
        self.lig = x    
        # colonne de la cellule
        self.col = y   
        # Dictionnaire centenant des booléens indiquant la présence ou abscence des murs en fonction du côté
        self.murs = {"haut": True, "bas": True, "gauche" : True, "droite": True}  
        
        # Initialiser un dictionnaire contenant les voisines de chaque cellule en fonction du côté
        self.CellulesVoisines = {"haut": None, "bas": None, "gauche" : None, "droite": None}

        # booléen pour indqiuer si la cellule visitée (utilisé pour la génération du Labyrinthe)
        self.visitee = False
        
        # booléen pour indiquer si la case est une sortie du Labyrinthe
        self.sortie = False
        
        # booléen pour indiquer si la case est parcourue lors du parcour à la main droite
        self.parcourue = False


    # Accesseur en écriture pour mettre en place les cellule voisines de chaque cellule
    def setCellulesVoisines(self, cote, cellule_voisine):
        self.CellulesVoisines[cote] = cellule_voisine
    
    # Méthode pour retourner la valeur du booléen indiquant si la cellule est une sortie du labyrinthe
    def estSortie(self):
        return self.sortie
    
    # Méthode pour récupérer les coordonées des cellules voisines
    def getVoisines(self):
        tab = [] # Initialisation du tableau
        for d in ["haut", "bas", "gauche", "droite"]: #Tester pour chaque côté
            # Si la cellule existe bien et il n'y a pas un mur entre les deux cellules
            if self.getVoisineDir(d) is not None:
                # Récupérer les coordonnées de la voisine et les ajouter au tableau
                tab.append((self.getVoisineDir(d).lig, self.getVoisineDir(d).col))
        # retourner le tableau des cellules voisines 
        return tab
        

    # Méthode pour récupérer les cellules voisines non visitées 
    def getVoisinesNonVisitees(self): # (ancien nom de la méthode = getCellulesAdjacentes(self))
        tabVoisines = [] # Initialisation du tableau
        
        # Parcourir le disctionnaire des cellules voisines
        for cote, voisine in self.CellulesVoisines.items() :
            # Si la case voisine existe et elle n'est pas visitées
            if (voisine != None) and (not voisine.visitee) :
                # Ajouter un tuple contenant le côté ou la case voisine se situe et son l'adresse
                tabVoisines.append((cote, voisine))
                
        # Retourner le tableau des cases voisines
        return tabVoisines


    # Méthode pour récupérer la cellule dans une direction donnée
    # Utilisée pour faire le parcour de la main droite
    def getVoisineDir(self, direction):  
        # Récupérer la case voisine dans cette direction
        cellule = self.CellulesVoisines[direction]
        
        # Si la case voisine existe bien
        if cellule != None and not self.murs[direction]:     
            # Retourner l'adresse de catte cellule
            return cellule
    
    # Méthode pour récupérer les cellules non parcourues
    # Utilisée pour faire le parcour de la main droite
    def getVoisinesNonParcourues(self):
        # Initialisation du tabelau
        tabVoisines = []
        
        # Parcourir toutes les cellules voisines
        for cote, voisine in self.CellulesVoisines.items():
            
            # Si la cellule voisine existe bien et elle n'est pas parcourue
            if (voisine!= None) and (not voisine.parcourue) and (not self.murs[cote]):
                
                # Ajouter son adresse au tableau tabVoisines
                tabVoisines.append(voisine)
        
        # Retourner le tableau des cases voisines non parcourues
        return tabVoisines
    
        

    # Méthode pour supprimer les murs en fonction du côté
    def supprimer_Mur(self, suivante, cote):
        
        # Chaque fois qu'on supprime un mur d'une case dans une direction
        # On le supprime aussi de la case suivante dans le sens oposé
        
        if cote == "haut":
            self.murs["haut"] = False
            suivante.murs["bas"] = False
            
        if cote == "bas":
            self.murs["bas"] = False
            suivante.murs["haut"] = False
              
        if cote == "gauche":
            self.murs["gauche"] = False
            suivante.murs["droite"] = False
            
        if cote == "droite":
            self.murs["droite"] = False
            suivante.murs["gauche"] = False          
        
    