import pygame
import random

from constantes import SCREEN_HEIGHT, SCREEN_WIDTH

class Objeto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(3)

        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load("img/piedra.png"), (70, 45))
            self.radius = 35
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load("img/piedra.png"), (30, 15))
            self.radius = 15
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load("img/piedra.png"), (40, 25))
            self.radius = 25


        self.rect = self.image.get_rect()
        #self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        #self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
        self.rect.x = random.randrange(800)

    def mover(self):
        self.rect.move_ip(7, 1)
        if self.rect.bottom > 600:
            self.rect.top = 0

        if self.rect.right > 900:
            self.rect.left = 0
            self.rect.center = (0, random.randint(30, 370))

    def draw(self, surface):
        surface.blit(self.image, self.rect)