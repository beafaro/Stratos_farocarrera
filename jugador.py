import pygame
from pygame.locals import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/astronauta.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)

    def mover(self):
        pulsa = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pulsa[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 800:
            if pulsa[K_RIGHT]:
                self.rect.move_ip(5, 0)

        # if pressed_keys[K_UP]:
            # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
            # self.rect.move_ip(0,5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#https://coderslegacy.com/python/pygame-tutorial-part-2/