import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Résolution de référence
reference_resolution = (800, 600)

# Définition de la taille de l'écran
largeur, hauteur = pygame.display.Info().current_w, pygame.display.Info().current_h
taille_ecran = (largeur, hauteur)

# Calcul des ratios pour adapter les dimensions et positions
ratio_largeur = largeur / reference_resolution[0]
ratio_hauteur = hauteur / reference_resolution[1]

# Définition de la couleur
fond = (183, 173, 171)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
orange = (122, 41, 14)

# Ajout d'un titre à la fenêtre
pygame.display.set_caption('Minesweeper')

# Création de l'écran
ecran = pygame.display.set_mode(taille_ecran, pygame.FULLSCREEN)

# Chargement des images
drapeau = pygame.image.load('images/drapeau_start.png')
bombe = pygame.image.load('images/bombe_start.png')
fond_image = pygame.image.load('images/fond_start.png')
fondu = pygame.transform.scale(fond_image, taille_ecran)
fondu.set_alpha(140)

# Création de la police de caractères
police = pygame.font.SysFont(None, int(48 * ratio_largeur))
police_2 = pygame.font.SysFont(None, int(60 * ratio_largeur))
police_3 = pygame.font.SysFont(None, int(20 * ratio_largeur))

# Calcul des nouvelles tailles et positions en fonction des ratios
taille_texte = int(48 * ratio_largeur)
taille_texte_2 = int(60 * ratio_largeur)
taille_texte_3 = int(20 * ratio_largeur)

# Création du texte
# texte
minesweeper = police_2.render("Minesweeper", True, blanc)
Dev = police_3.render("Devs : Antoine KAYALI, Renan KAELBEL", True, blanc)
quitter = police.render("QUIT GAME", True, blanc)
jouer = police.render("PLAY", True, blanc)
option = police.render("OPTION", True, blanc)
retour = police.render("RETOUR", True, blanc)

# Calcul des nouvelles tailles et positions en fonction des ratios
texte_rect = minesweeper.get_rect(center=(largeur / 2, hauteur / 2 - 200 * ratio_hauteur))
DEV_rect = Dev.get_rect(center=(largeur / 2 + 260 * ratio_largeur, hauteur - 25 * ratio_hauteur))
quitter_rect = quitter.get_rect(center=(largeur / 2, hauteur / 2 + 130 * ratio_hauteur))
jouer_rect = jouer.get_rect(center=(largeur / 2, hauteur / 2 - 55 * ratio_hauteur))
option_rect = option.get_rect(center=(largeur / 2, hauteur / 2 + 35 * ratio_hauteur))
retour_rect = retour.get_rect(center=(90 * ratio_largeur, 50 * ratio_hauteur))

# Paramètres
param_value = 50  # Valeur initiale du paramètre
param_min = 0  # Valeur minimale du paramètre
param_max = 100  # Valeur maximale du paramètre

# Création des boutons
bouton_jouer = pygame.Rect(int(288 * ratio_largeur), int(215 * ratio_hauteur), int(225 * ratio_largeur), int(60 * ratio_hauteur))
bouton_option = pygame.Rect(int(288 * ratio_largeur), int(305 * ratio_hauteur), int(225 * ratio_largeur), int(60 * ratio_hauteur))
bouton_quitter = pygame.Rect(int(288 * ratio_largeur), int(400 * ratio_hauteur), int(225 * ratio_largeur), int(60 * ratio_hauteur))
bouton_retour = pygame.Rect(int(6 * ratio_largeur), int(24 * ratio_hauteur), int(172 * ratio_largeur), int(55 * ratio_hauteur))

# Ajout des ombres sur les boutons
def dessiner_bouton_ombre(ecran, rect):
    shadow_rect = rect.copy()
    shadow_rect.move_ip(5, 5)
    pygame.draw.rect(ecran, (100, 100, 100), shadow_rect)

