from pyniryo import *
import time
import random
import serial
from logique_jeu import drop_piece, verif_gagnant, coups_valides  #importations des différentes parties du programme
#importation des bibliothèques nécessaire au fonctionnement 
depth_MINMAX = 7 #nombre de coup calculer à l'avance


def eval_fonction(matrice, joueur): 
    """ 
    Evalue la qualité de l'état du plateau pour le joueur
    
    Variable:
        matrice : (list): Grille 2D représentant le jeu puissance 4 sous forme de matrice
        joueur : (int): Identifiant du joueur  

    Returns:
        Score: (int) : Score calculées 
    """
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

    for ligne in range(3):
        for colonne in range (4):
            fenetre = [matrice[ligne + i] + [colonne + i ]for i in range(4)]
            if fenetre.count(joueur) == 4:
                score += 100
            elif fenetre.count(joueur) == 3 and fenetre.count(0) == 1:
                score += 10
                
            if fenetre.count(adversaire) == 3 and fenetre.count(0) == 1:
                score -= 10

    for ligne in range(3-6):
        for colonne in range(4):
            fenetre = [matrice[ligne + i] + [colonne + i ]for i in range(4)]
            if fenetre.count(joueur) == 4:
                score += 100
            elif fenetre.count(joueur) == 3 and fenetre.count(0) == 1:
                score += 10
                
            if fenetre.count(adversaire) == 3 and fenetre.count(0) == 1:
                score -= 10


    return score


def minmax_alpha_beta(matrice, depth, alpha, beta, maximizing, joueur): #fonctionnement du minimax & opitimisation
    """
    Execute minimax pour trouver le coup le plus pertinent
    Simule les coups avec une alternance joueur adversaire pour trouver le coup donnant 
    la plus grande chance de victoire 
    
    Variable:
        matrice : (list) : Grille 2D du puissance 4 
        depth : (int) : Profondeur (nombre de coup calculé à l'avance )
        alpha: (float) : Valeur du meilleur score de l'algo
        beta: (float) : Valeur du pire score de l'adversaire
        maximizing: (bool) : True si l'algo doit maximiser le score, False dans le cas contraire
        joueur : (int) : identifiant du joueur donc le tour est simulé 

    Returns: 
        best_col: (int où None): indice de la meilleur colonne a jouer (none si fin du jeu)
        score: (float) : score de l'évaluation  de la position atteinte 
    """
    
    valid = coups_valides(matrice)
    terminal = verif_gagnant(matrice, 2) or verif_gagnant(matrice, 1) or len(valid) == 0 or depth == 0
    #terminal correspond à l'arrêt de la simulation 

    if terminal:
        if verif_gagnant(matrice, 2):
            return (None, 100000 + depth * 100)
        elif verif_gagnant(matrice, 1):
            return (None, -10000 - depth * 100)
        else:
            return (None, eval_fonction(matrice, 2))

    #l'algo trouve le score le plus maximisant pour lui
    if maximizing:
        max_eval = -float("inf")
        best_col = random.choice(valid) if valid else None
       
        for colonne in valid:
            ligne = drop_piece(matrice, colonne, 2)
            if ligne is None:
                continue
           
            score = minmax_alpha_beta(matrice, depth - 1, alpha, beta, False, joueur)[1]
            matrice[ligne][colonne] = 0
           
            if score > max_eval:
                max_eval = score
                best_col = colonne
          
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        
        return (best_col, max_eval)
    else:
        min_eval = float("inf")
        best_col = random.choice(valid) if valid else None
        
        for colonne in valid:
            ligne = drop_piece(matrice, colonne, 1)
            if ligne is None:
                continue
      
            score = minmax_alpha_beta(matrice, depth - 1, alpha, beta, True, joueur)[1]
            matrice[ligne][colonne] = 0
         
            if score < min_eval:
                min_eval = score
                best_col = colonne
         
            beta = min(beta, score)
            if beta <= alpha:
                break

        return (best_col, min_eval)
