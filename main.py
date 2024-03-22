# Main file of the project
import matplotlib.pyplot as plt
from random import randint

def main():
    # Génération d’une grille correcte
    grille = creation_grille_aleatoire()
    
    # Jeu
    # Tant que echange_existe (un échange peut donner une combinaison)
    
    
def creation_grille_aleatoire():
    """
        Fonction créant une grille aléatoire qui ne contient aucune combinaison (déjà présente) et qui contient au moins un échange possible.
        Valeurs de la grille entre 0 et 3, taille de 5x5

        Sortie : grille -> 2D list, grille du jeu
    """
    grille = [[randint(0, 3) for _ in range(5)] for _ in range(5)]
    # On enlève toutes les combinaisons possibles
        
    # On vérifie qu’il existe au moins un échange qui entraine une combinaison
    
    # (Si c’est pas le cas on regénère la grille)
    
    return grille

def detecte_coordonnees_combinaison(grille, i, j):
    """
    entrée : grille, coordonnées (i,j) du bonbon
    sortie : une liste contenant les coordonnées de tous les bonbons
        appartenant à la combinaison du bonbon (i, j).
    """


def affichage_grille(grille, nb_type_bonbons=4):
    """
        Affiche la grille de jeu "grille" contenant au
        maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons−1, cmap=’jet’)
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)

def modification_grille(grille):
  '''
entrée : grille 
sortie : rien
Prend en entrée une grille qui présente des combinaison. La fonction supprime ces combinaisons et remplace dans la grille les espaces vides par des bonbons choisis aléatoirement
  '''

def test_detecte_coordonnees_combinaison(): 
""" Test la fonction detecte_coordonnees_combinaison(grille, i, j). 
Pour chaque cas de test, affiche True si le test passe, False sinon 
"""

def decalage_bas(grille):
