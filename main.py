# Importation des bibiloithèques
from pyniryo import *              
import serial

from logique_jeu import gravite_piece, verif_gagnant, affichage        # Importation des fonctions créer sur les autres codes
from robot import port_serie, robot, pick_robot_piece

port_serie = serial.Serial("COM3", baudrate=9600, timeout=2) # Ouverture de la liaison série

# Création de la matrice pour visualiser le jeu
matrice = [[0 for _ in range(7)] for _ in range(6)]                

joueur = 1

# Choix du mode 
while True:                                                         
    print("Choisissez le mode du robot (1 = aléatoire, 2 = minmax): ")
    try:
        mode_robot = int(input())
        if not (mode_robot == 1 or mode_robot == 2):                # Recomence la boucle si une valeur autre que 1 ou 2 est entrée
            raise ValueError
        break
    except ValueError:
        print("Tapez 1 ou 2.")

while True:
    affichage(matrice)

    if joueur == 1:                                             # permet de lancer la lecture des distances uniquement si c'est au tour du joueur
        port_serie.reset_input_buffer()

        while True:
            donnee_cm = port_serie.readline()                        # Lecture de la distance envoyer sur le port série
            try:
                distance = int(donnee_cm.decode("utf-8").strip())    #Retire le préfix utf-8 et le transforme en int pour une lecture correcte
                if not distance:                                     # Si aucune donnée n'est reçue, recommence la boucle
                    continue
            except ValueError:
                continue

            if distance == 3:                       # Vérifie la distance pour chaque colonne     
                colonne = 0                         # Numéro de la colonne 
            elif distance == 7:
                colonne = 1
            elif distance == 11:
                colonne = 2
            elif distance == 14:
                colonne = 3
            elif distance == 18:
                colonne = 4
            elif distance == 22:
                colonne = 5
            elif distance == 26:
                colonne = 6
            else:
                continue
            
            if colonne <= 6 :
                robot.play_sound('connected.wav')

            # Vérifie si le entrée colonne n'est pas hors limite    
            if not (0 <= colonne < 7):              
                print("Colonne hors limite.")
                robot.play_sound('error.wav')
                continue

            # Vérifie si la colonne est pleine
            if matrice[0][colonne] != 0:           
                print("Colonne pleine.")
                robot.play_sound('error.wav')
                port_serie.reset_input_buffer()
                continue

            break

        gravite_piece(matrice, colonne, joueur)

    else:
        colonne = pick_robot_piece(matrice, mode_robot)
        gravite_piece(matrice, colonne, joueur)

# Vérifie si la matrice est une matrice gagnante
    if verif_gagnant(matrice, joueur):              # Sélectionne la matrice a regardé et le joueur à verifier
        affichage(matrice)                          # Affiche la matrice finale
        print(f"Le joueur {joueur} gagne !")        
        if joueur == 1:                             # Joue un son différent selon le gagnant
            robot.play_sound('ready.wav')
        if joueur == 2:
            robot.play_sound('error.wav')
        robot.release_with_tool()
        break

# Vérifie si la matrice est pleine
    if all(matrice[0][i] != 0 for i in range(7)):       
        affichage(matrice)                              
        print("Égalité, la grille est pleine.")         
        break                                           

    joueur = 2 if joueur == 1 else 1              

robot.close_connection()