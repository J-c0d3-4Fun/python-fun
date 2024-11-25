# TRY IT YOURSELF



# 12-1. Blue Sky: Make a Pygame window with a blue background.

import sys
import pygame

class Screen:

    def __init__(self):
        """Set the settings for the background color to be blue"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,250)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Blue Background")
        self.clock  = pygame.time.Clock()
        pygame.init()

    def create_bg(self):
        """Create the screen with the blue background"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    sc = Screen()
    sc.create_bg()


# 12-2. Game Character: Find a bitmap image of a game character 
# you like or convert an image to a bitmap. 
# Make a class that draws the character at the center of the screen, 
# then match the background color of the image to 
# the background color of the screen or vice versa.

import pygame


class Knight:
    """A class to control the knight"""

    def __init__(self, player):
        self.screen = player.screen
        self.screen_rect = player.screen.get_rect()
        self.image = pygame.image.load('images/knight.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the knight at its current location"""
        self.screen.blit(self.image,self.rect)
# Separate File

import pygame
import sys
from knight import Knight


class Screen:

    def __init__(self):
        """Set the settings for the background color to be blue"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (110,177,196)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Blue Background")
        self.clock  = pygame.time.Clock()
        pygame.init()
        self.knight = Knight(self)

    def create_bg(self):
        """Create the screen with the blue background"""
        while True:
            self.change_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def change_screen(self):
        self.screen.fill(self.bg_color)
        self.clock.tick(60)
        self.knight.blitme()
        pygame.display.flip()




if __name__ == '__main__':
    sc = Screen()
    sc.create_bg()








