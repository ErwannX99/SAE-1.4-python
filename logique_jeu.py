from pyniryo import *
import time
import random
import serial

def gravite_piece(matrice, colonne, piece):
    """Dépose une pièce dans la colonne donnée.
    Parcourt la colonne de bas en haut (index 5 à 0) et place
    la valeur `piece` dans la première cellule vide rencontrée.
    ça imite la gravité.

    Args:
        matrice (list[list[int]]): la grille 6x7 du jeu (0=vide)(1=joueur 2=robot)
        colonne (int): index de la colonne (0 à 6)
        piece (int): nombre du joueur (1 ou 2)

    Returns:
        int | None: le numéro de la ligne où la pièce a été posée,
                    ou None si la colonne est pleine
    """
    for ligne in range(5, -1, -1):
        if matrice[ligne][colonne] == 0:
            matrice[ligne][colonne] = piece
            return ligne
    return None

def verif_gagnant(matrice, joueur):
    """Vérifie si le `joueur` a 4 pièces alignées.
    Recherche les alignements horizontaux, verticaux et diagonaux
    (montants et descendants). Renvoie True dès qu'un alignement
    de longueur 4 est trouvé.

    Args:
        matrice (list[list[int]]): la grille 6x7
        joueur (int): identifiant du joueur à tester

    Returns:
        bool: True si le joueur a gagné, False sinon
    """
    # lignes horizontales
    for ligne in range(6):
        for colonne in range(4):
            # on vérifie 4 cases consécutives sur la ligne
            if all(matrice[ligne][colonne + i] == joueur for i in range(4)):
                return True

    # colonnes verticales
    for colonne in range(7):
        for ligne in range(3):
            # on vérifie 4 cases consécutives dans la colonne
            if all(matrice[ligne + i][colonne] == joueur for i in range(4)):
                return True

    # diagonales montantes (bas-gauche -> haut-droit)
    for ligne in range(3):
        for colonne in range(4):
            if all(matrice[ligne + i][colonne + i] == joueur for i in range(4)):
                return True

    # diagonales descendantes (haut-gauche -> bas-droit)
    for ligne in range(3, 6):
        for colonne in range(4):
            if all(matrice[ligne - i][colonne + i] == joueur for i in range(4)):
                return True

    return False

def affichage(matrice):
    """Affiche la grille sur la sortie standard.
    Les colonnes sont numérotées 1 à 7 et les
    cases vides sont affichées par un point "."
    """
    # numéro des colonnes
    print(" " + " ".join(str(i+1) for i in range(7)))
    for ligne in matrice:
        # remplacer 0 par des "." pour la lisibilité
        print("| " + " ".join(str(x) if x != 0 else "." for x in ligne))
    print()

def coups_valides(matrice):
    """Retourne la liste des indices de colonnes jouables.
    La liste est triée pour favoriser le centre (colonne 3)
    """
    center = 3
    # une colonne est valide si la case du haut (ligne 0) est vide
    colonnes = [colonne for colonne in range(7) if matrice[0][colonne] == 0]
    # trier par le plus proche du centre (3)
    colonnes.sort(key=lambda colonne: abs(colonne - center))
    return colonnes