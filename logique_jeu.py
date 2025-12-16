from pyniryo import *
import time
import random 
import serial

#lacher la pièce
def drop_piece(matrice, col, piece):
    for row in range(5, -1, -1):
        if matrice[row][col] == 0:
            matrice[row][col] = piece
            return row
    return None

def verif_gagnant(matrice, joueur):
    for r in range(6):
        for c in range(4):
            if all(matrice[r][c + i] == joueur for i in range(4)):
                return True
    
    for c in range(7):
        for r in range(3):
            if all(matrice[r + i][c] == joueur for i in range(4)):
                return True
    
    for r in range(3):
        for c in range(4):
            if all(matrice[r + i][c + i] == joueur for i in range(4)):
                return True
    
    for r in range(3, 6):
        for c in range(4):
            if all(matrice[r - i][c + i] == joueur for i in range(4)):
                return True
    
    return False

def affichage(matrice):
    print(" " + " ".join(str(i+1) for i in range(7)))
    for ligne in matrice:
        print("| " + " ".join(str(x) if x != 0 else "." for x in ligne))
    print()

def coups_valides(matrice):
    center = 3
    cols = [c for c in range(7) if matrice[0][c] == 0]
    cols.sort(key=lambda c: abs(c - center))
    return cols

