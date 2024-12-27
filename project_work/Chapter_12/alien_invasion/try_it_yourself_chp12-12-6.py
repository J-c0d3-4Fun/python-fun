import pygame
import tiny_ship

class Surface:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,139)
        self.screen  = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Ship Shooting Game")
        self.clock = pygame.time.Clock()
        pygame.init()
        self.ship = tiny_ship.tship(self)

    
    def surface(self):
        """Creates the surface for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
    
    def keydown(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
    
    def keyup(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

if __name__ == '__main__':
    tship = Surface()
    tship.surface()