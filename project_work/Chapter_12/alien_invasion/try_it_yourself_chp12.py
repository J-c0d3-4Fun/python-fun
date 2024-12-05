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

import pygame
from rocket import Rocket

class RocketPower:
    """Class to manage the surface of the rocket power game"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (253, 165, 15)
        self.screen = pygame.display.set_mode()
        self.rocket = Rocket(self)
    
    def surface(self):
        """create the the surface"""
        while True:
            self.change_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    self._keydown(event)
                elif event.type == pygame.KEYUP:
                    self._keyup(event)
                

    def change_screen(self):
        """Redraw the screen"""
        self.screen.fill(self.bg_color)
        self.clock.tick(60)
        self.rocket.blitme()
        self.rocket.update_h()
        self.rocket.update_v()
        pygame.display.flip()
    

    def _keydown(self,event):
        """When players press down a key the action will happen"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
    
    def _keyup(self,event):
        """When players are not pressing down on a key the action will stop"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

if __name__ == '__main__':
    game = RocketPower()
    game.surface()

import pygame


class Rocket:
    """Adding the rocket to the game"""
    
    def __init__(self,rocket):
        self.screen = rocket.screen
        self.screen_rect = rocket.screen.get_rect()
        self.image = pygame.image.load('images/onlyrocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update_h(self):
        """horizontal movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        elif self.moving_left and self.rect.left > 0 :
            self.rect.x -= 1
    
    def update_v(self):
        """vertical movement"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        """Draw the rocket ship at its current location"""
        self.screen.blit(self.image,self.rect)


# 12-5. Keys: Make a Pygame file that creates an empty screen. 
# In the event loop, print the event.key attribute whenever a pygame.KEYDOWN 
# event is detected. Run the program and press various keys to see how Pygame responds.





