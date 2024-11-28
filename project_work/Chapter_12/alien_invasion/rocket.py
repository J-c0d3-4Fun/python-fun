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
    
    def update(self):
        if self.moving_right:
            self += 1

    def blitme(self):
        """Draw the rocket ship at its current location"""
        self.screen.blit(self.image,self.rect)
