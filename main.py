import pygame
from States import States

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Simple Maze Game")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

Game = States(screen)

while True:
    Game.state_manager()


