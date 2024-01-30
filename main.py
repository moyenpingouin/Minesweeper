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

for i in range(longueur_x):
    liste=[]
    for j in range(longueur_y):
        liste.append('X')
print(jeu_cache)
print(fonction())

#class



#code
def remplir(l:int,h:int,X:int,Y:int,max_mine:int):
    """l:longeur du tableau
    h:hauteur du tableau
    X,Y: coordonnees du point d'initialisation
    OUT:liste de liste de int """
    H=[0 for i in range(h)]
    max_mine_ligne=max_mine/h
    print(max_mine_ligne)
    nombre_mine_tot=0
    for i in range(h):
        L=[0 for _ in range(l)]
        nombre_mine=0
        for y in range(l):
          x=randint(0,6)
          if x==2 :
             if(i,y)!=(Y,X) and nombre_mine < max_mine_ligne and nombre_mine_tot<max_mine:
                L[y]='B'
                nombre_mine+=1
                nombre_mine_tot+=1
        H[i]=L
    H[Y][X]="A"
    return H,nombre_mine_tot
print(remplir(8,10,2,1,7))