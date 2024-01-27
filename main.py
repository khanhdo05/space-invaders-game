# main.py
# Importing Libraries
import pygame
import random
from sys import exit
# Initialize PyGame
pygame.init()

# Game Window
WIDTH = 800
HEIGHT = 600
TITLE = "Space Invaders Game"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)