# Définition de la page option
run_global = True
run = True
while run_global:
    # Boucle principale
    while run:
        # Récupérer les coordonnées de la souris
        mouse_x, mouse_y = pygame.mouse.get_pos()

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
                    run_option = True
                    run = False
                elif bouton_quitter.collidepoint(event.pos):
                    run = False
                    run_global = False
                    pygame.quit()
                    sys.exit()

        # Remplissage de l'écran avec la couleur noire
        ecran.fill(fond)
        ecran.blit(fondu, (0, 0))

        # Dessiner les boutons avec ombre
        dessiner_bouton_ombre(ecran, bouton_jouer)
        dessiner_bouton_ombre(ecran, bouton_option)
        dessiner_bouton_ombre(ecran, bouton_quitter)

        # Vérifier si la souris est sur un bouton et changer sa couleur en rouge si c'est le cas
        if bouton_jouer.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran, orange, bouton_jouer)
        else:
            pygame.draw.rect(ecran, (116, 111, 110), bouton_jouer)

        if bouton_option.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran, orange, bouton_option)
        else:
            pygame.draw.rect(ecran, (116, 111, 110), bouton_option)

        if bouton_quitter.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran, orange, bouton_quitter)
        else:
            pygame.draw.rect(ecran, (116, 111, 110), bouton_quitter)

        # Dessin sur le fond
        pygame.draw.rect(ecran, (50, 67, 60), (((largeur / 2) - 200 * ratio_largeur, (hauteur / 2) - 240 * ratio_hauteur, (largeur / 2) + 5 * ratio_largeur, 75 * ratio_hauteur)))
        pygame.draw.rect(ecran, (50, 67, 60), (0, hauteur - 50 * ratio_hauteur, largeur, 50 * ratio_hauteur))
        pygame.draw.rect(ecran, (116, 111, 110), (((largeur / 2) - 200 * ratio_largeur, (hauteur / 2) - 240 * ratio_hauteur, (largeur / 2) * ratio_largeur, 70 * ratio_hauteur)))
        ecran.blit(minesweeper, texte_rect)
        ecran.blit(quitter, quitter_rect)
        ecran.blit(jouer, jouer_rect)
        ecran.blit(option, option_rect)
        ecran.blit(Dev, DEV_rect)
        ecran.blit(drapeau, ((largeur / 2) - 180 * ratio_largeur, (hauteur / 2) - 225 * ratio_hauteur))
        ecran.blit(bombe, ((largeur / 2) + 125 * ratio_largeur, (hauteur / 2) - 225 * ratio_hauteur))

        # Rafraîchissement de l'écran
        pygame.display.flip()

    while run_option:
        # Ajoutez ici le code pour afficher les options sur l'écran
        # Remplissage de l'écran
        ecran.fill(fond)
        ecran.blit(fondu, (0, 0))
        # Récupérer les coordonnées de la souris
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # evenement de option
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_retour.collidepoint(event.pos):
                    run = True
                    run_option = False
            if event.type == pygame.QUIT:
                run_option = False
                run_global = False
                pygame.quit()
                sys.exit()

        if bouton_retour.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran, orange, bouton_retour)
        else:
            pygame.draw.rect(ecran, (116, 111, 110), bouton_retour)

        pygame.draw.rect(ecran, (50, 67, 60), (int(95 * ratio_largeur), int(125 * ratio_hauteur), int(620 * ratio_largeur), int(50 * ratio_hauteur)), 10)  # Barre du curseur
        pygame.draw.rect(ecran, (116, 111, 110), (int(100 * ratio_largeur), int(120 * ratio_hauteur), int(620 * ratio_largeur), int(50 * ratio_hauteur)), 10)  # Barre du curseur
        pygame.draw.rect(ecran, (80, 80, 80), (int(100 * ratio_largeur), int(120 * ratio_hauteur), int(param_value * 6 * ratio_largeur), int(50 * ratio_hauteur)))  # Curseur
        pygame.draw.rect(ecran, (34, 34, 37), (int(100 * ratio_largeur + param_value * 6 * ratio_largeur), int(120 * ratio_hauteur), int(10 * ratio_largeur), int(50 * ratio_hauteur)))  # Curseur
        pygame.draw.rect(ecran, (50, 67, 60), (int(90 * ratio_largeur), int(190 * ratio_hauteur), int(155 * ratio_largeur), int(75 * ratio_hauteur)))
        pygame.draw.rect(ecran, (116, 111, 110), (int(90 * ratio_largeur), int(190 * ratio_hauteur), int(150 * ratio_largeur), int(70 * ratio_hauteur)))
        value_text = police.render("Son: " + str(int(param_value)), True, (255, 255, 255))
        ecran.blit(value_text, (int(100 * ratio_largeur), int(210 * ratio_hauteur)))
        ecran.blit(retour, retour_rect)
        pygame.display.flip()
