import pygame
import math
from game import Game
pygame.init()


#definir une clock
clock = pygame.time.Clock()
FPS = 120

# Generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1000, 720))

#Importer charger l'arriere plan
background = pygame.image.load('assets/bg.jpg')

#importer charger notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer/charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#Charger notre jeu
game = Game()

running = True

#Boucle tant que cette condition est vraie
while running:

    #Aplliquer la fenetre du jeu
    screen.blit(background, (0, -200))

    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)

    #Verifier si notre jeu n'a pas commencé
    else:
        #ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #Mettre a jour l'ecran
    pygame.display.flip()

    #Si le joueur ferme cette fenertre
    for event in pygame.event.get():
        #Que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermture du jeu")
        # Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #Detecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Verification pour savoir si la souris est en colision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                game.start()

    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)
