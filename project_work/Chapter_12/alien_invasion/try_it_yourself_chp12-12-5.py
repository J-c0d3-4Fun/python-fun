import pygame

class Blank:
    """Creates a blank screen"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (40,120,200)
        self.screen = pygame.display.set_mode([self.screen_height, self.screen_width])
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def surface(self):
        """Draws the blank screen inside the window"""
        while True:
            self._updated_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    self._keydown(event)
    
    def _updated_screen(self):
        """changes the screen"""
        self.screen.fill(self.bg_color)
        self.clock.tick(60)
        pygame.display.flip()


    def _keydown(self,event):
        """Keydown events from the user"""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
            print(event.key)
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
            print(event.key)
        elif event.key == pygame.K_UP:
            self.moving_up = True
            print(event.key)
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
            print(event.key)
    


    def _keyup(self,event):
        """Keyup events from the user"""


if __name__ == '__main__':
    b = Blank()
    b.surface()