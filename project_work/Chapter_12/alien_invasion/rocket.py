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
