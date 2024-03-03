from random import randint
from classes import *
from fonctions import *
from main import *

print('-------------------------')
affiche(jeu_cache)
while True:
    coordonnées=input("coordonnées")
    coordonnées=coordonnées.split()
    coordonnées=tuple(int(element) for element in coordonnées)
    if deminer((coordonnées),jeu_cache)=='GAME OVER':
        break
    else:
        print('-------------------------')
        deminer((coordonnées),jeu_cache)
        affiche(jeu_cache)

