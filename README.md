# SAE-1.4-python
code permetant a jjouer au puissance 4 avec un bras nirio de façon autonome 


biblioteque utiliser:


#explication du programme:

main:
main sert a controler toute les autre parties du codes et appeller les fonctions necessaire.



logique_jeu:


robot:


## Algorithme de décision Minimax 
# Algorithme d'anticipation et de prise de décision pour des jeux 
Objectif: Anticiper les coups dans la profondeur indiqué en utilisant 
une évaluation des coups possible ainsi qu'une exploration d'un arbre de possibilité 
des coups jouables 

# Spécification
Une variable DEPTH_MINMAX (profondeur du minimax) sert à définir la profondeur souhaité.
Cette variable prends un entier en entrée 

Fonction d'évaluation (eval_fonction)
fonction servant évaluer l'état du plateau pour anticiper les prochains coups 
Cette fonction crée des fenêtres ou elle va pondérer sa prédiction sur ce coup
(ex: fenêtre gagnante = +100, fenêtre menaçante = +10 et fenêtre menacée = -10 )

Fonction d'anticipation (minimax_alpha_beta)

Algorithme simulant l'alternance des coups entre lui et son adversaire afin d'anticiper
les coups et de prendre la décision du pion à jouer 

# Optimisation 

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

# Recommendation

Ne pas affecter à DEPTH_MINMAX une entrée au dessus de 10
--> Algorithme quasiment imbattable au delà de ce seuil, cela n'est donc pas nécessaire
--> Arbre de possibilité trop grand à parcourir, l'algorithme peut donc mettre énormément de temps 
à se décider 

Maintenir DEPTH_MINMAX entre 6 et 8 pour le temps réel
--> L'algorithme joue très rapidement (le premier coup peut prendre 10secondes puis temps réel)
--> Difficulté haute, algorithme pas imbattable mais difficilement 
