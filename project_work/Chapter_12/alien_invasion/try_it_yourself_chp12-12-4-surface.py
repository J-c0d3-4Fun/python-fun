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
