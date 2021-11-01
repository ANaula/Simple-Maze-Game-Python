import pygame

# User controlled object class. Checks to see for user input and resets its position if it collided with an obstacle.
# Inherited from the Sprite class in order to make updating, displaying, and checking for collision easier.


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((50, 50))
        self.image.fill((139, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = 5
        self.screen = screen

    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.right + self.speed <= self.screen.get_width():
            self.rect.x += self.speed
        if keys[pygame.K_a] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        if keys[pygame.K_w] and self.rect.y - self.speed >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom + self.speed <= self.screen.get_height():
            self.rect.y += self.speed

    def collision_with_objects(self, object_collision):
        if object_collision:
            self.rect.topleft = (self.x, self.y)

    def update(self, object_collision):
        self.user_input()
        self.collision_with_objects(object_collision)
