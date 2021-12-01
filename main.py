'''
    TAREAS
        hacer fondo
        hacer mover fondo
        hacer astronauta
        colisiones --> cuando colisiona hacer boom y poner sangre
        cambiar direcciones
                --> astronauta debe caer
                --> objetos moverse de lado
        PANTALLA inicial para empezar --> https://pythonprogramming.net/pause-game-pygame/
        PANTALLA con game over y puntuación -^
'''

import os
import time

import pygame, sys, random
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

def moverFondo(screen,fondo,velocidad, y):
    rel_y = y % fondo.get_rect().height
    screen.blit(fondo, (0, rel_y - fondo.get_rect().height))
    if rel_y < constantes.SCREEN_WIDTH:
        screen.blit(fondo, (0, rel_y))
    y -= 1 * velocidad  # fondo mas velocidad
    return y

#código para GAME OVER
def gameOver(screen):
    WHITE = (255, 255, 255)
    gameOverFont = pygame.font.SysFont('arial.ttf', 54)  # Fuente y tamaño final del juego
    gameOverSurf = gameOverFont.render("GAME OVER", True, WHITE)  # Game over content display
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (400, 300)  # posición de visualización
    screen.blit(gameOverSurf, gameOverRect)

#código para pantalla de pausa
def paused(screen, WHITE):
    pausedFont = pygame.font.SysFont("arial.ttf", 54)
    pausedSurf = pausedFont.render("PAUSED", True, WHITE)
    pausedRect = pausedSurf.get_rect()
    pausedRect.midtop = (400, 300) #((ancho_de_pantalla / 2), (altura_de_pantalla / 2))
    screen.blit(pausedSurf, pausedRect)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # gameDisplay.fill (blanco)
        botón("Continuar", 150, 450, 100, 50, verde, bright_green, Reanudar)
        botón("Salir", 550, 450, 100, 50, rojo, bright_red, quitgame)

        pygame.display.update()


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
    #grupo que contiene todos los elementos
    all_sprites = pygame.sprite.Group()
    all_sprites.add(astronauta)
    all_sprites.add(piedra)
    #grupo que contiene los enemigos
    enemies = pygame.sprite.Group()
    enemies.add(piedra)

    EVENT_INC_SPEED = crearEventoIncrementarVelocidad()
    velocidad = constantes.speed #inicializamos velocidad desde constante
    y = 0

    while True:
        #screen.blit(fondo, (0, 0))

        # control de eventos
        for event in pygame.event.get():
            #si se produce el evento de incrementar velocidad le sumammos
            if event.type == EVENT_INC_SPEED:
                velocidad += 1

            if event.type == pygame.QUIT:
                sys.exit()

        #mover fondo en vertical
        y = moverFondo(screen, fondo, velocidad, y)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.mover()

        #si colisiona astronauta con algun enemigo fin del juego con game over
        if pygame.sprite.spritecollideany(astronauta, enemies):
            gameOver(screen)
            finJuego(all_sprites)

        pygame.display.update()
        FramePerSec.tick(constantes.FPS)

if __name__ == '__main__':
    main()

