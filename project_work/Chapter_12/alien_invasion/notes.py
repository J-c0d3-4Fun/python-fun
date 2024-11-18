        # The object assigned to self.screen is called a surface. 
        # A surface in a Pygame is a part of the screen were a game element can be displayed.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Pygame creates a black screen by default
        # Set the background color.
        self.bg_color = (230, 230, 230)



# NOTE Pygame’s clock should help the game run consistently on most systems. If it makes the
# game run less consistently on your system, you can try different values for the frame
# rate. If you can’t find a good frame rate on your system, you can leave the clock out
# entirely and adjust the game’s settings so it runs well on your system.


# Colors in Pygame are specified as RGB colors: a mix of red, green, and
# blue.