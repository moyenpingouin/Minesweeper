#-------------------------PROJET DEMINEUR --------------------------------#
#banane
#import
import os
#import pygame
from random import randint
from classes import *
from fonctions import *
#Variables
jeu_revele=[]
jeu_cache=[]
    #difficulte=int(input("difficulté"))
difficulte=1

#initialisation

if difficulte==1:
    nb_mines=7
    longueur_x=8
    longueur_y=10
elif difficulte==2:
    nb_mines=40
    longueur_x=15
    longueur_y=20
elif difficulte==3:
    nb_mines=100
    longueur_y=26
    longueur_x=19



jeu_revele=initialiser(jeu_revele,longueur_y,longueur_x)
jeu_revele=remplir(jeu_revele,(0,0),nb_mines)
jeu_cache=mise_a_jour(jeu_revele)

for f in range(len(jeu_revele)):
        for h in range(len(jeu_revele[0])):
            if h == len(jeu_revele[0])-1:
                print(jeu_revele[f][h].nouvel_etat)
            else:
                print(jeu_revele[f][h].nouvel_etat, end=',')
