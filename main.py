# INITIALIZATION
# Importing Libraries
import pygame
import random
from sys import exit
# Initialize PyGame
pygame.init()

# GAME WINDOW
WIDTH = 800
HEIGHT = 600
TITLE = "Space Invaders Game"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# GRAPHIC
## Load background image
background_img = pygame.image.load('graphic/background.png')
## Load player image

## Load alien image

## Load laser image

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
        if event.type == pygame.QUIT():
            running = False
    
    # GAME LOGIC
            
    # DRAWING
    # Renew screen
    screen.blit(background_img, (0, 0))
    # Draw the player

    # Draw the alien

    # Draw the laser

    # Draw the score

    # UPDATE DISPLAY
    pygame.display.flip()

    # CLOCK


# Clean up and quit
pygame.quit()
exit()