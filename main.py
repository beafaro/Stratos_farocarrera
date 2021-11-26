'''
    TAREAS
        hacer fondo
        hacer mover fondo
        hacer astronauta
        colisiones
        cambiar direcciones
                --> astronauta debe caer
                --> objetos moverse de lado
'''

import os
import time

import pygame, sys, random
import constantes
from Objetos import Objeto
from jugador import Jugador


def main():
    pygame.init()
    FPS = 30
    FramePerSec = pygame.time.Clock()

    # tamaño pantalla
    ancho_pantalla = constantes.SCREEN_WIDTH #400
    alto_pantalla = constantes.SCREEN_HEIGHT #540
    screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
    # titulo ventana
    pygame.display.set_caption("STRATOS")

    imagenFondo = os.path.join('img/copia_fondo.png')
    #fondo = pygame.image.load(imagenFondo)
    fondo = pygame.image.load(imagenFondo).convert()
    x = 0

    os.environ['SDL_VIDEO_CENTERED'] = '1'

    astronauta = Jugador()
    piedra = Objeto()

    ''' creacion de grupos de sprites, para despues poder colisionar
    enemies = pygame.sprite.Group()
    enemies.add(piedra)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(astronauta)
    all_sprites.add(piedra)'''

    while True:
        #screen.blit(fondo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        '''if pygame.sprite.spritecollideany(astronauta, enemies):
            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()'''
        rel_x = x % fondo.get_rect().width
        screen.blit(fondo, (rel_x - fondo.get_rect().width, 0))
        if rel_x < ancho_pantalla:
            screen.blit(fondo, (rel_x, 0))
        x -= 1

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == '__main__':
    main()

