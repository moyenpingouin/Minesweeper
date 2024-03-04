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
    nb_mines=2
    longueur_x=3
    longueur_y=3
elif difficulte==2:
    nb_mines=40
    longueur_x=15
    longueur_y=20
elif difficulte==3:
    nb_mines=100
    longueur_y=26
    longueur_x=19


def initialiser_jeu():
    jeu_revele=[]
    jeu_cache=[]
    cordonnees_dep=input("coordonnées départ")
    cordonnees_dep=cordonnees_dep.split()
    cordonnees_dep=tuple(int(element) for element in cordonnees_dep)
    jeu_revele=initialiser(jeu_revele,longueur_y,longueur_x)
    jeu_revele=remplir(jeu_revele,cordonnees_dep,nb_mines)
    jeu_cache=mise_a_jour(jeu_revele)
    tableau_jeu=tableau(jeu_cache)


    for f in range(len(jeu_revele)):
            for h in range(len(jeu_revele[0])):
                if h == len(jeu_revele[0])-1:
                    print(jeu_revele[f][h].nouvel_etat)
                else:
                    print(jeu_revele[f][h].nouvel_etat, end=',')
