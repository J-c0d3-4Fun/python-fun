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


# 12-3. Pygame Documentation: We’re far enough into the game now that you might want to look at some of the Pygame documentation. 
# The Pygame home page is at https://pygame.org, and the home page for the documentation is at https://pygame.org/docs. 
# Just skim the documentation for now. You won’t need it to complete this project, but it will help if you want to modify 
# Alien Invasion or make your own game afterward.



# 12-4. Rocket: Make a game that begins with a rocket in the center of the screen. 
# Allow the player to move the rocket up, down, left, or right using the four arrow keys. 
# Make sure the rocket never moves beyond any edge of the screen.


# 12-5. Keys: Make a Pygame file that creates an empty screen. 
# In the event loop, print the event.key attribute whenever a pygame.KEYDOWN 
# event is detected. Run the program and press various keys to see how Pygame responds.





