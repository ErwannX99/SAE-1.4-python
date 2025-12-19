# SAE-1.4-python

Code permettant a joué au puissance 4 avec un bras niryo de façon autonome. 

# bibliothèques utilisées :

        Pyniryo --> va permettre d'utiliser les commande pour contrôler le nyrio 

        Time    --> utilisé sur une seul instance pour une 

        Random  --> utilisé pour le mode random de jeu qui sélectionne une colonne aléatoirement pour jouer

        Serial --> sert pour la lecture de la distance provenant du port série envoyer par le capteur ultrason

# explication du programme :

# main:

## objectif : 

Contrôler les partitions du code par une partie centrale qui appelle les fonctions nécessaires

## specification

main fonctionne sur plusieurs fonctions infinies (while true) permettant un fonctionnement continu.

Premier while true sert pour le choix de la difficulté avant de passer sur la seconde boucle

Qui elle est la boucle infinie du fonctionnement général et qui appelle les autres fonctions 

## Optimisation :

    Amélioration de la visibilité par des variables renommées 

    Suppression de répétition dans le programme évitant d'utiliser des ressources inutiles

# Algorithme de décision Minimax 

## Algorithme d'anticipation et de prise de décision pour des jeux 

Objectif : anticiper les coups dans la profondeur indiquée en utilisant 

Une évaluation des coups possible ainsi qu'une exploration d'un arbre de possibilité 

Des coups jouables 

## Spécification

Une variable DEPTH_MINMAX (profondeur du minimax) sert à définir la profondeur souhaitée.

Cette variable prend un entier en entrée. 

Fonction d'évaluation (eval_fonction)

fonction servant évalué l'état du plateau pour anticiper les prochains coups 

Cette fonction crée des fenêtres où elle va pondérer sa prédiction sur ce coup.

(Ex: fenêtre gagnante = +100, fenêtre menaçante = +10 et fenêtre menacée = -10)

Fonction d'anticipation (minimax_alpha_beta)

Algorithme simulant l'alternance des coups entre lui et son adversaire afin d'anticiper

Les coups et de prendre la décision du pion à jouer 

## Optimisation 

1.

Ajout d'un élagage alpha et bêta afin de mesurer son coup et celui de son adversaire, 

Si le coup du minimax (alpha) à un score inférieur à celui de son adversaire (bêta),

Il arrête d'explorer les branches qui découlent de ce coup.

--> Permet d'optimiser le temps de réflexion du minimax étant donné la réduction du nombre de 

coup à calculer. Réduit donc la consommation de ressources requise par le PC 

2.

Visualisation de l'état du plateau sur la même grille :

Au lieu de créer une seconde grille virtuelle avec le même état du plateau pour simuler les coups,

La simulation est effectuée directement sur la grille existante (toujours de manière virtuelle), une fois celle-ci terminée, les jetons seront retirés puis le véritable coup sera joué sur la grille réelle. 

--> évite la copie inutile de grille, parfois lourde optimisant ainsi les ressources de l'ordinateur

## Recommendation

Ne pas affecter à DEPTH_MINMAX une entrée au-dessus de 10

--> Algorithme quasiment imbattable au-delà de ce seuil, cela n'est donc pas nécessaire

--> Arbre de possibilité trop grand à parcourir, l'algorithme peut donc mettre énormément de temps 

À se décider 

Maintenir DEPTH_MINMAX entre 6 et 8 pour le temps réel

--> L'algorithme joue très rapidement (le premier coup peut prendre 10 secondes puis temps réel)

--> Difficulté haute, algorithme pas imbattable mais difficilement 

## Version

v1.0: Minimax fonctionnel, ne joue pas de manière purement intelligente car ne calcule pas les fenêtres diagonales. 

v1.1: Ajout des fenêtres diagonales

# robot :

## objectif :

Contrôle des mouvements du niryo avec des positions généralisées 

## Spécification :

    Hauteur tuple des hauteur

    position_X tuple des positions des x 

    position_Y tuple des positions des Y

    Position haute et drop utilise les tuples précèdent

    Des fonctions move_linear_pose utilise les positions et drop en fonction des colonne choisis 

# Optimisation :

    Rassemblement des variables en tuple 

    meilleur nom de variable

# logique_jeu :

## Objectif : faire toute la logique du jeu du puissance 4

### def gravite_piece(matrice, colonne, piece):

Permet de quand on choisit une colonne faire que la pièce aille directement le plus bas possible comme si elles tombaient

### def verif_gagnant(matrice, joueur):

Permet de savoir quand un joueur a gagné en regardant toutes les colonnes si un joueur à gagner True est return

### def affichage(matrice):

C'est lui qui va afficher la matrice dans le terminal à chaque coup pour suivre le jeu depuis l'ordinateur.

### def coups_valides(matrice):

Permet de savoir si un coup est valide ou non le main après chaque coup de l'ordi et du joueur va regarder si le coup est possible 

ex: si une colonne est pleine, le coup va être annulé et on demande ou joueur de rejouer.

Et aussi le programme va trier les colonnes restantes selon leur proximité au centre ce qui va aider le programme minmax

## Amélioration : changement de nom de variable et de fonction

### Changement des noms de variables et de fonction pour une meilleure compréhension (dans tout les programmes):

c -> colonne 

col -> colonne 

r -> ligne 

row -> ligne 

drop_piece -> gravite_piece

