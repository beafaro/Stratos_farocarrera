'''
    TAREAS
        hacer fondo
        hacer mover fondo
        hacer astronauta
        colisiones --> cuando colisiona hacer boom y poner sangre
        cambiar direcciones
                --> astronauta debe caer
                --> objetos moverse de lado
        PANTALLA inicial para empezar
        PANTALLA con game over con boton seguir jugando y guardar su puntuación
        PANTALLA pausa con botones seguir jugando o salir del juego --> guardando su puntuación
'''

import os
import time

import pygame, sys
from pygame.locals import *

import constantes
from Objetos import Objeto
from jugador import Jugador

def inicializar():
    pygame.init()
    # titulo ventana
    pygame.display.set_caption("STRATOS")

def crearEventoIncrementarVelocidad():
    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)
    return INC_SPEED

def finJuego(all_sprites):
    pygame.display.update()
    for entity in all_sprites:
        entity.kill()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def moverFondo(screen, fondo, velocidad, y):
    rel_y = y % fondo.get_rect().height
    screen.blit(fondo, (0, rel_y - fondo.get_rect().height))
    if rel_y < constantes.SCREEN_WIDTH:
        screen.blit(fondo, (0, rel_y))
    y -= 1 * velocidad  # fondo mas velocidad
    return y

# código para GAME OVER
def gameOver(screen):
    WHITE = (255, 255, 255)
    gameOverFont = pygame.font.SysFont('arial.ttf', 54)  # Fuente y tamaño final del juego
    gameOverSurf = gameOverFont.render("GAME OVER", True, WHITE)  # Game over content display
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (400, 300)  # posición de visualización
    screen.blit(gameOverSurf, gameOverRect)

# código para pantalla de pausa con pulsacion de tecla p para pausar-reanudar
def paused(screen):
    WHITE = (255, 255, 255)
    pausedFont = pygame.font.SysFont("arial.ttf", 54)  # fuente para texto PAUSA
    pausedSurf = pausedFont.render("PAUSA", True, WHITE)  # PAUSA en display
    pausedRect = pausedSurf.get_rect()
    pausedRect.midtop = (400, 300)  # ((ancho_de_pantalla / 2), (altura_de_pantalla / 2))
    screen.blit(pausedSurf, pausedRect)
# otra forma de pausar hasta que el usuario presione una tecla --> os.system("pause")


'''MAIN DEL JUEGO'''

def main():
    inicializar()
    screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))
    FramePerSec = pygame.time.Clock()

    imagenFondo = os.path.join('img/copia_fondo.png')
    fondo = pygame.image.load(imagenFondo).convert()

    os.environ['SDL_VIDEO_CENTERED'] = '1'

    astronauta = Jugador()
    piedra = Objeto()

    ''' creacion de grupos de sprites, para despues poder colisionar'''
    # grupo que contiene todos los elementos
    all_sprites = pygame.sprite.Group()
    all_sprites.add(astronauta)
    all_sprites.add(piedra)
    # grupo que contiene los enemigos
    enemies = pygame.sprite.Group()
    enemies.add(piedra)

    EVENT_INC_SPEED = crearEventoIncrementarVelocidad()
    velocidad = constantes.speed  # inicializamos velocidad desde constante
    y = 0

    pause = False

    while True:
        # screen.blit(fondo, (0, 0))

        # control de eventos
        for event in pygame.event.get():
            # si se produce el evento de incrementar velocidad le sumammos
            if event.type == EVENT_INC_SPEED:
                velocidad += 1

            if event.type == pygame.QUIT:
                sys.exit()
            #evento para pausar con tecla p
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAUSE:
                    pause = not pause
                    paused(screen)

        # mover fondo en vertical
        y = moverFondo(screen, fondo, velocidad, y)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.mover()

        # si colisiona astronauta con algun enemigo fin del juego con game over
        if pygame.sprite.spritecollideany(astronauta, enemies):
            gameOver(screen)
            finJuego(all_sprites)

        pygame.display.update()
        pygame.display.flip()
        FramePerSec.tick(constantes.FPS)

if __name__ == '__main__':
    main()