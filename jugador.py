import pygame.sprite


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        vec = pygame.math.Vector2
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.pos = vec((20, 385))