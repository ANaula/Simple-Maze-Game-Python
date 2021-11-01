import pygame


class Moving_Objects(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, direction, window, static_objects, speed=4):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.speed = speed
        self.static_objects = static_objects

        self.window = window
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 100, 0))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def movement(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

    def objects_collision(self):
        for static_object in self.static_objects:
            if self.rect.colliderect(static_object):
                return True

    def collision_with_objects(self):
        if self.objects_collision() or self.out_of_bounds():
            if self.direction == "left":
                self.direction = "right"
            elif self.direction == "right":
                self.direction = "left"
            elif self.direction == "up":
                self.direction = "down"
            elif self.direction == "down":
                self.direction = "up"

    def out_of_bounds(self):
        if self.rect.x < 0 or self.rect.right > self.window.get_width() or self.rect.y < 0 or self.rect.bottom > self.window.get_height():
            return True

    def update(self):
        self.movement()
        self.collision_with_objects()






