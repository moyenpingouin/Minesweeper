from random import randint
from classes import *
from fonctions import *
from intialisation import *
import pygame

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
        b= verif(jeu_cache)
        if b==True:
            a=1
        if b=='GAME OVER':
            a=2
if a ==1:
    print('gagné')
if a==2:
    print('perdu')
affiche_rev(jeu_cache)


#if a==1: BRAVO
#if a==2: Game over

            
