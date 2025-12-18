from pyniryo import *
import time
import random
import serial
from logique_jeu import gravite_piece, coups_valides
from minmax import minmax_alpha_beta, PROFONDEUR_MINMAX

port_serie = serial.Serial("COM3", baudrate = 9600, timeout=2)

robot = NiryoRobot("10.216.30.1")
robot.calibrate_auto()
robot.update_tool()

z = 0.2
zp = 0.371
zpb = 0.331
zb = 0.106
x0 = 0.068
x = 0.28
x1 = 0.277
x2 = 0.283

pose_y = [-0.144, -0.115, -0.080, -0.045, -0.015, 0.020, 0.053, 0.086]

roll = -1.57
pitch = 1.57

Pose0 = [x0, pose_y[0], zp, 0, pitch, 0]
Pose0m = [x0, pose_y[0], z, 0, pitch, 0]
Pose0b = [x0, pose_y[0], zb, 0, pitch, 0]
Pose1 = [x1, pose_y[1], zp, roll, pitch, 0]
Pose1p = [x1, pose_y[1], zpb, roll, pitch, 0]
Pose2 = [x1, pose_y[2], zp, roll, pitch, 0]
Pose2p = [x1, pose_y[2], zpb, roll, pitch, 0]
Pose3 = [x, pose_y[3], zp, roll, pitch, 0]
Pose3p = [x, pose_y[3], zpb, roll, pitch, 0]
Pose4 = [x, pose_y[4], zp, roll, pitch, 0]
Pose4p = [x, pose_y[4], zpb, roll, pitch, 0]
Pose5 = [x2, pose_y[5], zp, roll, pitch, 0]
Pose5p = [x2, pose_y[5], zpb, roll, pitch, 0]
Pose6 = [x2, pose_y[6], zp, roll, pitch, 0]
Pose6p = [x2, pose_y[6], zpb, roll, pitch, 0]
Pose7 = [x2, pose_y[7], zp, roll, pitch, 0]
Pose7p = [x2, pose_y[7], zpb, roll, pitch, 0]

Maison = [0, 0.28, -0.12, 0, -pitch, 0]

def pick_robot_piece(matrice, mode):
    if mode == 1:
        Algorithme_de_choix = random.choice(coups_valides(matrice)) + 1
    else:
        col_minmax, _ = minmax_alpha_beta(matrice, PROFONDEUR_MINMAX, -float('inf'), float('inf'), True, 2)
        Algorithme_de_choix = (col_minmax + 1) if col_minmax is not None else random.choice(coups_valides(matrice)) + 1
    
    robot.play_sound('learning_trajectory.wav')
    robot.move_joints(Maison)
    robot.move_pose(Pose0)
    robot.move_pose(Pose0m)
    robot.release_with_tool()
    robot.move_pose(Pose0b)
    robot.grasp_with_tool()
    robot.move_linear_pose(Pose0)
    
    poses = [Pose1, Pose2, Pose3, Pose4, Pose5, Pose6, Pose7]
    poses_p = [Pose1p, Pose2p, Pose3p, Pose4p, Pose5p, Pose6p, Pose7p]
    
    robot.move_linear_pose(poses[Algorithme_de_choix - 1])
    robot.move_linear_pose(poses_p[Algorithme_de_choix - 1])
    time.sleep(1)
    robot.release_with_tool()
    robot.move_pose(poses[Algorithme_de_choix - 1])
    robot.move_joints(Maison)
    
    print(f"[Robot] Jeton posé colonne {Algorithme_de_choix}")
    robot.play_sound('disconnected.wav')
    
    return Algorithme_de_choix - 1
