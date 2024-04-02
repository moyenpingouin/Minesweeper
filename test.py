import pygame
import sys

pygame.init()

# Initialisation de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Curseur Glissant")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Paramètres
param_value = 50  # Valeur initiale du paramètre
param_min = 0  # Valeur minimale du paramètre
param_max = 100  # Valeur maximale du paramètre

# Police
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 100 <= mouse_x <= 700 and 300 <= mouse_y <= 350:  # Zone du curseur
                    param_value = (mouse_x - 100) / 6  # Mettre à jour la valeur du paramètre en fonction de la position du curseur

    # Affichage
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (100, 300, 600, 50), 2)  # Barre du curseur
    pygame.draw.rect(screen, BLUE, (100 + param_value * 6, 300, 2, 50))  # Curseur
    value_text = font.render("Valeur du paramètre : " + str(int(param_value)), True, BLACK)
    screen.blit(value_text, (250, 400))
    pygame.display.flip()

pygame.quit()
sys.exit()