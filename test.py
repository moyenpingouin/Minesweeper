import pygame
import sys
def option_ecran():
    run_option = True
    while run_option:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Ajoutez ici d'autres événements spécifiques à la page des options

        # Ajoutez ici le code pour afficher les options sur l'écran
        # Remplissage de l'écran 
        ecran.fill(fond)
        ecran.blit(fondu, (0,0))
        # Récupérer les coordonnées de la souris
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Événement du bouton retour
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_jouer.collidepoint(event.pos):
                    run=True
                    run_option=False
                    break
                elif bouton_retour.collidepoint(event.pos):
                    run_option = False  # Sortir de la boucle des options
                    return  # Retourner à la boucle principale

        if bouton_retour.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran,orange, ((6,24,177,60)))
            pygame.draw.rect(ecran, rouge, bouton_retour)
        else:
            pygame.draw.rect(ecran, (50, 67, 60), ((6,24,177,60)))
            pygame.draw.rect(ecran, (116, 111, 110), bouton_retour)

        ecran.blit(retour,retour_rect)
        pygame.display.flip()

# Boucle principale
run=True
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
                run_option=True
                run=False
                option_ecran()
            elif bouton_quitter.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Remplissage de l'écran avec la couleur noire
    ecran.fill(fond)
    ecran.blit(fondu, (0,0))
    # Afficher les boutons
    pygame.draw.rect(ecran, (50, 67, 60), bouton_jouer)
    pygame.draw.rect(ecran, (50, 67, 60), bouton_option)
    pygame.draw.rect(ecran, (50, 67, 60), bouton_quitter)
    ecran.blit(jouer, jouer_rect)
    ecran.blit(option, option_rect)
    ecran.blit(quit, quit_rect)
    
    pygame.display.flip()
