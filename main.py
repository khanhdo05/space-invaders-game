import pygame
import random
from sys import exit

class Game:
    def __init__(self):
        # Initialize PyGame
        pygame.init()
        
        # Game window
        self.WIDTH = 1600
        self.HEIGHT = int(self.WIDTH * 0.75)
        self.TITLE = "Space Invaders Game"
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        
        # Load images
        self.background_img = pygame.image.load('graphic/background.png')
        self.background_img = pygame.transform.scale(self.background_img, (self.WIDTH, self.HEIGHT))
        self.player_img = pygame.image.load('graphic/player.png')
        self.player_img = pygame.transform.scale(self.player_img, (self.WIDTH // 8, self.HEIGHT // 6))
        self.alien_img = pygame.image.load('graphic/alien.png')
        self.laser_img = pygame.image.load('graphic/laser.png')
        self.laser_img = pygame.transform.scale(self.laser_img, (self.WIDTH // 16, self.HEIGHT // 12))
        
        # Player properties
        self.player_x = self.WIDTH // 2 - (self.WIDTH / 16)
        self.player_y = self.HEIGHT - (self.HEIGHT / 4.8)
        
        # Laser properties
        self.laser_x = self.WIDTH // 2 - (self.WIDTH / 32)
        self.laser_y = self.HEIGHT - (self.WIDTH / 4.57142857)
        self.laser_speed = 20
        self.laser_state = "ready"
        
        # Score
        self.score = 0
        
        # Clock
        self.clock = pygame.time.Clock()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
        
    def draw(self):
        self.screen.blit(self.background_img, (0, 0))
        self.screen.blit(self.player_img, (self.player_x, self.player_y))
        self.screen.blit(self.laser_img, (self.laser_x, self.laser_y))
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(30)  # 30 frames per second
        pygame.quit()
        exit()

if __name__ == "__main__":
    game = Game()
    game.run()
