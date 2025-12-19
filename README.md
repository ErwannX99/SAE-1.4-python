# SAE-1.4-python
code permetant a jjouer au puissance 4 avec un bras nirio de façon autonome 


# biblioteques utilisées :
        pynirio --> va permetre d'utiliser les commande pour controler le nyrio 
        time    --> utilisé sur une seul instance pour une 
        random  --> utilisé pour le mode random de jeu qui selectionne une colonne aleatoirement pour jouer
        serial  --> sert pour la lecture de la distance provenant du port serie envoyer par le capteur ultrason

# explication du programme:

# main:
## objectif : 
conntroler les partition du code par une partie central qui appelle les fonction necessaire

## specification
main fonctionne sur plusieurs fonction infini (while true) pemettant un fonctionnement continu, 
premier while true sert pour le choix de la difficulter avant de passer sur la seconde boucle
qui elle est la boucle infini du fonctionnement general et qui appelle les autre fonction 

## optimisation :
    amelioration de la visibiliter par des variables rennomées 
    supression de repetition dans le programme evitant d'utiliser des ressourse inutile

# Algorithme de décision Minimax 
## Algorithme d'anticipation et de prise de décision pour des jeux 
Objectif: Anticiper les coups dans la profondeur indiqué en utilisant 
une évaluation des coups possible ainsi qu'une exploration d'un arbre de possibilité 
des coups jouables 

## Spécification
Une variable DEPTH_MINMAX (profondeur du minimax) sert à définir la profondeur souhaité.
Cette variable prends un entier en entrée 

Fonction d'évaluation (eval_fonction)
fonction servant évaluer l'état du plateau pour anticiper les prochains coups 
Cette fonction crée des fenêtres ou elle va pondérer sa prédiction sur ce coup
(ex: fenêtre gagnante = +100, fenêtre menaçante = +10 et fenêtre menacée = -10 )

Fonction d'anticipation (minimax_alpha_beta)

Algorithme simulant l'alternance des coups entre lui et son adversaire afin d'anticiper
les coups et de prendre la décision du pion à jouer 

## Optimisation 

1.
Ajout d'un élagage alpha et bêta afin de mesurer son coups et celui de son adversaire, 
si le coup du minimax (alpha) à un score inférieur à celui de son adversaire (bêta),
il arrête d'explorer les branches qui découle de ce coup.

--> Permet d'optimiser le temps de réfléxion du minimax étant donné la réduction du nombre de 
coup à calculer. Réduit donc la consommation de ressources requise par le pc 

2.
Visualisation de l'état du plateau sur la même grille:

Au lieu de créer une seconde grille virtuel avec le même état du plateau pour simuler les coups,
la simulation est effectué directement sur la grille existante (toujours de manière virtuelle), une fois celle-ci terminée, les jetons seront retirés puis le véritable coup sera joué sur la grille réelle. 

--> évite la copie inutile de grille, parfois lourde optimisant ainsi les ressources de l'ordinateur

## Recommendation

Ne pas affecter à DEPTH_MINMAX une entrée au dessus de 10
--> Algorithme quasiment imbattable au delà de ce seuil, cela n'est donc pas nécessaire
--> Arbre de possibilité trop grand à parcourir, l'algorithme peut donc mettre énormément de temps 
à se décider 

Maintenir DEPTH_MINMAX entre 6 et 8 pour le temps réel
--> L'algorithme joue très rapidement (le premier coup peut prendre 10secondes puis temps réel)
--> Difficulté haute, algorithme pas imbattable mais difficilement 



# robot :






# logique_jeu :

## Objectif : Faire toute la logique du jeu du puissance 4

### def gravite_piece(matrice, colonne, piece):
Permet de quand on choisit une colonne faire que la pièce aille directement le plus bas possible comme si elles tombaient

### def verif_gagnant(matrice, joueur):
Permet de savoir quand un joueur a gagner en regardant toutes les colonnes si un joueur a gagné True est return

### def affichage(matrice):
C'est lui qui va afficher la matrice dans le terminal a chaque coups pour suivre le jeu depuis l'ordinateur

### def coups_valides(matrice):
Permet de savoir si un coup est valide ou non le main apres chaque coup de l'ordi et du joueur va regarder si le coup est possible 
ex: si un colonne est pleine le coup va etre annulé et on demande ou joueur de rejouer
Et aussi le programme va trier les colonnes restantes selon leurs proximité au center ce qui va aider le programme minmax

## Amélioration : Changement de nom de variable et de fonction
### Changement des noms de variables et de fonction pour une meilleur compréhension (dans tout les programmes):
c -> colonne 
col -> colonne 
r -> ligne 
row -> ligne 
drop_piece -> gravite_piece

