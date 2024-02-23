import pygame
pygame.init()

# Définir les couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Définir la taille de la fenêtre
WIDTH, HEIGHT = 400, 300
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouton qui change de couleur")

# Définir le texte du bouton
font = pygame.font.SysFont(None, 30)
text = font.render("Cliquez ici", True, WHITE)

# Définir le rectangle du bouton
button = pygame.Rect(150, 100, 100, 50)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Récupérer les coordonnées de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Vérifier si la souris est sur le bouton
    if button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(win, GREEN, button)
    else:
        pygame.draw.rect(win, RED, button)

    # Afficher le texte sur le bouton
    win.blit(text, (165, 110))

    pygame.display.update()

pygame.quit()