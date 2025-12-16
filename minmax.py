from pyniryo import *
import time
import random
import serial
from logique_jeu import drop_piece, verif_gagnant, coups_valides

PROFONDEUR_MINMAX = 7

def eval_fonction(matrice, joueur):
    score = 0
    adversaire = 2 if joueur == 1 else 1
    
    for r in range(6):
        for c in range(4):
            ligne = [matrice[r][c + i] for i in range(4)]
            if ligne.count(joueur) == 4:
                score += 100
            elif ligne.count(joueur) == 3 and ligne.count(0) == 1:
                score += 10
            
            if ligne.count(adversaire) == 3 and ligne.count(0) == 1:
                score -= 10
    
    for c in range(7):
        for r in range(3):
            colonne = [matrice[r + i][c] for i in range(4)]
            if colonne.count(joueur) == 4:
                score += 100
            elif colonne.count(joueur) == 3 and colonne.count(0) == 1:
                score += 10
            
            if colonne.count(adversaire) == 3 and colonne.count(0) == 1:
                score -= 10
    
    return score

def minmax_alpha_beta(matrice, depth, alpha, beta, maximizing, joueur):
    valid = coups_valides(matrice)
    terminal = verif_gagnant(matrice, 2) or verif_gagnant(matrice, 1) or len(valid) == 0 or depth == 0
    
    if terminal:
        if verif_gagnant(matrice, 2):
            return (None, 100000 + depth*100)
        elif verif_gagnant(matrice, 1):
            return (None, -10000 - depth*100)
        else:
            return (None, eval_fonction(matrice, 2))
    
    if maximizing:
        max_eval = -float('inf')
        best_col = random.choice(valid) if valid else None
        
        for col in valid:
            row = drop_piece(matrice, col, 2)
            if row is None:
                continue
            
            score = minmax_alpha_beta(matrice, depth-1, alpha, beta, False, joueur)[1]
            matrice[row][col] = 0
            
            if score > max_eval:
                max_eval = score
                best_col = col
            
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        
        return (best_col, max_eval)
    
    else:
        min_eval = float('inf')
        best_col = random.choice(valid) if valid else None
        
        for col in valid:
            row = drop_piece(matrice, col, 1)
            if row is None:
                continue
            
            score = minmax_alpha_beta(matrice, depth-1, alpha, beta, True, joueur)[1]
            matrice[row][col] = 0
            
            if score < min_eval:
                min_eval = score
                best_col = col
            
            beta = min(beta, score)
            if beta <= alpha:
                break
        
        return (best_col, min_eval)
