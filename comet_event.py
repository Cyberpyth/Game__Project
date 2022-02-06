import pygame
from comet import Comet

# creer une classe pour gerer cet evenement
class CometFallEvent:

    # lors du chargement -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

        #deifinir un groupe de sprite pour sotcker les cometes
        self.all_comets = pygame.sprite.Group()



    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #boucle pour les valeurs en tre 1 et 10
        for i in range(1, 10):
            # apparaitre une premoeire bdf
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #la jauge d'event est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de comet")
            self.meteor_fall()
            self.fall_mode = True #activer l'event


    def update_bar(self, surface):

        #ajouter du pourcentage al abarre
        self.add_percent()

        # barre noir en arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #axe x
            surface.get_height() - 20, #axe y
            surface.get_width(), #longeur fenetre
            10 # epaisseur barre
        ])
        # barre rouge (jauge d'evenement)

        # barre noir en arriere plan
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe x
            surface.get_height() - 20 ,  # axe y
            (surface.get_width() / 100) * self.percent,  # longeur fenetre
            10  # epaisseur barre
        ])
