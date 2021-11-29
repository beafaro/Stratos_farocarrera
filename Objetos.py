import pygame
import random

class Objeto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/piedra.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 800 - 40), 0)

    def mover(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


#https://www.programacionfacil.org/cursos/pygame/capitulo_11_moviento_enemigos_y_fisicas.html