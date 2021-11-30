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
        PANTALLA con game over y puntuación
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

    '''GAME OVER '''
    # Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
    fuente = pygame.font.Font(None, 36)
    # Usamos esta variable booleana para avisar que el juego se acabó variable.
    game_over = False
    #color para de GAME OVER
    WHITE = (255, 255, 255)

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

        #si colisiona astronauta con algun enemigo fin del juego
        if pygame.sprite.spritecollideany(astronauta, enemies):
            finJuego(all_sprites)

        #código para GAME OVER
        if game_over:
            # Si el juego finalizó, dibujamos 'el juego se acabó'.
            texto = fuente.render("GAME OVER", True, WHITE)
            texto_rect = texto.get_rect()
            texto_x = screen.get_width() / 2 - texto_rect.width / 2
            texto_y = screen.get_height() / 2 - texto_rect.height / 2
            screen.blit(texto, [texto_x, texto_y])
        else:
            # Si el juego no acabó, dibujamos lo siguiente.
            texto = fuente.render("Haz click para terminar el juego", True, WHITE)
            texto_rect = texto.get_rect()
            texto_x = screen.get_width() / 2 - texto_rect.width / 2
            texto_y = screen.get_height() / 2 - texto_rect.height / 2
            screen.blit(texto, [texto_x, texto_y])

        pygame.display.update()
        FramePerSec.tick(constantes.FPS)

        pygame.quit()

if __name__ == '__main__':
    main()

