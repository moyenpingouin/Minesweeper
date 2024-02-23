import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de l'écran
largeur, hauteur = 800, 600
taille_ecran = (largeur, hauteur)

# Création de l'écran
ecran = pygame.display.set_mode(taille_ecran)

# Chargement de l'image
image = pygame.image.load('démineur.png')  # Remplacez 'chemin_vers_votre_image.jpg' par le chemin de votre image
image = pygame.transform.scale(image, (largeur, hauteur))  # Redimensionner l'image pour qu'elle remplisse l'écran

# Création d'une surface transparente
surface_transparente = pygame.Surface((largeur, hauteur), pygame.SRCALPHA)
pygame.draw.rect(surface_transparente, (0, 0, 0, 200), (0, 0, largeur, hauteur))  # Rectangle semi-transparent noir

# Boucle principale
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    ecran.fill((0, 0, 0))

    # Superposer l'image avec la surface transparente
    ecran.blit(image, (0, 0))
    ecran.blit(surface_transparente, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    clock.tick(60)