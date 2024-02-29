#-------------------------PROJET DEMINEUR --------------------------------#

#import
import os
#import pygame
from random import randint
from classes import *
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

for i in range(longueur_y):
    liste=[]
    for j in range(longueur_x):
        liste.append('X')
    jeu_cache.append(liste)

for i in range(longueur_y):
    liste=[]
    for j in range(longueur_x):
        liste.append(0)
    jeu_revele.append(liste)
#class



#code
def remplir(tableau,coordonnees,mines:int):
    """l:longeur du tableau
    h:hauteur du tableau
    X,Y: coordonnees du point d'initialisation
    mines:le nombre total de mine sur la grille
    OUT:liste de liste de int """
    h,l=len(tableau),len(tableau[0])
    X,Y=coordonnees[0],coordonnees[1]
    H=[0 for i in range(h)]
    max_mine_ligne=mines/h
    nombre_mine_tot=0
    for i in range(h):
        L=[0 for _ in range(l)]
        nombre_mine=0
        for y in range(l):
          x=randint(0,6)
          if x==2:
             if(i,y)!=(Y,X) and nombre_mine < max_mine_ligne and nombre_mine_tot<mines:
                bombe=case(True,(i,y),tableau)
                L[y]=bombe
                nombre_mine+=1
                nombre_mine_tot+=1
        H[i]=L
    if nombre_mine_tot!=mines:
        for i in range(mines-nombre_mine_tot):
            x=randint(0,l-1)
            y=randint(0,h-1)
            if(i,y)!=(Y,X):
                H[y][x]=case(True,(i,y),tableau)
                nombre_mine_tot+=1

    H[Y][X]="A"
    return H,nombre_mine_tot

jeu_revele=remplir(jeu_revele,(2,1),30)[0]
for i in range(len(jeu_revele)):
    for j in range(len(jeu_revele[0])):
        if j == len(jeu_revele[0])-1:
            print(jeu_revele[i][j])
        else:
            print(jeu_revele[i][j], end=',')

for i in jeu_revele:
    for a in i:
        if type(a)==case:
            print(a.coordonnees, a.voisins)
