import pygame
from tiny_ship import TShip

class Surface:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25,25,112)
        self.screen  = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Ship Shooting Game")
        self.clock = pygame.time.Clock()
        pygame.init()
        self.tship = TShip(self)

    
    def surface(self):
        """Creates the surface for the game."""
        while True:
            self.screen.fill(self.bg_color)
            self.clock.tick(60)
            self.tship.blitme()
            self.tship.update_vertical()
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    self.keydown(event)
                elif event.type == pygame.KEYUP:
                    self.keyup(event)

                    
    def keydown(self,event):
        if event.key == pygame.K_UP:
            self.tship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.tship.moving_down = True
    
    def keyup(self,event):
        if event.key == pygame.K_UP:
            self.tship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.tship.moving_down = False

if __name__ == '__main__':
    tship = Surface()
    tship.surface()