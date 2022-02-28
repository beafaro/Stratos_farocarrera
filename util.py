import os, constantes, time, pygame, sys

import conexion
import util


class Utilidades:
    def inicializar(self):
        pygame.init()
        # titulo ventana
        pygame.display.set_caption("STRATOS")

    def crearEventoIncrementarVelocidad(self):
        INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(INC_SPEED, constantes.TIEMPO_ACTUALIZAR_VELOCIDAD)
        return INC_SPEED

    def finJuego(all_sprites):
        for entity in all_sprites:
            entity.kill()
        pygame.quit()
        sys.exit()

    def moverFondo(screen, fondo, velocidad, y):
        rel_y = y % fondo.get_rect().height
        screen.blit(fondo, (0, rel_y - fondo.get_rect().height))
        if rel_y < constantes.SCREEN_WIDTH:
            screen.blit(fondo, (0, rel_y))
        y -= 0.3 * velocidad  # fondo mas velocidad
        return y

    def pedirNombre(screen, fondo, posicionFondoY, all_sprites):
        if posicionFondoY > constantes.DIFICULTAD_2:
            color = (0, 0, 0)
        else:
            color = (254, 254, 254)

        nombre = "";
        while True:

            '''TEXTO PARA OPCIONES'''
            letra_opciones = pygame.font.SysFont("arial.ttf", 30, False, False)
            superficie_opciones = letra_opciones.render("Introduzca su nombre: ", True, color)
            rectangulo_opciones = superficie_opciones.get_rect()
            rectangulo_opciones.midtop = (400, 350)
            screen.blit(superficie_opciones, rectangulo_opciones)

            '''TEXTO PARA OPCIONES'''
            letra_opciones = pygame.font.SysFont("arial.ttf", 30, False, False)
            superficie_opciones = letra_opciones.render(nombre, True, color)
            rectangulo_opciones = superficie_opciones.get_rect()
            rectangulo_opciones.midtop = (400, 370)
            screen.blit(superficie_opciones, rectangulo_opciones)

            pygame.display.update()

            util.Utilidades.moverFondo(screen, fondo, 0, posicionFondoY)
            for entity in all_sprites:
                screen.blit(entity.image, entity.rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return nombre
                    elif event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    elif event.key >= pygame.K_a and event.key < pygame.K_z:
                        try:
                            nombre = nombre + chr(event.key)
                        except Exception as error:
                            nombre = nombre
        return nombre

    def guardarPuntuacion(nombre, puntuacion):
        conexion.Conexion.db_connect(constantes.FILENAME)
        dato = [nombre, puntuacion]
        conexion.Conexion.guardarPuntuacion(dato)

    def visualizarPuntuaciones(screen, posicionFondoY, puntuaciones):
        if posicionFondoY*-1 < constantes.DIFICULTAD_5:
            color = (244, 208, 63)
        else:
            color = (254, 254, 254)

        '''TEXTO PARA OPCIONES'''
        letra_opciones = pygame.font.SysFont("arial.ttf", 32, False, False)
        superficie_opciones = letra_opciones.render("Top 5", True, color)
        rectangulo_opciones = superficie_opciones.get_rect()
        rectangulo_opciones.midtop = (400, 340)
        screen.blit(superficie_opciones, rectangulo_opciones)

        y = 360
        for x in puntuaciones:
            y = y+20
            '''TEXTO PARA OPCIONES'''
            letra_opciones = pygame.font.SysFont("arial.ttf", 30, False, False)
            superficie_opciones = letra_opciones.render(x[0] + " - " +x[1], True, color)
            rectangulo_opciones = superficie_opciones.get_rect()
            rectangulo_opciones.midtop = (400, y)
            screen.blit(superficie_opciones, rectangulo_opciones)

    def gameOver(screen, fondo, posicionFondoY, all_sprites, puntuacion):
        # código para GAME OVER
        RED = (254, 0, 0)
        conexion.Conexion.db_connect(constantes.FILENAME)
        puntuaciones = conexion.Conexion.cargarPuntuaciones(self=None)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        time.sleep(0.5)
                        return 1
                    if event.key == pygame.K_x:
                        util.Utilidades.finJuego(all_sprites)
                    if event.key == pygame.K_g:
                        nombre = util.Utilidades.pedirNombre(screen, fondo, posicionFondoY, all_sprites)
                        util.Utilidades.guardarPuntuacion(nombre, puntuacion)
                        puntuaciones = conexion.Conexion.cargarPuntuaciones(self=None)

            letra_gameOver = pygame.font.SysFont('arial.ttf', 100)  # Fuente y tamaño final del juego
            superficie_gameOver = letra_gameOver.render("GAME OVER", True, RED)  # Game over content display
            rectangulo_gameOver = superficie_gameOver.get_rect()
            rectangulo_gameOver.midtop = (400, 200)  # posición de visualización
            screen.blit(superficie_gameOver, rectangulo_gameOver)

            '''TEXTO PARA OPCIONES'''
            letra_opciones = pygame.font.SysFont("arial.ttf", 30, False, False)
            superficie_opciones = letra_opciones.render("Pulsa g para guardar la puntuacion", True, RED)
            rectangulo_opciones = superficie_opciones.get_rect()
            rectangulo_opciones.midtop = (400, 270)
            screen.blit(superficie_opciones, rectangulo_opciones)

            '''TEXTO PARA OPCIONES'''
            letra_opciones = pygame.font.SysFont("arial.ttf", 30, False, False)
            superficie_opciones = letra_opciones.render("Pulsa r para volver a jugar o X para salir", True, RED)
            rectangulo_opciones = superficie_opciones.get_rect()
            rectangulo_opciones.midtop = (400, 290)
            screen.blit(superficie_opciones, rectangulo_opciones)

            util.Utilidades.visualizarPuntuaciones(screen, posicionFondoY, puntuaciones)

            pygame.display.update()

    def gameSuccess(screen, fondo, posicionFondoY, all_sprites, puntuacion):
        GREEN = (50, 220, 50)
        conexion.Conexion.db_connect(constantes.FILENAME)
        puntuaciones = conexion.Conexion.cargarPuntuaciones(self=None)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        time.sleep(0.5)
                        return 1
                    if event.key == pygame.K_x:
                        util.Utilidades.finJuego(all_sprites)
                    if event.key == pygame.K_g:
                        nombre = util.Utilidades.pedirNombre(screen, fondo, posicionFondoY, all_sprites)
                        util.Utilidades.guardarPuntuacion(nombre, puntuacion)
                        puntuaciones = conexion.Conexion.cargarPuntuaciones(self=None)

            letra_success = pygame.font.SysFont('arial.ttf', 100)  # Fuente y tamaño final del juego
            superficie_success = letra_success.render("YOU WIN!", True, GREEN)  # Game over content display
            rectangulo_success = superficie_success.get_rect()
            rectangulo_success.midtop = (400, 190)  # posición de visualización
            screen.blit(superficie_success, rectangulo_success)

            '''TEXTO PARA OPCIONES'''
            letra_opciones = pygame.font.SysFont("arial.ttf", 30, False, False)
            superficie_opciones = letra_opciones.render("Pulsa r para volver a jugar o X para salir", True, GREEN)
            rectangulo_opciones = superficie_opciones.get_rect()
            rectangulo_opciones.midtop = (400, 260)
            screen.blit(superficie_opciones, rectangulo_opciones)

            util.Utilidades.visualizarPuntuaciones(screen, posicionFondoY, puntuaciones)

            pygame.display.update()


    def pause(screen):
        # código para pantalla de pausa con pulsacion de tecla p para pausar
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
            letra_pausa1 = pygame.font.SysFont("arial.ttf", 100, False, False)  # fuente para texto PAUSA
            superficie_pausa1 = letra_pausa1.render("PAUSA", True, YELLOW)  # PAUSA en display
            rectangulo_pausa1 = superficie_pausa1.get_rect()
            rectangulo_pausa1.midtop = (400, 250)  # ((ancho_de_pantalla / 2), (altura_de_pantalla / 2))
            screen.blit(superficie_pausa1, rectangulo_pausa1)

            '''TEXTO PARA OPCIONES SEGUIR'''
            letra_pausa2 = pygame.font.SysFont("arial.ttf", 30, False, False)
            superficie_pausa2 = letra_pausa2.render("Pulsa S para seguir o X para salir", True, YELLOW)
            rectangulo_pausa2 = superficie_pausa2.get_rect()
            rectangulo_pausa2.midtop = (400, 320)
            screen.blit(superficie_pausa2, rectangulo_pausa2)

            pygame.display.update()


    def puntuacion(screen, texto, dificultad):
        YELLOW = (244, 208, 63)
        letra_puntuacion = pygame.font.SysFont("arial.ttf", 25, True, True)
        superficie_puntuacion = letra_puntuacion.render("Para pausar pulsa 'p'. (Puntuación: "+texto+")", True, True, YELLOW)  # PAUSA en display
        rectangulo_puntuacion = superficie_puntuacion.get_rect()
        rectangulo_puntuacion.center = (600, 10)
        screen.blit(superficie_puntuacion, rectangulo_puntuacion)
