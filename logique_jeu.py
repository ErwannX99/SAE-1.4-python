from pyniryo import *
#test
import time
import random
import serial

def drop_piece(matrice, colonne, piece):
    for ligne in range(5, -1, -1):
        if matrice[ligne][colonne] == 0:
            matrice[ligne][colonne] = piece
            return ligne
    return None

def verif_gagnant(matrice, joueur):
    # lignes horizontales
    for ligne in range(6):
        for colonne in range(4):
            if all(matrice[ligne][colonne + i] == joueur for i in range(4)):
                return True

    # colonnes verticales
    for colonne in range(7):
        for ligne in range(3):
            if all(matrice[ligne + i][colonne] == joueur for i in range(4)):
                return True

    # diagonales montantes
    for ligne in range(3):
        for colonne in range(4):
            if all(matrice[ligne + i][colonne + i] == joueur for i in range(4)):
                return True

    # diagonales descendantes
    for ligne in range(3, 6):
        for colonne in range(4):
            if all(matrice[ligne - i][colonne + i] == joueur for i in range(4)):
                return True

    return False

def affichage(matrice):
    print(" " + " ".join(str(i+1) for i in range(7)))
    for ligne in matrice:
        print("| " + " ".join(str(x) if x != 0 else "." for x in ligne))
    print()

def coups_valides(matrice):
    center = 3
    colonnes = [colonne for colonne in range(7) if matrice[0][colonne] == 0]
    colonnes.sort(key=lambda colonne: abs(colonne - center))
    return colonnes
