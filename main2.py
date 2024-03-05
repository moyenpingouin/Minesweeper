from random import randint
from classes import *
from fonctions import *
from intialisation import *

a=0
deminer((cordonnees_dep),jeu_cache)
affiche(jeu_cache)


while a==0:
    coordonnées=input("coordonnées")
    coordonnées=coordonnées.split()
    coordonnées=tuple(int(element) for element in coordonnées)
    if deminer((coordonnées),jeu_cache)=='GAME OVER':
        break
    else:
        print('-------------------------')
        deminer((coordonnées),jeu_cache)
        affiche(jeu_cache)
        if tableau_rgt.test_revele():
            a=1


#if a==1: BRAVO
#if a==2: Game over

            
