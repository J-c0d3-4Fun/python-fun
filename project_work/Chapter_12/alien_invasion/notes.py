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

# Images in Games

# To draw the player’s ship on the screen,
# we’ll load an image and then use the Pygame blit() method to draw the
# image.

# When you’re choosing artwork for your games, be sure to pay attention
# to licensing. The safest and cheapest way to start is to use freely
# licensed graphics that you can use and modify, from a website like https://
# opengameart.org.

# You can use almost any type of image file in your game, but it’s easiest
# when you use a bitmap (.bmp) file because Pygame loads bitmaps by default.
# Although you can configure Pygame to use other file types, some file types
# depend on certain image libraries that must be installed on your computer.
# Most images you’ll find are in .jpg or .png formats, but you can convert them
# to bitmaps using tools like Photoshop, GIMP, and Paint.

# bitmaps using tools like Photoshop, GIMP, and Paint.
# Pay particular attention to the background color in your chosen
# image. Try to find a file with a transparent or solid background that you
# can replace with any background color, using an image editor. Your games
# will look best if the image’s background color matches your game’s background
# color. Alternatively, you can match your game’s background to the
# image’s background.


# Pygame is efficient because it lets you treat all game elements like 
# rectangles (rects), even if they’re not exactly shaped like rectangles. 
# Treating an element as a rectangle is efficient because rectangles are simple geometric shapes. 
# When Pygame needs to figure out whether two game elements have collided, 
# for example, it can do this more quickly if it treats each object as a rectangle.

# When you’re working with a rect object, you can use the x- and
# y-coordinates of the top, bottom, left, and right edges of the rectangle, as
# well as the center, to place the object. You can set any of these values to
# establish the current position of the rect. 
# 
# When you’re centering a game
# element, work with the center, centerx, or centery attributes of a rect. When
# you’re working at an edge of the screen, work with the top, bottom, left, or
# right attributes. 
# 
# There are also attributes that combine these properties,
# such as midbottom, midtop, midleft, and midright. When you’re adjusting the
# horizontal or vertical placement of the rect, you can just use the x and y
# attributes, which are the x- and y-coordinates of its top-left corner. These
# attributes spare you from having to do calculations that game developers
# formerly had to do manually, and you’ll use them often.

# NOTE In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates
# increase as you go down and to the right. On a 1200×800 screen, the origin is at the
# top-left corner, and the bottom-right corner has the coordinates (1200, 800). These
# coordinates refer to the game window, not the physical screen.



# Refactoring: The _check_events() and _update_screen() Methods 
# A helper method does work inside a class but isn’t meant 
# to be used by code outside the class.
# In Python, a single leading underscore indicates a helper method.

# The _check_events() Method
# move the code that manages events to a separate method called
# _check_events(). This will simplify run_game() and isolate the event management
# loop. Isolating the event loop allows you to manage events separately
# from other aspects of the game, such as updating the screen.

# The _update_screen() Method


# Piloting the Ship

# Whenever the player presses a key, that 
# keypress is registered in Pygame as an event. 
# Each event is picked up by the pygame.event.get() method. 
# We need to specify in our _check_events() method what 
# kinds of events we want the game to check for. 
# Each keypress is registered as a KEYDOWN event.
# When Pygame detects a KEYDOWN event, we need to check whether the
# key that was pressed is one that triggers a certain action.

# we add an elif block to the event loop, to respond
# # when Pygame detects a KEYDOWN event
# The right arrow key is represented by
# pygame.K_RIGHT. If the right arrow key was pressed, we move the ship to the
# right by increasing the value of self.ship.rect.x by 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the to the right.
                    self.ship.rect.x += 1


# Allowing Continous Movement


# When the player holds down the right arrow key, we want the ship to continue
# moving right until the player releases the key. We’ll have the game detect a
# pygame.KEYUP event so we’ll know when the right arrow key is released; then
# we’ll use the KEYDOWN and KEYUP events together with a flag called moving_right
# to implement continuous motion.
# When the moving_right flag is False, the ship will be motionless. When
# the player presses the right arrow key, we’ll set the flag to True, and when the
# player releases the key, we’ll set the flag to False again.
# The Ship class controls all attributes of the ship, so we’ll give it an attribute
# called moving_right and an update() method to check the status of the
# moving_right flag. The update() method will change the position of the ship if
# the flag is set to True. We’ll call this method once on each pass through the
# while loop to update the position of the ship.


# Moving Both Left and Right

# In __init__(), we add a self.moving_left flag. In update(), we use two
# separate if blocks, rather than an elif, to allow the ship’s rect.x value to be
# increased and then decreased when both arrow keys are held down. This
# results in the ship standing still. If we used elif for motion to the left, the
# right arrow key would always have priority. Using two if blocks makes the
# movements more accurate when the player might momentarily hold down
# both keys when changing directions.



















