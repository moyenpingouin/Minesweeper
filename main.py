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
jeu_revele=mise_a_jour(jeu_revele)
deminer((0,0),jeu_revele)
affiche(jeu_revele)