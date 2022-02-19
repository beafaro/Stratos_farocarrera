import pygame
from pygame.locals import *

import constantes


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tipo = "astronauta"
        self.image = pygame.image.load("img/astronauta.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 250)

    def mover(self):
        pulsa = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pulsa[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 800:
            if pulsa[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pulsa[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 600:
            if pulsa[K_DOWN]:
                self.rect.move_ip(0, 5)
        return True

    def moverFinJuego(self):
        if not self.estaEnFinal():
            self.rect.move_ip(0, 5)

        pulsa = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pulsa[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 800:
            if pulsa[K_RIGHT]:
                self.rect.move_ip(5, 0)
        return True

    def estaEnFinal(self):
        if self.rect.y + self.rect.height + self.rect.height/2 < constantes.SCREEN_HEIGHT:
            return False
        else:
            return True

    def draw(self, surface):
        surface.blit(self.image, self.rect)