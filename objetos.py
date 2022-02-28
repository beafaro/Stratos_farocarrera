import pygame
import random

from constantes import SCREEN_HEIGHT, SCREEN_WIDTH

class Objeto(pygame.sprite.Sprite):
    def __init__(self, tipoEnemigo, dificultad):
        super().__init__()
        self.tipo = "enemigo"
        self.dificultad = dificultad

        # Tipos de enemigos
        # Piedra
        if tipoEnemigo == 0:
            self.srcImage = "img/piedra.png"
            self.tamanho_aleatorio = random.randrange(3)
            if self.tamanho_aleatorio == 0:
                self.image = pygame.transform.scale(pygame.image.load("img/piedra.png"), (70, 45))
                self.radius = 35
                self.velocidad_x = random.randrange(5, 6)
                self.velocidad_y = 1
            if self.tamanho_aleatorio == 1:
                self.image = pygame.transform.scale(pygame.image.load("img/piedra.png"), (40, 25))
                self.radius = 25
                self.velocidad_x = random.randrange(6, 7)
                self.velocidad_y = 2
            if self.tamanho_aleatorio == 2:
                self.image = pygame.transform.scale(pygame.image.load("img/piedra.png"), (30, 15))
                self.radius = 15
                self.velocidad_x = random.randrange(7, 9)
                self.velocidad_y = -1

        # Avion
        if tipoEnemigo == 1:
            self.image = pygame.transform.scale(pygame.image.load("img/avion.png"), (70, 45))
            self.velocidad_x = random.randrange(7, 9)
            self.velocidad_y = -1

        # Pajaro
        if tipoEnemigo == 2:
            self.image = pygame.transform.scale(pygame.image.load("img/pajaro.png"), (30, 15))
            self.velocidad_x = random.randrange(3, 7)
            self.velocidad_y = -2


        self.rect = self.image.get_rect()
        #self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
        self.rect.x = -50

    def mover(self):

        # Variamos velocidades en funcion de la dificultad actual
        velocidad_x = self.velocidad_x
        velocidad_y = self.velocidad_y
        if self.dificultad == 2:
            velocidad_x = self.velocidad_x + 2
        if self.dificultad == 4:
            velocidad_x = self.velocidad_x + 4
            velocidad_y = self.velocidad_y + 3

        self.rect.move_ip(velocidad_x, velocidad_y)
        if self.rect.bottom > 600:
            return False

        if self.rect.right > 900:
            return False

        return True

    def draw(self, surface):
        surface.blit(self.image, self.rect)