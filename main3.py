#imports
import fonctions
from intialisation import *
import classes
import pygame
import PIL
import sys

#initialisation
pygame.init()
print(type(tableau_jeu.image))
# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
fond = pygame.image.load(tableau_jeu.imageq)  # Remplacez "votre_image.jpg" par le chemin de votre image de fond
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Définir la position initiale de l'image de fond
fond_x = 0
fond_y = 0


#boucle globale
run_glbl=True
while run_glbl:





    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()