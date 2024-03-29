from random import randint
import matplotlib.pyplot as plt


def main():
    # On crée la grille
    print("Lancement programme…")
    grille = creation_grille()
    # On affiche la grille
    afficher_grille(grille)

    fin = False
    while not fin:
        # On demande les coordonnees des deux cellules a echanger
        x1, y1, x2, y2 = map(int, input("coos :").split())
        print()

        print("on affiche l’échange")
        echange(grille, x1, y1, x2, y2)
        afficher_grille(grille)
        

        c1, c2 = dcb(grille, x1, y1), dcb(grille, x2, y2)
        print("On a c1 :", c1)
        print("On a c2 :", c2)
        if c1 == [] and c2 == []:
            echange(grille, x1, y1, x2, y2)
            afficher_grille(grille)
            print("Ça n’a pas provoqué de combinaison")
        else:
            print("Ça fait une comb")
            supprime_comb(grille, c1) # Modifie la grille pour enlever les combinaisons (une ou deux selon le cas)
            supprime_comb(grille, c2)
            afficher_grille(grille)

            boucle_suppression(grille)


def boucle_suppression(grille, afficher=True):
    # On recherche une combinaison
    c = combinaison_presente(grille)
    # Tant qu’il reste des combinaisons
    while c != []:
        supprime_comb(grille, c)
        if afficher:
            afficher_grille(grille)

        c = combinaison_presente(grille)
        print(c)


def combinaison_presente(grille):
    """
        Fonction qui renvoie une liste contenant les 3 2-uple de coordonnées de la première combinaison
        rencontrée (en partant de (0, 0)), ou une liste vide s’il n’y a pas de combinaison présente.
        Entrée : grille -> 2D list
        Sortie : list, la liste de coordonées des cellules formant la combinaison
    """ 
    trouve = False
    x, y = 0, 0
    while not trouve and x <= 4:
        while not trouve and y <= 4:
            c = dcb(grille, x, y)
            if c != []:
                trouve = True

            y += 1
        x += 1
        y = 0
    
    return c


def supprime_comb(grille, liste):
    """
        Fonction déplaçant les éléments de la grille au dessus des cellules contenues dans liste
        vers le bas et générant des nouvelles valeurs en haut de la grille.
        Entrées :
            * grille -> 2D list, la matrice du jeu
            * liste -> list, vide ou constituée de 3 couples de 2-uple qui correspond aux 
            coos. des bonbons de la combinaison.
        Sortie : None, la grille est modifiée directement
    """
    # Si liste est pas vide
    if liste != []:
        # Si c’est une combinaison horizontale (les x des 3 2-uple sont les mêmes)
        if liste[0][0] == liste[1][0] and liste[0][0] == liste[2][0]:
            # VERIFIER QUE LA COMB EXISTE ENCORE 
            # déplacer vers le bas
            for (x, y) in liste:
                for x_i in range(x, 0, -1):
                    grille[x_i][y] = grille[x_i-1][y]

                # Modifier valeurs en haut (3 en ligne ou 3 en colonne)
                grille[0][y] = randint(0, 3)
        
        # Sinon, c’est une combinaison verticale
        else:
            x, y = liste[0] # On prend le premier couple, qui est la case du bas de la comb.
            for _ in range(3):
                for i in range(y, 0, -1):
                    grille[i][y] = grille[i-1][y]

                grille[0][y] = randint(0, 3)
"""
test = [[0 for _ in range(5)] for _ in range(5)]
test[4][4], test[4][3], test[4][2] = 1, 1, 1
supprime_comb(test, [(4, 4), (4, 3), (4, 2)])
#supprime_comb(test, [(2, 2), (2, 3), (2, 4)])
for line in test:
    print(line)
"""

def dcb(grille, x, y): # NE MARCHE QUE SI ON TAPE D’EMBLÉE SUR LA CASE CENTRALE DE LA COMBINAISON
    """
        Fonction detecte_coordonnee_combinaison. Pour une cellule donnée, renvoie les coordonnées des bonbons constituant une combinaison 
        s'il y en a une, sinon une liste vide
        Entrée :
            * grille -> 2D list
            * x, y -> int, coordonnée de la cellule étudiée
        Sortie : list, vide si le bonbon ne forme pas une combinaison, les coordonnées des autres bonbons de la comb sinon.
    """
    coo_combinaison = []
    # Combinaison horizontale
    if (y > 0 and y < 4): # On ne teste pas x, supposant qu’il est compris entre 0 et 4
        combinaison_horizontale = (grille[x][y] == grille[x][y-1] and grille[x][y] == grille[x][y+1])
        if combinaison_horizontale:
            coo_combinaison = [(x, y-1), (x, y), (x, y+1)]

    # Combinaison verticale
    if coo_combinaison == [] and (x > 0 and x < 4): # On ne teste pas y, supposant qu’il est compris entre 0 et 4
        combinaison_verticale = (grille[x][y] == grille[x-1][y] and grille[x][y] == grille[x+1][y])
        if combinaison_verticale:
            coo_combinaison = [(x+1, y), (x, y), (x-1, y)] # On met d’abord celui du bas

    return coo_combinaison


def dcb(grille, x, y):
    coo_combinaison = []

    

    return coo_combinaison

"""
test = [[0 for _ in range(5)] for _ in range(5)]
test[0][0], test[1][0], test[2][0] = 1, 1, 1
print(dcb(test, 1, 0))
"""

def echange(grille, x1, y1, x2, y2):
    grille[x1][y1], grille[x2][y2] = grille[x2][y2], grille[x1][y1]


def creation_grille():
    grille = [[randint(0,3) for _ in range(5)] for _ in range(5)]
    boucle_suppression(grille)
    
    return grille


def afficher_grille(grille):
    for line in grille:
        for char in line:
            print(char, end=" ")
        print()
    print()


main()
