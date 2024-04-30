
import fonctions
from intialisation import *
import classes
import pygame
import PIL
import sys
from start import *

#boucle globale
def global_run():
    pygame.init()
    #initialisation
    print("aaa")
    # Définir la taille de la fenêtre
    largeur, hauteur = 800, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))
    
    # Définir la position initiale de l'image de fond
    fond_x = 0
    fond_y = 0
    #------------------------------------------------------------------------------#
    #Selection Difficulté
    run_diff=True
    while run_diff:
        ecran.fill(fond)
        ecran.blit(fondu, (0,0))
        pygame.display.flip()
    #Run Global
    initialisation_(1)
    tableau_jeu=initialisation_(1)[2]
    fond = pygame.image.load(tableau_jeu.image)  
    fond = pygame.transform.scale(fond, (largeur, hauteur))
    run_glbl=True
    while run_glbl:
        fenetre.blit(fond, (0, 0))




        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()