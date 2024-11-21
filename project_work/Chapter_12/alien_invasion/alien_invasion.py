import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        # Controlling Frame Rate
        self.clock  = pygame.time.Clock()
        # Instance of Settings function
        self.settings = Settings()
        # The object assigned to self.screen is called a surface. 
        # A surface in a Pygame is a part of the screen were a game element can be displayed.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # The call to Ship() requires one argument:a instance of AlienInvasiion. 
        # The self argument here refers to the current instance of AlienInvasion
        self.ship = Ship(self)



    def run_game(self):
        """Start the main loop fr the game"""
        while True:
            # To call amethod from within a class, 
            # use dot notation with the variable self and the name of the method.
            self._check_events()
            self._update_screen()
           
            # instance of the class Clock
            # the tick() method takes one argument: the fram rate for the game.
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        # An event is an action that the user performs while playing the game.
        # i.e. pressing a key or mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        # Redraw the screen during each passs through the loop.
        # The fill() method acts on a surface and takes only one argument: a color.
        self.screen.fill(self.settings.bg_color)
            
        # After filling the background the ship is drawn on the screen by calling 
        # ship.blitme(), so the ship appears on top of the background.
        self.ship.blitme()


        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()




