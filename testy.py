import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
ROUGE = (255, 0, 0)

# Définir les dimensions de la fenêtre
largeur = 800
hauteur = 600

# Créer la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Barre de réglage")

# Définir les variables
param_value = 0.5
en_train_de_glisser = False

# Boucle principale du jeu
run_option = True
while run_option:
    # Récupérer les coordonnées de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_option = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if 100 <= mouse_x <= 720 and 120 <= mouse_y <= 170:  # Zone du curseur
                    en_train_de_glisser = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Bouton gauche de la souris
                en_train_de_glisser = False

    # Si en train de glisser, mettre à jour la valeur du paramètre en fonction de la position du curseur
    if en_train_de_glisser:
        mouse_x = max(100, min(720, mouse_x))  # Limiter le curseur à l'intérieur de la barre
        param_value = (mouse_x - 100) / 620  # Calculer la valeur du paramètre

    # Effacer l'écran
    ecran.fill(BLANC)

    # Dessiner la barre de réglage
    pygame.draw.rect(ecran, GRIS, (100, 120, 620, 50), 10)  # Barre du curseur
    pygame.draw.rect(ecran, NOIR, (100, 120, int(param_value * 620), 50))  # Curseur

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
