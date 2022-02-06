import pygame
import random
import animation



# creer une classe qui va gerer la notion de monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 910 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)


    def set_loot_amount(self, amount):
        self.loot_amount = amount




    def damage(self, amount):
        #Infliger des degats
        self.health -= amount


        #verifier si son nouveau nombre de point de vie est inferieur ou egale a 0
        if self.health <= 0:
            # Repop comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            # si la barre d'event est chargée a son max
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)

            #appel de la methode pour essayer de declancher pluie de comet
            self.game.comet_event.attempt_fall()

        #deifinir la position de ntore jauge de vie ainsi que sa largeur et son epaisseur
        bar_position = [self.rect.x, self.rect.y, self.health, 5]

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # Dessinier la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])



    def forward(self):
        # le deplacement ne se fait que si il ny a pas de collsions avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en colision avec le joueur
        else :
            #infliger des degats
            self.game.player.damage(self.attack)


#definir une classe pour la momie
class Mummy(Monster):


    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

# definir une classe pour l'alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)




