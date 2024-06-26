from random import randint
import matplotlib.pyplot as plt


def main():
    # On crée la grille
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
            print("Ça fait une combinaison")
            supprime_comb(grille, c1) # Modifie la grille pour enlever les combinaisons (une ou deux selon le cas)
            supprime_comb(grille, c2)
            boucle_suppression(grille)
            fin = test_fini(grille)
    print(" Game over ")


def boucle_suppression(grille, afficher=True):
    # On recherche une combinaison
    c = combinaison_presente(grille)
    # Tant qu’il reste des combinaisons
    while c != []:
        supprime_comb(grille, c)

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

def dcb(grille, x, y):
    """
        Fonction detecte_coordonnee_combinaison. Pour une cellule donnée, renvoie les coordonnées des bonbons constituant une combinaison 
        s'il y en a une, sinon une liste vide.
        Entrée :
            * grille -> 2D list
            * x, y -> int, coordonnée de la cellule étudiée
        Sortie : 
            * list -> vide si le bonbon ne forme pas une combinaison, les coordonnées des autres bonbons de la comb sinon.
    """
    
    liste = []
    
    if 0 <= x-2:
        if grille[x-2][y] == grille[x-1][y] == grille[x][y]:
            liste = [(x-2,y), (x-1,y), (x,y)]
            
    if x-1 >= 0 and x+1 <= 4 and liste == []:
        if grille[x-1][y] == grille[x][y] == grille[x+1][y]:
            liste = [(x-1,y), (x,y), (x+1,y)]
            
    if x+2 <= 4  and liste == []:
        if grille[x][y] == grille[x+1][y] == grille[x+2][y]:
            liste = [(x,y), (x+1,y), (x+2,y)]

    if 0 <= y-2 and liste == []:
        if grille[x][y-2] == grille[x][y-1] == grille[x][y]:
            liste = [(x,y-2), (x,y-1), (x,y)]
            
    if y-1 >= 0 and y+1 <= 4 and liste == []:
        if grille[x][y-1] == grille[x][y] == grille[x][y+1]:
            liste = [(x,y-1), (x,y), (x,y+1)]
            
    if y+2 <= 4  and liste == []:
        if grille[x][y] == grille[x][y+1] == grille[x][y+2]:
            liste = [(x,y), (x,y+1), (x,y+2)]
    
    
    return liste


def test_fini(grille):
    ''' 
    Fonction qui teste au moins une combinaison  potentielle est présente dans la grille. Pour cela, elle échange sucessivement les positions des bonbons adjacents de la grille de toutes les manières possibles.
    Entrée : grille 
    sortie  : fini
    objectif : évaluer fini a true ou false 
    ''' 
    trouve = False
    # Horizontal
    y = 0
    while y < 5 and not trouve:
        x = 0 
        while x < 4 and not trouve :
            echange(grille, x, y, x+1 , y)
            if combinaison_presente(grille) != []:
                trouve = True 
            echange(grille, x, y, x+1 , y)
            x += 1
        y += 1 
    # Vertical 
    x = 0
    while x < 5 and not trouve:
        y = 0 
        while y < 4 and not trouve :
            echange(grille, x, y, x , y + 1)
            if combinaison_presente(grille) != []:
                trouve = True 
            echange(grille, x, y, x , y + 1)
            y += 1
        x += 1 
    if not trouve :
        fini = True
    return fini

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
        # Si la liste est pas vide
        if liste != []:

            if grille[liste[0][0]][liste[0][1]] == grille[liste[1][0]][liste[1][1]] and grille[liste[0][0]][liste[0][1]] == grille[liste[2][0]][liste[2][1]]:
                # VERIFIER QUE LA COMB EXISTE ENCORE, c’est une vérification de + au cas où il y a une erreur dans le raisonnement. 
                #pourra être enlevé si démontré que non
    
                # Si c’est une combinaison horizontale (les x des 3 2-uple sont les mêmes)
                if liste[0][0] == liste[1][0] and liste[0][0] == liste[2][0]:
            
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


# Fonction d’affichage de test
"""
def afficher_grille(grille):
    for line in grille:
        for char in line:
            print(char, end=" ")
        print()
    print()
"""

def afficher_grille(grille, nb_type_bonbons=4, latency=0.2):
    """
        Affiche la grille de jeu "grille" contenant au
        maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons-1, cmap='jet')
    plt.pause(latency)
    plt.draw()
    plt.pause(latency)


main()
