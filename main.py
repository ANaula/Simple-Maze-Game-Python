import pygame
from States import States

pygame.init()

# Window customization
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Simple Maze Game")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

Game = States(screen)

# Main loop
while True:
    Game.state_manager()


