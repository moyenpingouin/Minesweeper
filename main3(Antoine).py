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
    c=case()
    for j in range(longueur_x):
        liste.append(c)
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
                b=bombe()
                L[y]=b
                nombre_mine+=1
                nombre_mine_tot+=1
        H[i]=L
    if nombre_mine_tot!=mines:
        for i in range(mines-nombre_mine_tot):
            x=randint(0,l-1)
            y=randint(0,h-1)
            if(i,y)!=(Y,X):
                H[y][x]=bombe()
                nombre_mine_tot+=1

    return H,nombre_mine_tot

jeu_revele=remplir(jeu_revele,(2,1),30)[0]
for i in range(len(jeu_revele)):
    for j in range(len(jeu_revele[0])):
        if j == len(jeu_revele[0])-1:
            print(jeu_revele[i][j])
        else:
            print(jeu_revele[i][j], end=',')

def voisins(coordonnees:tuple(),tableau):
    """fonction qui donne les coordonnées des voisins"""
    x=coordonnees[0]
    y=coordonnees[1]
    hauteur=len(tableau)
    longueur=len(tableau[0])
    assert 0<=coordonnees[0]<hauteur+1 and 0<=coordonnees[1]<longueur
    liste=[]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            liste.append((i,j))
    liste2=list(liste)
    #supprime les coordonnées hors du tableau + point en question
    for i in liste:
        if i[0]<0 or i[1]<0 or (i[0]==x and i[1]==y) or (i[0]>hauteur-1 or i[1]>longueur-1):
            liste2.remove(i)
    return liste2
print(voisins((0,0),[[1,2,3,4],[1,2,3,4],[1,2,3,4]]))

def mis_a_jour_etat(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            nb=0
            for vois in voisins((i,j),tableau):
                if tableau[vois[0]][vois[1]].est_bombe():
                    nb+=1
            tableau[i][j].etat=str(nb)
    return tableau

print(mis_a_jour_etat(jeu_revele))