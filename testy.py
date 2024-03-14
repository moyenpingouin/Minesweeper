import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Exemple de jeu Pygame")

# Position initiale du carré
square_x = WINDOW_WIDTH // 2
square_y = WINDOW_HEIGHT // 2
square_size = 50

# Vitesse de déplacement
speed = 5

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des mouvements du carré
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed

    # Limite les coordonnées du carré à l'intérieur de la fenêtre
    square_x = max(0, min(square_x, WINDOW_WIDTH - square_size))
    square_y = max(0, min(square_y, WINDOW_HEIGHT - square_size))

    # Efface l'écran
    window.fill(WHITE)

    # Dessine le carré
    pygame.draw.rect(window, BLACK, (square_x, square_y, square_size, square_size))

    # Met à jour l'affichage
    pygame.display.update()

    # Limite le taux de rafraîchissement de la boucle
    pygame.time.Clock().tick(30)

# Quitte Pygame
pygame.quit()
sys.exit()
