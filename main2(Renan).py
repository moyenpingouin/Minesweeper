import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de l'écran
largeur, hauteur = 800, 600
taille_ecran = (largeur, hauteur)

# Ajout d'un titre à la fenêtre
pygame.display.set_caption('Minesweeper')

# Création de l'écran
ecran = pygame.display.set_mode(taille_ecran)

# Définition de la couleur noire
fond = (183, 173, 171)
blanc = (255, 255, 255)

# Création de la police de caractères
police = pygame.font.SysFont(None, 48)
police_2 = pygame.font.SysFont(None,60)
# Création du texte
minesweeper=police_2.render("Minesweeper", True, blanc)
quitter=police.render("QUIT GAME",True,blanc)
jouer=police.render("PLAY",True,blanc)
texte_rect = minesweeper.get_rect(center=(largeur/2, (hauteur/2)-200))
quitter_rect=quitter.get_rect(center=(largeur/2,(hauteur/2)+100))
jouer_rect=jouer.get_rect(center=(largeur/2,(hauteur/2)-25))
# Création des boutons
bouton_jouer = pygame.Rect(288, 245, 225, 60)
bouton_quitter = pygame.Rect(288, 370, 225, 60)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_jouer.collidepoint(event.pos):
                # Code pour passer à l'écran de jeu
                pass
            elif bouton_quitter.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Remplissage de l'écran avec la couleur noire
    ecran.fill(fond)

    # Dessin des boutons
    pygame.draw.rect(ecran, (116, 111, 110), bouton_jouer)
    pygame.draw.rect(ecran, (116, 111, 110), bouton_quitter)
    ecran.blit(minesweeper, texte_rect)
    ecran.blit(quitter,quitter_rect)
    ecran.blit(jouer,jouer_rect)
    # Rafraîchissement de l'écran
    pygame.display.flip()