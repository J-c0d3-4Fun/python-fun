import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        # Controlling Frame Rate
        self.clock  = pygame.time.Clock()
        # Instance of Settings function
        self.settings = Settings()

        # Make the game Full screen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height 


        # The object assigned to self.screen is called a surface. 
        # A surface in a Pygame is a part of the screen were a game element can be displayed.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # The call to Ship() requires one argument:a instance of AlienInvasiion. 
        # The self argument here refers to the current instance of AlienInvasion
        self.ship = Ship(self)

        # The group that holds the bullets:
        self.bullets = pygame.sprite.Group()
        # Get rid of bullets that have disappeared.

       


    def run_game(self):
        """Start the main loop fr the game"""
        while True:
            # To call amethod from within a class, 
            # use dot notation with the variable self and the name of the method.
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()
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
            # we add an elif block to the event loop, to respond
            # when Pygame detects a KEYDOWN event
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    # Helper Method to _check_events
    def _check_keydown_events(self,event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship ot the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        # call _fire_bullet() when the spacebar is pressed
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    # Helper Method to _check_events
    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            # Do not move to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Do not move to the left
            self.ship.moving_left = False
    
    # Helper Method to fire the bullets (_check_keydown_events)
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) <self.settings.bullets_allowed:
            # Make an instance of Bullet and call it new_bullet 
            new_bullet = Bullet(self)
            # Then add it to the group bullets using the add() method 
            # The add() method is similar to append(), but it’s written specifically for Pygame groups
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet position
        # update the position of the bullets on each pass through the while loop
        self.bullets.update()
        # use the copy() method to set up the for loop
        for bullet in self.bullets.copy():
            # check each bullet to see whether it has disappeared off the top of the screen
            if bullet.rect.bottom <= 0:
                # If it has, we remove it from bullets
                self.bullets.remove(bullet)
        # Show how many bullets currently exist in the game and verify
        # they’re being deleted when they reach the top of the screen
        print(len(self.bullets))
           

    def _update_screen(self):
        # Redraw the screen during each passs through the loop.
        # The fill() method acts on a surface and takes only one argument: a color.
        self.screen.fill(self.settings.bg_color)
        
        # The bullets.sprites() method returns a list of all sprites in the group bullets. 
        # To draw all fired bullets to the screen, we loop through the sprites in bullets and call draw_bullet() on each one
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # After filling the background the ship is drawn on the screen by calling 
        # ship.blitme(), so the ship appears on top of the background.
        self.ship.blitme()


        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()




