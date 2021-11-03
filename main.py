import os

import pygame, sys
from pygame.locals import *

import constantes


def main():
    pygame.init()
    FPS = 60
    FramePerSec = pygame.time.Clock()

    # tamaño pantalla
    screen = pygame.display.set_mode((800, 600))
    # titulo ventana
    pygame.display.set_caption("STRATOS")

    imagenFondo = os.path.join('img/cielo.png')
    fondo = pygame.image.load(imagenFondo)
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    x = constantes.x
    y = constantes.y
    velocidad = constantes.speed

    class Jugador(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("img/astronauta.png")
            self.rect = self.image.get_rect()
            self.rect.center = (160, 520)

        def mover(self):
            pulsa = pygame.key.get_pressed()
            if self.rect.left > 0:
                if pulsa[K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < 800:
                if pulsa[K_RIGHT]:
                    self.rect.move_ip(5, 0)

        def draw(self, surface):
            surface.blit(self.image, self.rect)

    astronauta = Jugador()

    while True:
        screen.blit(fondo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        astronauta.mover()

        astronauta.draw(screen)

        pygame.display.update()
        FramePerSec.tick(FPS)


if __name__ == '__main__':
    main()

