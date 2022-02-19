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
        - almacenamento da puntuación por xogador nunha base de datos.
        - mostrar un listaxe de xogadores segundo máxima puntuación e a data conseguida.
'''

import os, constantes, time, pygame, sys

import util
import random
from objetos import Objeto
from jugador import Jugador

'''MAIN DEL JUEGO'''
def main():
    util.Utilidades.inicializar(self=None)

    #Gestion del fondo
    screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))
    FramePerSec = pygame.time.Clock()
    imagenFondo = os.path.join('img/fondo.png')
    fondo = pygame.image.load(imagenFondo).convert()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    puntuacion=0

    # Creamos el jugador
    astronauta = Jugador()

    ''' creacion de grupos de sprites, para despues poder colisionar'''
    # grupo que contiene todos los elementos
    all_sprites = pygame.sprite.Group()
    all_sprites.add(astronauta)
    #all_sprites.add(piedra)


    # Creamos el grupo que contiene los enemigos
    numEnemigo = 0
    enemies = pygame.sprite.Group()
    for numEnemigo in range(constantes.ENEMIGOS_INICIALES):
        piedra = Objeto(0, 1) # piedras en dificultad 1
        all_sprites.add(piedra)
        enemies.add(piedra)
        numEnemigo +=1

    # Gestion de velocidad del caida del jugador
    EVENT_INC_SPEED = util.Utilidades.crearEventoIncrementarVelocidad(self=None)
    velocidad = constantes.speed  # inicializamos velocidad desde constante
    posicionFondoY = 0 # Ponemos el fondo al inicio de la imagen

    # Bucle infinito
    while True:
        # control de eventos
        for event in pygame.event.get():
            # Si se produce el evento de incrementar velocidad le sumammos 1
            if event.type == EVENT_INC_SPEED:
                velocidad += 1

            # Evento para salir del juego con la tecla x
            if event.type == pygame.QUIT:
                sys.exit()

            # Evento para pausar con tecla p
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    util.Utilidades.pause(screen)

        # Mover fondo en vertical
        posicionFondoY = util.Utilidades.moverFondo(screen, fondo, velocidad, posicionFondoY)
        posicionFondoYPositivo = posicionFondoY*-1

        # Analizar dificultad
        dificultad = 1
        enemigosSimultaneos = constantes.ENEMIGOS_MAXIMOS_SIMULTANEOS_1
        if posicionFondoYPositivo > constantes.DIFICULTAD_2 :
            dificultad = 2
            enemigosSimultaneos = constantes.ENEMIGOS_MAXIMOS_SIMULTANEOS_2
        if posicionFondoYPositivo > constantes.DIFICULTAD_3:
            dificultad = 3
            enemigosSimultaneos = constantes.ENEMIGOS_MAXIMOS_SIMULTANEOS_3

        if len(enemies.sprites()) < enemigosSimultaneos:
            obj = None

            #Piedras
            if posicionFondoYPositivo < constantes.DIFICULTAD_2:
                obj = Objeto(0, dificultad)

            #Aviones
            if posicionFondoYPositivo > constantes.DIFICULTAD_2:
                obj = Objeto(1, dificultad)

            # Aviones
            if posicionFondoYPositivo > constantes.DIFICULTAD_3:
                obj = Objeto(2, dificultad)

            # Crearlo a la altura del astronauta
            if astronauta.rect != None:
                obj.rect.y = astronauta.rect.y + random.randrange(-200, 200)

            all_sprites.add(obj)
            enemies.add(obj)

        # Mover sprites existentes
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

            # Si se sale de la pantalla, lo eliminamos como enemigo
            if not entity.mover():
                all_sprites.remove(entity)
                enemies.remove(entity)


        #Gestion del mensaje de pausar y puntuacion
        util.Utilidades.puntuacion(screen, (str(puntuacion).zfill(5)), posicionFondoYPositivo)
        
        # si colisiona astronauta con algun enemigo fin del juego con game over
        if pygame.sprite.spritecollideany(astronauta, enemies):
            util.Utilidades.gameOver(screen)
            util.Utilidades.finJuego(all_sprites)
        elif not pygame.sprite.spritecollideany(astronauta, enemies):
            puntuacion+=1


        # Observamos si el bloque protagonista ha colisionado con algo.
        lista_impactos = pygame.sprite.spritecollide(astronauta, enemies, True)
        if lista_impactos:
            util.Utilidades.gameOver(screen)
            util.Utilidades.finJuego(all_sprites)
        elif not lista_impactos:
            # Comprobamos la lista de colisiones.
            for piedra in lista_impactos:
                puntuacion += 1
                print(puntuacion)

        pygame.display.update()
        pygame.display.flip()
        FramePerSec.tick(constantes.FPS)

if __name__ == '__main__':
    main()