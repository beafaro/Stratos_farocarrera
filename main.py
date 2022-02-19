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

import conexion
import util
import random
from objetos import Objeto
from jugador import Jugador

'''MAIN DEL JUEGO'''
def main():
    conexion.Conexion.create_DB(constantes.FILENAME)
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
    posicionFondoY = constantes.COMIENZO_JUEGO # Ponemos el fondo al inicio de la imagen

    # Bucle infinito
    alternancia = 1
    finJuego = False;
    while True:
        alternancia = alternancia * -1

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
                    # Evento para pausar con tecla p

        # Mover fondo en vertical
        if posicionFondoY > constantes.FINAL_JUEGO:
            posicionFondoY = util.Utilidades.moverFondo(screen, fondo, velocidad, posicionFondoY)
        else:
            posicionFondoY = util.Utilidades.moverFondo(screen, fondo, 0, posicionFondoY)
            finJuego = True

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
        if posicionFondoYPositivo > constantes.DIFICULTAD_4:
            dificultad = 4
            enemigosSimultaneos = constantes.ENEMIGOS_MAXIMOS_SIMULTANEOS_4
        if posicionFondoYPositivo > constantes.DIFICULTAD_5:
            dificultad = 5
            enemigosSimultaneos = constantes.ENEMIGOS_MAXIMOS_SIMULTANEOS_5

        # Crear enemigos
        if len(enemies.sprites()) < enemigosSimultaneos:
            obj = None

            # Piedras
            if dificultad == 1:
                #print("Nivel 1: Creando 0")
                obj = Objeto(0, dificultad)

            # Piedras y aviones
            if dificultad == 2:
                if alternancia < 0:
                    #print("Nivel 2: Creando 0")
                    obj = Objeto(0, dificultad)
                else:
                    #print("Nivel 2: Creando 1")
                    obj = Objeto(1, dificultad)

            # Aviones
            if dificultad == 3:
                #print("Nivel 3: Creando 1")
                obj = Objeto(1, dificultad)

            # Aviones y pajaros
            if dificultad == 4:
                if alternancia < 0:
                    #print("Nivel 4: Creando 1")
                    obj = Objeto(1, dificultad)
                else:
                    #print("Nivel 4: Creando 2")
                    obj = Objeto(2, dificultad)

            # Pajaros
            if dificultad == 5:
                #print("Nivel 5: Creando 2")
                obj = Objeto(2, dificultad)

            # Crearlo a la altura del astronauta
            if astronauta.rect != None:
                obj.rect.y = astronauta.rect.y + random.randrange(-200, 200)

            all_sprites.add(obj)
            enemies.add(obj)

        # Mover sprites existentes
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

            if (entity.tipo == "astronauta") and finJuego:
                entity.moverFinJuego()
            elif not entity.mover(): # Si se sale de la pantalla, lo eliminamos como enemigo
                    all_sprites.remove(entity)
                    enemies.remove(entity)


        #Gestion del mensaje de pausar y puntuacion
        util.Utilidades.puntuacion(screen, (str(puntuacion).zfill(5)), posicionFondoYPositivo)
        
        # si colisiona astronauta con algun enemigo fin del juego con game over
        if pygame.sprite.spritecollideany(astronauta, enemies):
            if util.Utilidades.gameOver(screen, fondo, posicionFondoY, all_sprites, puntuacion) == 1:
                main()
        elif not pygame.sprite.spritecollideany(astronauta, enemies):
            puntuacion+=1


        # Observamos si el bloque protagonista ha colisionado con algo.
        lista_impactos = pygame.sprite.spritecollide(astronauta, enemies, True)
        if lista_impactos:
            util.Utilidades.gameOver(screen, fondo, posicionFondoY, all_sprites, puntuacion)
        elif not lista_impactos:
            # Comprobamos la lista de colisiones.
            for piedra in lista_impactos:
                puntuacion += 1
                print(puntuacion)

        pygame.display.update()
        pygame.display.flip()
        FramePerSec.tick(constantes.FPS)

        if finJuego and astronauta.estaEnFinal():
            if util.Utilidades.gameSuccess(screen, fondo, posicionFondoY, all_sprites, puntuacion) == 1:
                main()

if __name__ == '__main__':
    main()