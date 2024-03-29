from random import randint
import matplotlib.pyplot as plt


def main():
    # On crée la grille
    grille = creation_grille(3)
    # On affiche la grille
    afficher_grille(grille)

    fin = jeu_fini(grille)
    while not fin:
        # On demande les coordonnees des deux cellules a echanger
        x1, y1, x2, y2 = map(int, input("Coordonnées : ").split())
        print()

        echange(grille, x1, y1, x2, y2)
        afficher_grille(grille)
        
        combi1, combi2 = dcb(grille, x1, y1), dcb(grille, x2, y2)
        if combi1 == [] and combi2 == []:
            echange(grille, x1, y1, x2, y2)
            afficher_grille(grille)
        else:
            # Modifie la grille pour enlever les combinaisons (une ou deux selon le cas)
            if combi1 != []:
                supprime_comb(grille, combi1)
            if combi2 != []:
                supprime_comb(grille, combi2)
            afficher_grille(grille)

            boucle_suppression(grille)
            fin = jeu_fini(grille)
    print("Game over...")


def boucle_suppression(grille, afficher=True):
    # On recherche une combinaison
    c = combinaison_presente(grille)
    # Tant qu’il reste des combinaisons
    while c != []:
        supprime_comb(grille, c)
        if afficher:
            afficher_grille(grille)

        c = combinaison_presente(grille)


def jeu_fini(grille):
    ''' 
    Fonction qui teste au moins une combinaison  potentielle est présente dans la grille. Pour cela, elle échange sucessivement les positions des bonbons adjacents de la grille de toutes les manières possibles.
    Entrée : grille 
    sortie  : fini
    objectif : évaluer fini a true ou false 
    ''' 
    taille, trouve = len(grille), False
    # Horizontal
    y = 0
    while y < taille and not trouve:
        x = 0 
        while x < taille-1 and not trouve :
            echange(grille, x, y, x+1 , y)
            if combinaison_presente(grille) != []:
                trouve = True 
            echange(grille, x, y, x+1 , y)
            x += 1
        y += 1 
    # Vertical 
    x = 0
    while x < taille and not trouve:
        y = 0 
        while y < taille-1 and not trouve :
            echange(grille, x, y, x , y + 1)
            if combinaison_presente(grille) != []:
                trouve = True 
            echange(grille, x, y, x , y + 1)
            y += 1
        x += 1
    
    return not trouve


def combinaison_presente(grille):
    """
        Fonction qui renvoie une liste contenant les 3 2-uple de coordonnées de la première combinaison
        rencontrée (en partant de (0, 0)), ou une liste vide s’il n’y a pas de combinaison présente.
        Entrée : grille -> 2D list
        Sortie : list, la liste de coordonées des cellules formant la combinaison
    """ 
    taille, trouve = len(grille), False
    x, y = 0, 0
    while not trouve and x < taille:
        while not trouve and y < taille:
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
    
    # La condition suivante est peut être inutile, j’ai la flemme de vérifier, pour être franchement honnête.
    if grille[liste[0][0]][liste[0][1]] == grille[liste[1][0]][liste[1][1]] and grille[liste[0][0]][liste[0][1]] == grille[liste[2][0]][liste[2][1]]:

        # On met la couleur blanche et affiche
        grille[liste[0][0]][liste[0][1]], grille[liste[1][0]][liste[1][1]], grille[liste[2][0]][liste[2][1]] = 4, 4, 4
        afficher_grille(grille)
        
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
                for i in range(x, 0, -1):
                    grille[i][y] = grille[i-1][y]

                grille[0][y] = randint(0, 3)


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
    taille = len(grille)
    
    # Cas verticaux
    if 0 <= x-2 and grille[x-2][y] == grille[x-1][y] == grille[x][y]:
        liste = [(x,y), (x-1,y), (x-2,y)]
            
    elif (x-1 >= 0 and x+1 < taille) and grille[x-1][y] == grille[x][y] == grille[x+1][y]:
        liste = [(x+1,y), (x,y), (x-1,y)]
            
    elif x+2 < taille and grille[x][y] == grille[x+1][y] == grille[x+2][y]:
        liste = [(x+2,y), (x+1,y), (x,y)]
    
    # Cas horizontaux
    elif 0 <= y-2 and grille[x][y-2] == grille[x][y-1] == grille[x][y]:
        liste = [(x,y-2), (x,y-1), (x,y)]
            
    elif (y-1 >= 0 and y+1 < taille) and grille[x][y-1] == grille[x][y] == grille[x][y+1]:
        liste = [(x,y-1), (x,y), (x,y+1)]
            
    elif y+2 < taille and grille[x][y] == grille[x][y+1] == grille[x][y+2]:
        liste = [(x,y), (x,y+1), (x,y+2)]
    
    
    return liste


def echange(grille, x1, y1, x2, y2):
    grille[x1][y1], grille[x2][y2] = grille[x2][y2], grille[x1][y1]


def creation_grille(taille):
    grille = [[randint(0,3) for _ in range(taille)] for _ in range(taille)]
    boucle_suppression(grille)
    
    return grille
    

def afficher_grille(grille, latency=0.05):
    """
        Affiche la grille de jeu "grille" contenant au
        maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=4, cmap='terrain')
    plt.pause(latency)
    plt.draw()
    plt.pause(latency)


main()
