# INITIALIZATION
# Importing Libraries
import pygame
import random
from sys import exit
# Initialize PyGame
pygame.init()

# GAME WINDOW
WIDTH = 1600
HEIGHT = WIDTH * 0.75
TITLE = "Space Invaders Game"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# GRAPHIC
## Load background image
background_img = pygame.image.load('graphic/background.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
## Load player image
player_img = pygame.image.load('graphic/player.png')
player_img = pygame.transform.scale(player_img, (WIDTH // 8, HEIGHT // 6))
## Load alien image
alien_img = pygame.image.load('graphic/alien.png')
## Load laser image
laser_img = pygame.image.load('graphic/laser.png')
## Load and set Window Icon
icon_img = pygame.image.load('graphic/icon.png')
pygame.display.set_icon(icon_img)

# PLAYER PROPORTIES
# Position
player_x = WIDTH // 2 - (WIDTH / 16)
player_y = HEIGHT - (HEIGHT / 4.8)

# FONT

# AUDIO

# CLOCK

# SCORE
score = 0

# MAIN GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        # Detech quit action
        if event.type == pygame.QUIT:
            running = False
    
    # GAME LOGIC
            
    # DRAWING
    # Renew screen
    screen.blit(background_img, (0, 0))
    # Draw the player
    screen.blit(player_img, (player_x, player_y))
    # Draw the alien

    # Draw the laser

    # Draw the score

    # UPDATE DISPLAY
    pygame.display.flip()

    # CLOCK


# Clean up and quit
pygame.quit()
exit()