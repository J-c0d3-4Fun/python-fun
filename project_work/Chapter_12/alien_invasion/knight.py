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

