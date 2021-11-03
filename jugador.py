import os
import pygame.sprite


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        imagenAstro = os.path.join('img', 'astronauta.png')
        astronauta = pygame.image.load(imagenAstro)