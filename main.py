import os

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("STRATOS")

def main():

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(fondo, (0, 0))
        pygame.display.update()

        screen.blit(imagenAstro, (x, y))  #posicionamos astronauta

def mover(self, x=0, y=0):
    if self.rect.centerx + x >= screen.get_width() or self.rect.centerx + x < 0:
        return
    if self.rect.centery + y >= screen.get_height() or self.rect.centery + y < 0:
        return
    # Si el movimiento está dentro de los límites de la pantalla, se "recoloca" el centro de la imagen
    self.rect.center = (self.rect.centerx + x, self.rect.centery + y)

if __name__ == '__main__':
    main()

