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
import random as rand

import pygame, sys

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
    if rel_y < constantes.SCREEN_HEIGHT:
        screen.blit(fondo, (0, rel_y))
    y -= 0.5 * velocidad  # fondo mas velocidad
    return y




# código para GAME OVER
def gameOver(screen):
    RED = (254, 0, 0)
    gameOverFont = pygame.font.SysFont('arial.ttf', 100)  # Fuente y tamaño final del juego
    gameOverSurf = gameOverFont.render("GAME OVER", True, RED)  # Game over content display
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (400, 300)  # posición de visualización
    screen.blit(gameOverSurf, gameOverRect)

# código para pantalla de pausa con pulsacion de tecla p para pausar-reanudar
def pause(screen):
    YELLOW = (244, 208, 63)

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    paused = False
                if event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

        '''TEXTO PARA PAUSA'''
        pausedFont = pygame.font.SysFont("arial.ttf", 100, False, False)  # fuente para texto PAUSA
        pausedSurf = pausedFont.render("PAUSA", True, YELLOW)  # PAUSA en display
        pausedRect = pausedSurf.get_rect()
        pausedRect.midtop = (400, 250)  # ((ancho_de_pantalla / 2), (altura_de_pantalla / 2))
        screen.blit(pausedSurf, pausedRect)

        '''TEXTO PARA OPCIONES SEGUIR'''
        pausedFont2 = pygame.font.SysFont("arial.ttf", 30, False, False)
        pausedSurf2 = pausedFont2.render("Pulsa S para seguir o X para salir", True, YELLOW)
        pausedRect2 = pausedSurf2.get_rect()
        pausedRect2.midtop = (400, 320)
        screen.blit(pausedSurf2, pausedRect2)

        pygame.display.update()

def puntuacion(screen):
    YELLOW = (244, 208, 63)
    puntosFont = pygame.font.SysFont("arial.ttf", 25, True, True)
    puntosSurf = puntosFont.render("Para pausar pulsa 'p'", True, YELLOW)  # PAUSA en display
    screen.blit(puntosSurf, (600, 10))



'''MAIN DEL JUEGO'''

def main():
    inicializar()
    screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))
    FramePerSec = pygame.time.Clock()

    imagenFondo = os.path.join('img/copia_fondo.png')
    fondo = pygame.image.load(imagenFondo).convert()

    os.environ['SDL_VIDEO_CENTERED'] = '1'

    #astronauta = Jugador()
    #piedra = Objeto()
    astronauta = pygame.image.load("img/astronauta.png")
    rectanguloAstronauta = astronauta.get_rect()
    rectanguloAstronauta.left = constantes.SCREEN_WIDTH/2
    rectanguloAstronauta.top = constantes.SCREEN_HEIGHT-50
    piedra = pygame.image.load("img/piedra.png")

    ''' creacion de grupos de sprites, para despues poder colisionar
    # grupo que contiene todos los elementos
    all_sprites = pygame.sprite.Group()
    all_sprites.add(astronauta)

    all_sprites.add(piedra)
    # grupo que contiene los enemigos
    i= 0
    enemies = pygame.sprite.Group()
    piedra = Objeto()
    for i in range(6):
        enemies.add(piedra)
        all_sprites.add(piedra)
        i +=1'''

    EVENT_INC_SPEED = crearEventoIncrementarVelocidad()
    velocidad = constantes.speed  # inicializamos velocidad desde constante
    y = 0

    while True:
        # screen.blit(fondo, (0, 0))

        cantidadPiedras = 10
        piedrasVisibles = {}
        velocidadesX = {}
        velocidadesY = {}

        rectangulosPiedras = {}


        for i in range(0, cantidadPiedras+1):
            rectangulosPiedras[i] = piedra.get_rect()
            rectangulosPiedras[i].left = rand.randrange(30, 370)
            rectangulosPiedras[i].top = rand.randrange(10,301)
            piedrasVisibles[i] = True
            velocidadesX[i] = 3
            velocidadesY[i] = 3

        # control de eventos
        for event in pygame.event.get():
            # si se produce el evento de incrementar velocidad le sumammos
            if event.type == EVENT_INC_SPEED:
                velocidad += 1

            if event.type == pygame.QUIT:
                sys.exit()
            #evento para pausar con tecla p
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause(screen)

        # mover fondo en vertical
        y = moverFondo(screen, fondo, velocidad, y)

        #mostrar mensaje para pausar
        puntuacion(screen)

        '''for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.mover()'''

        # ---- Actualizar estado ----
        for i in range(0, cantidadPiedras + 1):
            rectangulosPiedras[i].left += velocidadesX[i]
            rectangulosPiedras[i].top += velocidadesY[i]
            if rectangulosPiedras[i].left < 0 or rectangulosPiedras[i].right > constantes.SCREEN_WIDTH:
                velocidadesX[i] = -velocidadesX[i]
            if rectangulosPiedras[i].top < 0 or rectangulosPiedras[i].bottom > constantes.SCREEN_HEIGHT:
                velocidadesY[i] = -velocidadesY[i]

        # si colisiona astronauta con algun enemigo fin del juego con game over
        '''if pygame.sprite.spritecollideany(astronauta, enemies):
            gameOver(screen)
            finJuego(all_sprites)'''

        '''# ---- Comprobar colisiones ----'''
        for i in range(0, cantidadPiedras + 1):
            if piedrasVisibles[i]:
                if rectanguloAstronauta.colliderect(rectangulosPiedras[i]):
                    gameOver(screen)
                    finJuego()
            https: // www.nachocabanes.com / python / pygame10.php
            #puntos += 10

        cantidadPiedrasVisibles = 0
        for i in range(0, cantidadPiedras + 1):
            if piedrasVisibles[i]:
                cantidadPiedrasVisibles = cantidadPiedrasVisibles + 1

        pygame.display.update()
        pygame.display.flip()
        FramePerSec.tick(constantes.FPS)

if __name__ == '__main__':
    main()