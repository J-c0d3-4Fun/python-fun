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
                

    def change_screen(self):
        """Redraw the screen"""
        self.screen.fill(self.bg_color)
        self.clock.tick(60)
        self.rocket.blitme()
        pygame.display.flip()

    def _keydown(self,event):
        """Whenplayers press down a key the action will happen"""
        if event.key == pygame.K_RIGHT:

if __name__ == '__main__':
    game = RocketPower()
    game.surface()
