import pygame

# The non-moving obstacle class. It inherits from the sprite class to make updating, displaying, and collision checking
# easier.


class Static_Objects(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 100, 0))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
