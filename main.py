from pyniryo import *
import time
import random
import serial
from logique_jeu import drop_piece, verif_gagnant, affichage
from robot import port_serie, robot, pick_robot_piece

matrice = [[0 for _ in range(7)] for _ in range(6)]
joueur = 1

while True:
    print("Choisissez le mode du robot (1 = aléatoire, 2 = minmax): ")
    try:
        mode_robot = int(input())
        if not (mode_robot == 1 or mode_robot == 2):
            raise ValueError
        break
    except ValueError:
        print("Tapez 1 ou 2.")

while True:
    affichage(matrice)
    
    if joueur == 1:
        port_serie.reset_input_buffer()
        while True:
            donnee_cm = port_serie.readline()
            try:
                texte_recue = int(donnee_cm.decode("utf-8").strip())
                if not texte_recue:
                    continue
                distance = int(texte_recue)
            except ValueError:
                continue
            
            if distance==3:
                col = 0
                robot.play_sound('connected.wav')
            elif distance==7:
                col = 1
                robot.play_sound('connected.wav')
            elif distance==11:
                col = 2
                robot.play_sound('connected.wav')
            elif distance==14:
                col = 3
                robot.play_sound('connected.wav')
            elif distance==18:
                col = 4
                robot.play_sound('connected.wav')
            elif distance==22:
                col = 5
                robot.play_sound('connected.wav')
            elif distance==26:
                col = 6
                robot.play_sound('connected.wav')
            else :
                continue
            
            if not (0 <= col < 7):
                print("Colonne hors limite.")
                robot.play_sound('error.wav')
                continue
            
            if matrice[0][col] != 0:
                print("Colonne pleine.")
                robot.play_sound('error.wav')
                port_serie.reset_input_buffer()
                continue
            
            break
        
        drop_piece(matrice, col, joueur)
    
    else:
        col = pick_robot_piece(matrice, mode_robot)
        drop_piece(matrice, col, joueur)
    
    if verif_gagnant(matrice, joueur):
        affichage(matrice)
        print(f"Le joueur {joueur} gagne !")
        if joueur == 1:
            robot.play_sound('ready.wav')
        if joueur == 2:
            robot.play_sound('error.wav')
        robot.release_with_tool()
        break
    
    if all(matrice[0][i] != 0 for i in range(7)):
        affichage(matrice)
        print("Égalité, la grille est pleine.")
        break
    
    joueur = 2 if joueur == 1 else 1

robot.close_connection()
