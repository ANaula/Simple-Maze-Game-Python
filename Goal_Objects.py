import pygame


class Goal_Objects(pygame.sprite.Sprite):
    def __init__(self, x, y, width=70, height=70):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

