
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
rouge = (255, 0, 0)

# Chargement des images
drapeau = pygame.image.load('drapeau_start.png')  
bombe = pygame.image.load('bombe_start.png')

# Création de la police de caractères
police = pygame.font.SysFont(None, 48)
police_2 = pygame.font.SysFont(None,60)
police_3 = pygame.font.SysFont(None,20)
# Création du texte
minesweeper=police_2.render("Minesweeper", True, blanc)
Dev=police_3.render("DEV:Antoine KAYALI, Renan KAELBEL", True, blanc)
quitter=police.render("QUIT GAME",True,blanc)
jouer=police.render("PLAY",True,blanc)
option=police.render("OPTION",True,blanc)
texte_rect = minesweeper.get_rect(center=(largeur/2, (hauteur/2)-200))
DEV_rect = Dev.get_rect(center=(largeur/2, hauteur-50))
quitter_rect=quitter.get_rect(center=(largeur/2,(hauteur/2)+130))
jouer_rect=jouer.get_rect(center=(largeur/2,(hauteur/2)-55))
option_rect = option.get_rect(center=(largeur/2, (hauteur/2)+35))


# Création des boutons
bouton_jouer = pygame.Rect(288, 215, 225, 60)
bouton_option = pygame.Rect(288, 305, 225, 60)
bouton_quitter = pygame.Rect(288, 400, 225, 60)

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
            elif bouton_option.collidepoint(event.pos):
                # Code pour passer à l'écran des options
                pass
            elif bouton_quitter.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Remplissage de l'écran avec la couleur noire
    ecran.fill(fond)

    # Dessin sur le fond
    pygame.draw.rect(ecran, (50, 67, 60), ((288, 400, 230, 65)))
    pygame.draw.rect(ecran, (50, 67, 60), ((288, 305, 230, 65)))
    pygame.draw.rect(ecran, (50, 67, 60), ((288, 215, 230, 65)))
    pygame.draw.rect(ecran, (50, 67, 60) , (((largeur/2)-200, (hauteur/2)-240, (largeur/2)+5, 75)))
    pygame.draw.rect(ecran, (116, 111, 110), bouton_jouer)
    pygame.draw.rect(ecran, (116, 111, 110), bouton_option)
    pygame.draw.rect(ecran, (116, 111, 110), bouton_quitter)
    pygame.draw.rect(ecran, (50, 67, 60), (0, hauteur-50, largeur, 50))
    pygame.draw.rect(ecran, (116, 111, 110), (((largeur/2)-200, (hauteur/2)-240, (largeur/2), 70)))
    ecran.blit(minesweeper, texte_rect)
    ecran.blit(quitter,quitter_rect)
    ecran.blit(jouer,jouer_rect)
    ecran.blit(option,option_rect)
    ecran.blit(drapeau, ((largeur/2)-180,(hauteur/2)-225))
    ecran.blit(bombe, ((largeur/2)+125,(hauteur/2)-225))

    # Rafraîchissement de l'écran
    pygame.display.flip()