## Auteur / Author : Bahdja Moucer


***Français***

*English below*
# Générateur et Résolveur de Labyrinthe 🏰

Ce projet implémente un labyrinthe informatique avec génération, affichage et résolution, basé sur des algorithmes avancés tels que DFS et Dijkstra.

## Table des Matières
- [Présentation](#présentation)
- [Caractéristiques](#caractéristiques)
- [Technologies Utilisées](#technologies-utilisées)
- [Structure du Projet](#structure-du-projet)
- [Algorithmes](#algorithmes)
- [Installation](#installation)

---

## Présentation
Le projet vise à :
- **Modéliser** un labyrinthe comme une grille de cellules.
- **Générer** un labyrinthe parfait (une seule solution possible).
- **Résoudre** le labyrinthe en utilisant deux approches :
  - Méthode de la main droite.
  - Algorithme de Dijkstra pour le chemin optimal.

---

## Caractéristiques
- **Modélisation avancée** : Chaque cellule possède des attributs spécifiques, notamment ses murs, voisines, et son état (visité, parcouru, sortie, etc.).
- **Affichage graphique** : Utilisation de `matplotlib` pour visualiser le labyrinthe et ses chemins.
- **Génération de labyrinthes parfaits** : Créés avec l'algorithme DFS.
- **Résolution efficace** : Résolution avec la méthode de la main droite ou Dijkstra.

---

## Technologies Utilisées
- Python 3
- Bibliothèques : `matplotlib`, `numpy`

---

## Structure du Projet
### Classe `Cellule`
- Attributs :
  - `lig`, `col` : Coordonnées de la cellule.
  - `murs` : Présence ou absence des murs (haut, bas, gauche, droite).
  - `CellulesVoisines` : Références vers les cellules voisines.
  - `visitee`, `parcourue` : Booléens indiquant l'état de la cellule.
  - `sortie` : Booléen indiquant si la cellule est la sortie.

### Classe `Labyrinthe`
- Attributs :
  - `ligs`, `cols` : Dimensions du labyrinthe.
  - `lab` : Grille contenant toutes les instances de cellules.
- Méthodes principales :
  - `genererLabyrinthe` : Génération du labyrinthe parfait (DFS).
  - `parcourir_main_droite` : Résolution avec la méthode de la main droite.
  - `matrice_distances` et `chemin_sortie` : Résolution avec Dijkstra.

---

## Algorithmes
### Génération
- **DFS (Depth-First Search)** :
  - Génère un labyrinthe parfait sans boucle.

### Résolution
1. **Méthode de la Main Droite** :
   - Suit les murs du labyrinthe.
   - Peut nécessiter un backtracking.
2. **Dijkstra** :
   - Trouve le chemin optimal basé sur les distances calculées.

---

## Installation
1. Clonez le dépôt :
   ```bash
   git clone git@github.com:<votre-utilisateur>/<votre-repo>.git
   cd <votre-repo>

---
---
***English***
# Maze Generator and Solver 🏰

This project implements a computational maze with generation, display, and solving features, based on advanced algorithms like DFS and Dijkstra.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Algorithms](#algorithms)
- [Installation](#installation)

---

## Overview
The goal of this project is to:
- **Model** a maze as a grid of cells.
- **Generate** a perfect maze (only one solution exists).
- **Solve** the maze using two approaches:
  - The right-hand rule method.
  - Dijkstra's algorithm to find the optimal path.

---

## Features
- **Advanced Modeling**: Each cell includes attributes such as walls, neighbors, and state (visited, traversed, exit, etc.).
- **Graphical Display**: `matplotlib` is used to visualize the maze and paths.
- **Perfect Maze Generation**: Created using the DFS algorithm.
- **Efficient Solving**: Solve mazes using either the right-hand rule or Dijkstra's algorithm.

---

## Technologies Used
- Python 3
- Libraries: `matplotlib`, `numpy`

---

## Project Structure
### `Cell` Class
- Attributes:
  - `row`, `col`: Coordinates of the cell.
  - `walls`: Presence or absence of walls (top, bottom, left, right).
  - `neighboring_cells`: References to adjacent cells.
  - `visited`, `traversed`: Booleans indicating the cell's state.
  - `is_exit`: Boolean indicating if the cell is the maze exit.

### `Maze` Class
- Attributes:
  - `rows`, `cols`: Dimensions of the maze.
  - `grid`: Grid containing all instances of cells.
- Main Methods:
  - `generate_maze`: Generates a perfect maze using DFS.
  - `solve_with_right_hand_rule`: Solves the maze using the right-hand rule.
  - `distance_matrix` and `find_shortest_path`: Solve the maze using Dijkstra's algorithm.

---

## Algorithms
### Maze Generation
- **DFS (Depth-First Search)**:
  - Generates a perfect maze with no loops.

### Maze Solving
1. **Right-Hand Rule**:
   - Follows the walls of the maze.
   - May require backtracking to find the exit.
2. **Dijkstra**:
   - Finds the shortest path based on calculated distances.

---

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:<your-username>/<your-repo>.git
   cd <your-repo>
