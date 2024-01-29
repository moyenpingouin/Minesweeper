#-------------------------PROJET DEMINEUR --------------------------------#

#import
import os
import pygame

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

for i in range(longueur_x):
    liste=[]
    for j in range(longueur_y):
        liste.append('X')
print(jeu_cache)
#class



#code
