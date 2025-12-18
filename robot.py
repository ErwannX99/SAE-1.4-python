# Importer les bibliothèques nécessaires au projet ainsi que les fonctions qui ont été créées dans d'autres fichiers
from pyniryo import *  
import time  
import random  
import serial  
from logique_jeu import drop_piece, coups_valides  
from minmax import minmax_alpha_beta, PROFONDEUR_MINMAX  

port_serie = serial.Serial("COM3", baudrate=9600, timeout=2) # Ouverture de la liaison série

# Connexion au robot Niryo, calibration automatique des axes et détection de l'outil monté
robot = NiryoRobot("10.216.30.1") 
robot.calibrate_auto() 
robot.update_tool() 

# Définition des coordonnées cartésiennes du plateau de jeu : hauteurs (z), positions horizontales (x) et colonnes (y)
hauteurs = {'z': 0.2, 'zp': 0.371, 'zpb': 0.331, 'zb': 0.106} 
positions_x = {'x0': 0.068, 'x': 0.28, 'x1': 0.277, 'x2': 0.283} 
positions_y = {'0': -0.144, '1': -0.115, '2': -0.080, '3': -0.045, '4': -0.015, '5': 0.020, '6': 0.053, '7': 0.086} 

# Degré de rotation en radian
rotation_x = -1.57 
rotation_y = 1.57 

# Chaque pose est une liste de 6 valeurs : [X, Y, Z, rotation_X, rotation_Y, rotation_Z]
# Position 0 : zone de prise du jeton
Pose0 = [positions_x['x0'], positions_y['0'], hauteurs['zp'], 0, rotation_y, 0] # Hauteur haute au-dessus du jeton
Pose0m = [positions_x['x0'], positions_y['0'], hauteurs['z'], 0, rotation_y, 0] # Hauteur moyenne entre les deux
Pose0b = [positions_x['x0'], positions_y['0'], hauteurs['zb'], 0, rotation_y, 0] # Hauteur basse pour saisir le jeton
# Positions 1 à 7 : les 7 colonnes du Puissance 4 
Pose1 = [positions_x['x1'], positions_y['1'], hauteurs['zp'], rotation_x, rotation_y, 0] # Colonne 1 - hauteur haute colonne
Pose1p = [positions_x['x1'], positions_y['1'], hauteurs['zpb'], rotation_x, rotation_y, 0] # Colonne 1 - hauteur basse pour déposer
Pose2 = [positions_x['x1'], positions_y['2'], hauteurs['zp'], rotation_x, rotation_y, 0]
Pose2p = [positions_x['x1'], positions_y['2'], hauteurs['zpb'], rotation_x, rotation_y, 0] 
Pose3 = [positions_x['x'], positions_y['3'], hauteurs['zp'], rotation_x, rotation_y, 0] 
Pose3p = [positions_x['x'], positions_y['3'], hauteurs['zpb'], rotation_x, rotation_y, 0]
Pose4 = [positions_x['x'], positions_y['4'], hauteurs['zp'], rotation_x, rotation_y, 0] 
Pose4p = [positions_x['x'], positions_y['4'], hauteurs['zpb'], rotation_x, rotation_y, 0]
Pose5 = [positions_x['x2'], positions_y['5'], hauteurs['zp'], rotation_x, rotation_y, 0]
Pose5p = [positions_x['x2'], positions_y['5'], hauteurs['zpb'], rotation_x, rotation_y, 0]
Pose6 = [positions_x['x2'], positions_y['6'], hauteurs['zp'], rotation_x, rotation_y, 0] 
Pose6p = [positions_x['x2'], positions_y['6'], hauteurs['zpb'], rotation_x, rotation_y, 0]
Pose7 = [positions_x['x2'], positions_y['7'], hauteurs['zp'], rotation_x, rotation_y, 0]
Pose7p = [positions_x['x2'], positions_y['7'], hauteurs['zpb'], rotation_x, rotation_y, 0]

Maison = [0, 0.28, -0.12, 0, -rotation_y, 0] # Position d'attente entre chaque action

def pick_robot_piece(matrice, mode): 
    if mode == 1:  
        colonne = random.choice(coups_valides(matrice)) + 1 # Choisit une colonne jouable au hasard puis ajoute 1 car les colonnes vont de 1 à 7 et non de 0 à 6
    else: 
        col_minmax, _ = minmax_alpha_beta(matrice, PROFONDEUR_MINMAX, -float('inf'), float('inf'), True, 2) # Minimax : calcul du meilleur coup (joueur 2, élagage alpha-bêta)
        colonne = (col_minmax + 1) if col_minmax is not None else random.choice(coups_valides(matrice)) + 1 # Conversion index → colonne réelle (+1), ou coup aléatoire si échec

    # Séquence de saisie d'un pion dans la réserve
    robot.play_sound('learning_trajectory.wav')
    robot.move_joints(Maison)
    robot.move_pose(Pose0)
    robot.move_pose(Pose0m)
    robot.release_with_tool()
    robot.move_pose(Pose0b)
    robot.grasp_with_tool()
    robot.move_linear_pose(Pose0)
    
    # Coordonnées des 7 colonnes : hauteur au-dessus du jeu et hauteur de dépôt du jeton
    poses_haut = [Pose1, Pose2, Pose3, Pose4, Pose5, Pose6, Pose7]
    poses_bas = [Pose1p, Pose2p, Pose3p, Pose4p, Pose5p, Pose6p, Pose7p]
    
    # Séquence du dépôt du jeton
    robot.move_linear_pose(poses_haut[colonne - 1])
    robot.move_linear_pose(poses_bas[colonne - 1])
    time.sleep(1)
    robot.release_with_tool()
    robot.move_pose(poses_haut[colonne - 1])
    robot.move_joints(Maison)
    
    print(f"[Robot] Jeton posé colonne {colonne}")
    robot.play_sound('disconnected.wav')
    
    return colonne - 1 # Retourne l'index de la colonne entre 0 et 6
