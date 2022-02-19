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

import os, constantes, time, pygame, sys

import util
import random
from objetos import Objeto
from jugador import Jugador

'''MAIN DEL JUEGO'''
def main():
    inicializar()
    screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))
    FramePerSec = pygame.time.Clock()
    imagenFondo = os.path.join('img/fondo.png')
    fondo = pygame.image.load(imagenFondo).convert()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    marcador=0

    astronauta = Jugador()
    #piedra = Objeto()

    ''' creacion de grupos de sprites, para despues poder colisionar'''
    # grupo que contiene todos los elementos
    all_sprites = pygame.sprite.Group()
    all_sprites.add(astronauta)

    #all_sprites.add(piedra)
    # grupo que contiene los enemigos
    i= 0
    enemies = pygame.sprite.Group()

    for i in range(10):
        piedra = Objeto()
        all_sprites.add(piedra)
        enemies.add(piedra)
        all_sprites.add(piedra)
        i +=1

    EVENT_INC_SPEED = crearEventoIncrementarVelocidad()
    velocidad = constantes.speed  # inicializamos velocidad desde constante
    y = 0

    while True:
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
                    util.Utilidades.pause(screen)

        # mover fondo en vertical
        y = moverFondo(screen, fondo, velocidad, y)

        #mostrar mensaje para pausar
        puntuacion(screen)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.mover()

        '''# si colisiona astronauta con algun enemigo fin del juego con game over
        if pygame.sprite.spritecollideany(astronauta, enemies):
            gameOver(screen)
            finJuego(all_sprites)
        elif not pygame.sprite.spritecollideany(astronauta, enemies):
            marcador+=1
            print(marcador)'''

        # Observamos si el bloque protagonista ha colisionado con algo.
        lista_impactos = pygame.sprite.spritecollide(astronauta, enemies, True)
        if lista_impactos:
            util.Utilidades.gameOver(screen)
            util.Utilidades.finJuego(all_sprites)
        elif not lista_impactos:
            # Comprobamos la lista de colisiones.
            for piedra in lista_impactos:
                marcador += 1
                print(marcador)

        pygame.display.update()
        pygame.display.flip()
        FramePerSec.tick(constantes.FPS)

if __name__ == '__main__':
    main()