import pygame

class tship:
    """this will create a tiny rocket ship"""


    def __init__(self,tship):
        self.screen = tship.screen
        self.screen_rect = tship.screen.get_rect()
        self.image = pygame.image.load('images/tiny_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.moving_up = False
        self.moving_down = False

    def update_vertical(self):
        """moving the ship up and down"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1