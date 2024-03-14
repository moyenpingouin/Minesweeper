
import fonctions
from intialisation import *
import classes
import pygame
import PIL
import sys

#boucle globale
def global_run():
    #imports

    #initialisation
    pygame.init()
    # Définir la taille de la fenêtre
    largeur, hauteur = 800, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))
    fond = pygame.image.load(tableau_jeu.image)  
    fond = pygame.transform.scale(fond, (largeur, hauteur))
    # Définir la position initiale de l'image de fond
    fond_x = 0
    fond_y = 0
    run_glbl=True
    while run_glbl:
        fenetre.blit(fond, (0, 0))




        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()