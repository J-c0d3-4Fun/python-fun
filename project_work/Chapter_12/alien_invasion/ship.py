import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting point."""
        # assign the screen to an attribute of Ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # access the screen's rect attribute using the get_rect() method and assign it to self.screen_rect
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving. 
        self.moving_right = False
        self.moving_left = False
    
    def update(self): 
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        # The code self.rect.right returns the x-coordinate of the right edge
        # of the ship’s rect. If this value is less than the value returned by
        # self.screen_rect.right, the ship hasn’t reached the right edge of the screen

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        # if the value of the left side of the rect is greater than 0,
        # the ship hasn’t reached the left edge of the screen
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        # After self.x has been updated, use the new value to 
        # update self.rect.x, which controls
        # the position of the ship
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)