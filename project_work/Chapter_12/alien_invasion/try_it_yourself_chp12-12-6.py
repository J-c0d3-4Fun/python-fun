import pygame

class Surface:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200,40,130)
        self.screen  = pygame.display.set_mode(self.screen_width, self.screen_height)
        pygame.display.set_caption("Ship Shooting Game")
        self.clock = pygame.time.Clock()
        pygame.init()