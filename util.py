import os, constantes, time, pygame, sys

class Utilidades:
    def inicializar(self):
        pygame.init()
        # titulo ventana
        pygame.display.set_caption("STRATOS")


    def crearEventoIncrementarVelocidad(self):
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
        y -= 0.3 * velocidad  # fondo mas velocidad
        return y


    def gameOver(screen):
        # código para GAME OVER
        RED = (254, 0, 0)
        gameOverFont = pygame.font.SysFont('arial.ttf', 100)  # Fuente y tamaño final del juego
        gameOverSurf = gameOverFont.render("GAME OVER", True, RED)  # Game over content display
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (400, 300)  # posición de visualización
        screen.blit(gameOverSurf, gameOverRect)


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
