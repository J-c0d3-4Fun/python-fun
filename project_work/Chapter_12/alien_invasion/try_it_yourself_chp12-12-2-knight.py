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