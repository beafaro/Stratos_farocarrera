import pygame
import random

'''class Objeto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/piedra.png")
        self.rect = self.image.get_rect()
        #self.rect.center = (random.randint(40, 800 - 40), 0)

    def mover(self):
        self.rect.move_ip(7, 1)
        if self.rect.bottom > 600:
            self.rect.top = 0

        if self.rect.right > 900:
            self.rect.left = 0
            self.rect.center = (0, random.randint(30, 370))


    def draw(self, surface):
        surface.blit(self.image, self.rect)

#https://www.programacionfacil.org/cursos/pygame/capitulo_11_moviento_enemigos_y_fisicas.html
# para enemigos más rápidos que otros
    # self.velocidad_aleatoria_x = random.randrange(1, 10)
    # self.velocidad_aleatoria_y = random.randrange(1, 10)'''

class Objeto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(3)

        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load("img/piedra.png").convert(), (140, 90))
            self.radius = 75
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load("img/piedra.png").convert(), (70, 45))
            self.radius = 35
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load("img/piedra.png").convert(), (30, 15))
            self.radius = 15

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800)

    def mover(self):
        self.rect.move_ip(7, 1)
        if self.rect.bottom > 600:
            self.rect.top = 0

        if self.rect.right > 900:
            self.rect.left = 0
            self.rect.center = (0, random.randint(30, 370))