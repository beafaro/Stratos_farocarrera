import os, constantes, time, pygame, sys

class Utilidades:
    def inicializar(self):
        pygame.init()
        # titulo ventana
        pygame.display.set_caption("STRATOS")


    def crearEventoIncrementarVelocidad(self):
        INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(INC_SPEED, 3000)
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
        y -= 0.3 * velocidad  # fondo mas velocidad
        return y


    def gameOver(screen):
        # código para GAME OVER
        RED = (254, 0, 0)
        letra_gameOver = pygame.font.SysFont('arial.ttf', 100)  # Fuente y tamaño final del juego
        superficie_gameOver = letra_gameOver.render("GAME OVER", True, RED)  # Game over content display
        rectangulo_gameOver = superficie_gameOver.get_rect()
        rectangulo_gameOver.midtop = (400, 300)  # posición de visualización
        screen.blit(superficie_gameOver, rectangulo_gameOver)


    def pause(screen):
        # código para pantalla de pausa con pulsacion de tecla p para pausar-reanudar
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
        superficie_puntuacion = letra_puntuacion.render("Para pausar pulsa 'p'. (Puntuación: "+texto+")"+str(dificultad), True, YELLOW)  # PAUSA en display
        rectangulo_puntuacion = superficie_puntuacion.get_rect()
        rectangulo_puntuacion.center = (600, 10)
        screen.blit(superficie_puntuacion, rectangulo_puntuacion)
