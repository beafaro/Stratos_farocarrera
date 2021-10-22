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
    navep = pygame.image.load(imagenAstro)


    x = constantes.x  # posición x na pantalla
    y = constantes.y  # posición y na pantalla
    speed = constantes.speed  # cantos pixels se move con cada pulsacion

    pulsar = pygame.key.get_pressed()  # capturamos o evento
    if pulsar[K_LEFT] and x > 20:  # móvese a esquerda ata un borde da ventana
        x -= speed
    if pulsar[K_RIGHT] and x < 950:  # moves a dereita ata o borde da ventana
        x += speed


    while True:
        screen.blit(fondo, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(imagenAstro, (x, y))  #posicionamos astronauta



if __name__ == '__main__':
    main()

