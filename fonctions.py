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
    nb_mines=2
    longueur_x=10
    longueur_y=8
elif difficulte==2:
    nb_mines=40
    longueur_x=15
    longueur_y=20
elif difficulte==3:
    nb_mines=100
    longueur_y=26
    longueur_x=19

def affiche(tableau):
    """fonction bête d'affichage"""
    for f in range(len(tableau)):
        for h in range(len(tableau[0])):
            if h == len(tableau[0])-1:
                print(tableau[f][h])
            else:
                print(tableau[f][h], end=',')



################################################################


def initialiser(tableau,y,x):
    for i in range(y):
        liste=[]
        for j in range(x):
            c=case()
            liste.append(c)
        tableau.append(liste)
    return tableau

#code
def remplir(tableau,coordonneesdep,mines:int):
    """l:longeur du tableau
    h:hauteur du tableau
    X,Y: coordonnees du point d'initialisation
    mines:le nombre total de mine sur la grille
    OUT:liste de liste de int """
    l=len(tableau[0])
    h=len(tableau)
    nombre_mine=mines
    liste=[]
    liste.append(coordonneesdep)
    while nombre_mine>0:
        x=randint(0,l-1)
        y=randint(0,h-1)
        if (x,y) in liste:
            continue
        else:
            tableau[y][x]=bombe()
            liste.append((x,y))
            nombre_mine-=1
    return tableau




################# 


def voisins(coordonnees: tuple, tableau):
    """fonction qui donne les coordonnées des voisins"""
    x = coordonnees[0]
    y = coordonnees[1]
    hauteur = len(tableau)
    longueur = len(tableau[0])
    liste = []

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # Vérifier les coordonnées dans les limites du tableau
            if 0 <= i < hauteur and 0 <= j < longueur:
                # Ne pas inclure le point lui-même
                if not (i == x and j == y):
                    liste.append((i, j))

    return liste
############################################################
def mise_a_jour(tableau:list):
    '''met les numéros sur les cases'''
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j].est_bombe():
                continue
            nb = 0
            for vois in voisins((i, j), tableau):
                if tableau[vois[0]][vois[1]].est_bombe():
                    nb += 1
            tableau[i][j].nouvel_etat = str(nb)
    return tableau


def deminer(kase: tuple, tableau: list):
    '''affiche la case et toutes celles qu'il peut autour'''
    i = kase[0]
    j = kase[1]

    # Si la case n'est pas révélée et son nouvel état est '0', révèle la case et explore les voisins
    if not tableau[i][j].est_revelee and tableau[i][j].nouvel_etat == '0':
        tableau[i][j].est_revelee = True
        for vois in voisins((i, j), tableau):
            if not tableau[vois[0]][vois[1]].est_revelee:
                deminer(vois, tableau)

    # Si la case est révélée et ne contient pas de bombe, révèle la case
    elif not tableau[i][j].est_revelee and not tableau[i][j].est_bombe():
        tableau[i][j].est_revelee = True

    # Si la case est révélée et contient une bombe, retourne 'GAME OVER'
    elif not tableau[i][j].est_revelee and tableau[i][j].est_bombe():
        return 'GAME OVER'

