from pyniryo import *

import time
import random
import serial

from logique_jeu import drop_piece, verif_gagnant, coups_valides

PROFONDEUR_MINMAX = 7

def eval_fonction(matrice, joueur):
    score = 0
    adversaire = 2 if joueur == 1 else 1

    # lignes horizontales
    for ligne in range(6):
        for colonne in range(4):
            fenetre = [matrice[ligne][colonne + i] for i in range(4)]
            if fenetre.count(joueur) == 4:
                score += 100
            elif fenetre.count(joueur) == 3 and fenetre.count(0) == 1:
                score += 10
            if fenetre.count(adversaire) == 3 and fenetre.count(0) == 1:
                score -= 10

    # colonnes verticales
    for colonne in range(7):
        for ligne in range(3):
            fenetre = [matrice[ligne + i][colonne] for i in range(4)]
            if fenetre.count(joueur) == 4:
                score += 100
            elif fenetre.count(joueur) == 3 and fenetre.count(0) == 1:
                score += 10
            if fenetre.count(adversaire) == 3 and fenetre.count(0) == 1:
                score -= 10

    return score

def minmax_alpha_beta(matrice, profondeur, alpha, beta, maximizing, joueur):
    colonnes_valides = coups_valides(matrice)
    terminal = (
        verif_gagnant(matrice, 2)
        or verif_gagnant(matrice, 1)
        or len(colonnes_valides) == 0
        or profondeur == 0
    )

    if terminal:
        if verif_gagnant(matrice, 2):
            return (None, 100000 + profondeur * 100)
        elif verif_gagnant(matrice, 1):
            return (None, -10000 - profondeur * 100)
        else:
            return (None, eval_fonction(matrice, 2))

    if maximizing:
        max_eval = -float("inf")
        meilleure_colonne = random.choice(colonnes_valides) if colonnes_valides else None
        for colonne in colonnes_valides:
            ligne = drop_piece(matrice, colonne, 2)
            if ligne is None:
                continue
            score = minmax_alpha_beta(
                matrice, profondeur - 1, alpha, beta, False, joueur
            )[1]
            matrice[ligne][colonne] = 0
            if score > max_eval:
                max_eval = score
                meilleure_colonne = colonne
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return (meilleure_colonne, max_eval)
    else:
        min_eval = float("inf")
        meilleure_colonne = random.choice(colonnes_valides) if colonnes_valides else None
        for colonne in colonnes_valides:
            ligne = drop_piece(matrice, colonne, 1)
            if ligne is None:
                continue
            score = minmax_alpha_beta(
                matrice, profondeur - 1, alpha, beta, True, joueur
            )[1]
            matrice[ligne][colonne] = 0
            if score < min_eval:
                min_eval = score
                meilleure_colonne = colonne
            beta = min(beta, score)
            if beta <= alpha:
                break
        return (meilleure_colonne, min_eval)
