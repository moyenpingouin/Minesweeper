
import pygame
import sys
import webbrowser
# Initialisation de Pygame
pygame.init()

# Définition de la taille de l'écran
largeur, hauteur = 800, 600
taille_ecran = (largeur, hauteur)

# Définition de la couleur
fond = (183, 173, 171)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
orange = (122, 41, 14)

# Ajout d'un titre à la fenêtre
pygame.display.set_caption('Minesweeper')

# Création de l'écran
ecran = pygame.display.set_mode(taille_ecran)

# Chargement des images
drapeau = pygame.image.load('images/drapeau_start.png')  
bombe = pygame.image.load('images/bombe_start.png')
fond_image = pygame.image.load('images/fond_start.png') 
fondu = pygame.transform.scale(fond_image,(taille_ecran))
fondu.set_alpha(140)

# Création de la police de caractères
police = pygame.font.SysFont(None, 48)
police_2 = pygame.font.SysFont(None,60)
police_3 = pygame.font.SysFont(None,20)

# Création du texte
#texte
minesweeper=police_2.render("Minesweeper", True, blanc)
Dev=police_3.render("Devs : Antoine KAYALI, Renan KAELBEL", True, blanc)
quitter=police.render("QUIT GAME",True,blanc)
jouer=police.render("PLAY",True,blanc)
option=police.render("OPTION",True,blanc)
retour=police.render("RETOUR",True,blanc)
Help=police.render("HELP",True,blanc)
#rect
texte_rect = minesweeper.get_rect(center=(largeur/2, (hauteur/2)-200))
DEV_rect = Dev.get_rect(center=((largeur/2)+260, hauteur-25))
quitter_rect=quitter.get_rect(center=(largeur/2,(hauteur/2)+130))
jouer_rect=jouer.get_rect(center=(largeur/2,(hauteur/2)-55))
option_rect = option.get_rect(center=(largeur/2, (hauteur/2)+35))
retour_rect = retour.get_rect(center=(90,50))
Help_rect = Help.get_rect(center=(142,325))

# Paramètres
param_value = 50  # Valeur initiale du paramètre
param_min = 0  # Valeur minimale du paramètre
param_max = 100  # Valeur maximale du paramètre

# Création des boutons
bouton_jouer = pygame.Rect(288, 215, 225, 60)
bouton_option = pygame.Rect(288, 305, 225, 60)
bouton_quitter = pygame.Rect(288, 400, 225, 60)
bouton_retour = pygame.Rect(6,24,172,55)
bouton_help = pygame.Rect(90,295,120,60)

#Définition de la page option 
run_global=True
run=True
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
                    run_option=True
                    run=False
                elif bouton_quitter.collidepoint(event.pos):
                    run=False
                    run_global=False
                    pygame.quit()
                    sys.exit()

        # Remplissage de l'écran avec la couleur noire
        ecran.fill(fond)
        ecran.blit(fondu, (0,0))
        

        # Vérifier si la souris est sur un bouton et changer sa couleur en rouge si c'est le cas
        if bouton_jouer.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran,orange, ((288, 215, 230, 65)))
            pygame.draw.rect(ecran, rouge, bouton_jouer)
        else:
            pygame.draw.rect(ecran, (50, 67, 60), ((288, 215, 230, 65)))
            pygame.draw.rect(ecran, (116, 111, 110), bouton_jouer)
        
        if bouton_option.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran, orange, ((288, 305, 230, 65)))
            pygame.draw.rect(ecran, rouge, bouton_option)
        else:
            pygame.draw.rect(ecran, (50, 67, 60), ((288, 305, 230, 65)))
            pygame.draw.rect(ecran, (116, 111, 110), bouton_option)

        if bouton_quitter.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran, orange, ((288, 400, 230, 65)))
            pygame.draw.rect(ecran, rouge, bouton_quitter)
        else:
            pygame.draw.rect(ecran, (50, 67, 60 ), ((288, 400, 230, 65)))
            pygame.draw.rect(ecran, (116, 111, 110), bouton_quitter)
        # Dessin sur le fond
        pygame.draw.rect(ecran, (50, 67, 60) , (((largeur/2)-200, (hauteur/2)-240, (largeur/2)+5, 75)))
        pygame.draw.rect(ecran, (50, 67, 60), (0, hauteur-50, largeur, 50))
        pygame.draw.rect(ecran, (116, 111, 110), (((largeur/2)-200, (hauteur/2)-240, (largeur/2), 70)))
        ecran.blit(minesweeper, texte_rect)
        ecran.blit(quitter,quitter_rect)
        ecran.blit(jouer,jouer_rect)
        ecran.blit(option,option_rect)
        ecran.blit(Dev,DEV_rect)
        ecran.blit(drapeau, ((largeur/2)-180,(hauteur/2)-225))
        ecran.blit(bombe, ((largeur/2)+125,(hauteur/2)-225))

        # Rafraîchissement de l'écran
        pygame.display.flip()
    
    while run_option:
        # Ajoutez ici le code pour afficher les options sur l'écran
        # Remplissage de l'écran 
        ecran.fill(fond)
        ecran.blit(fondu, (0,0))
        # Récupérer les coordonnées de la souris
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #evenement de option 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_retour.collidepoint(event.pos):
                    run=True
                    run_option=False
                elif bouton_help.collidepoint(event.pos):
                    webbrowser.open('Minesweeper/page_web.html')
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 100 <= mouse_x <= 700 and 120 <= mouse_y <= 170:  # Zone du curseur
                        param_value = (mouse_x - 100) / 6  
            if event.type == pygame.QUIT:
                run_option=False
                run_global=False
                pygame.quit()
                sys.exit()
        
        if bouton_retour.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran,orange, ((6,24,177,60)))
            pygame.draw.rect(ecran, rouge, bouton_retour)
        else:
            pygame.draw.rect(ecran, (50, 67, 60), ((6,24,177,60)))
            pygame.draw.rect(ecran, (116, 111, 110), bouton_retour)

        if bouton_help.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(ecran, orange, (90,295,125,65))
            pygame.draw.rect(ecran, rouge, bouton_help)
        else:
            pygame.draw.rect(ecran, (50, 67, 60 ), (90,295,125,65))
            pygame.draw.rect(ecran, (116, 111, 110), bouton_help)

        pygame.draw.rect(ecran,(50, 67, 60 ), (95, 125, 620, 50), 10)  # Barre du curseur
        pygame.draw.rect(ecran,(116, 111, 110), (100, 120, 620, 50), 10)  # Barre du curseur
        pygame.draw.rect(ecran, (80, 80, 80), (100, 120,param_value * 6,50))  # Curseur
        pygame.draw.rect(ecran, (34, 34, 37), (100 + param_value * 6, 120, 10,50))  # Curseur
        pygame.draw.rect(ecran, (50, 67, 60 ), (90,190,155,75))
        pygame.draw.rect(ecran, (116, 111, 110), (90,190,150,70))
        value_text = police.render("Son: " + str(int(param_value)), True, (255,255,255))
        ecran.blit(value_text, (100, 210))
        ecran.blit(Help,Help_rect)
        ecran.blit(retour,retour_rect)
        pygame.display.flip()