import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
ROUGE = (255, 0, 0)
police = pygame.font.SysFont(None, 48)
retour=police.render("RETOUR",True,BLANC)
Help=police.render("HELP",True,BLANC)
retour_rect = retour.get_rect(center=(90,50))
Help_rect = Help.get_rect(center=(142,325))
bouton_retour = pygame.Rect(6,24,172,55)
bouton_help = pygame.Rect(90,295,120,60)

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
    # Ajoutez ici le code pour afficher les options sur l'écran

    # Remplissage de l'écran 
    ecran.fill(BLANC)
    # Récupérer les coordonnées de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #evenement de option 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_retour.collidepoint(event.pos):
                run=True
                run_option=False
            elif bouton_help.collidepoint(event.pos):
                webbrowser.open('file:///C:/Users/Renan/Documents/GitHub/Minesweeper/page_web.html')

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
    pygame.draw.rect(ecran,(50, 67, 60 ), (95, 125, 620, 50), 10)  # Barre du curseur
    pygame.draw.rect(ecran,(116, 111, 110), (100, 120, 620, 50), 10)  # Barre du curseur
    pygame.draw.rect(ecran, (80, 80, 80), (100, 120,param_value * 6,50))  # Curseur
    pygame.draw.rect(ecran, (34, 34, 37), (100 + param_value * 6, 120, 10,50))  # Curseur
    pygame.draw.rect(ecran, (50, 67, 60 ), (90,190,155,75))
    pygame.draw.rect(ecran, (116, 111, 110), (90,190,150,70))
    pygame.draw.rect(ecran,(116, 111, 110),(300,200,480,380))
    pygame.draw.rect(ecran,(50, 67, 60 ),(300,200,480,380),10)
    value_text = police.render("Son: " + str(int(param_value)), True, (255,255,255))
    ecran.blit(value_text, (100, 210))
    ecran.blit(Help,Help_rect)
    ecran.blit(retour,retour_rect)

    # Dessiner la barre de réglage
    pygame.draw.rect(ecran, GRIS, (100, 120, 620, 50), 10)  # Barre du curseur
    pygame.draw.rect(ecran, NOIR, (100, 120, int(param_value * 620), 50))  # Curseur

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
