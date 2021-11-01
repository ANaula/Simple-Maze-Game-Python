import pygame

# Simple button class that checks whenever the mouse is hover over a button and when the mouse clicks on a button.


class Button:
    def __init__(self, window, x, y, width, height, text="", outline_color=None):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outline_color = outline_color
        self.font = pygame.font.Font("font/Lato-Regular.ttf", 30)
        self.button_surface = pygame.Surface((width, height))
        self.button_rect = self.button_surface.get_rect(center=(x, y))
        self.button_surface.fill((0, 100, 0))
        if text != "":
            self.text_surface = self.font.render(text, False, (255, 255, 255))
            self.text_rect = self.text_surface.get_rect(center=self.button_rect.center)
        if self.outline_color:
            self.border_surface = pygame.Surface((self.button_rect.width+4, self.button_rect.height+4))
            self.border_surface.fill(outline_color)
            self.border_rect = self.border_surface.get_rect(center=self.button_rect.center)

    def click_check(self, pos):
        if self.button_rect.collidepoint(pos):
            self.button_surface.fill((0, 45, 0))
            return True
        return False

    def hover_check(self, pos):
        if self.button_rect.collidepoint(pos):
            self.button_surface.fill((0, 60, 0))
        else:
            self.button_surface.fill((0, 100, 0))

    def draw(self):
        if self.outline_color:
            self.window.blit(self.border_surface, self.border_rect)
        self.window.blit(self.button_surface, self.button_rect)
        self.window.blit(self.text_surface, self.text_rect)

