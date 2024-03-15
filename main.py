# Main file of the project
import matplotlib.pyplot as plt

def main():
    


def detecte_coordonnees_combinaison(grille, i, j):
    """
        Renvoie une liste contenant les coordonnées de tous les bonbons
        appartenant à la combinaison du bonbon (i, j).
    """


def affichage_grille(grille, nb_type_bonbons):
    """
        Affiche la grille de jeu "grille" contenant au
        maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons−1, cmap=’jet’)
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)
