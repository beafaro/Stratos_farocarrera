import os

import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("STRATOS")

    imagenFondo = os.path.join('img', 'cielo.png')
    fondo = pygame.image.load(imagenFondo)
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    imagenAstro = os.path.join('img', 'astronauta.png')
    astronauta = pygame.image.load(imagenAstro)

    pulsar = pygame.key.get_pressed()  # capturamos pulsaciones teclas izq/der
    if pulsar[K_LEFT]:
        astronauta.move_ip(-5, 0)
    if pulsar[K_RIGHT]:
        astronauta.move_ip(5, 0)


    while True:
        screen.blit(fondo, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(imagenAstro, (x, y))  #posicionamos astronauta



if __name__ == '__main__':
    main()

