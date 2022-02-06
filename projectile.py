import pygame


#Definir la classe qui gere le projectile du joueur

class Projectile(pygame.sprite.Sprite):


    #Defniri le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #Tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #Verifier si le projo entre en collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projo
            self.remove()

        #verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #Suppr le projectile
            self.remove()
            #Infliger des degats
            monster.damage(self.player.attack)

        #Verifier si notre projectile n'est plus présent sur l'ecran
        if self.rect.x > 1080:
            #Suppimer le projectile (en dehors de l'ecran)
            self.remove()
