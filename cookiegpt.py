import pygame
import random

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.5

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the cookie image
cookie_image = pygame.image.load("cookie.png").convert_alpha()

# Define a class for cookies
class Cookie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = -10
        self.width = cookie_image.get_width()
        self.height = cookie_image.get_height()

    def update(self):
        # Update the cookie's position and velocity
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY

        # If the cookie goes off the bottom of the screen, remove it
        if self.y > SCREEN_HEIGHT:
            cookies.remove(self)

    def draw(self):
        # Draw the cookie on the screen
        screen.blit(cookie_image, (self.x, self.y))

# Create a list to store the cookies
cookies = []

# Enter the main game loop
while True:
    pygame.time.Clock().tick(60)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Spawn a new cookie where the mouse was clicked
            x, y = pygame.mouse.get_pos()
            cookies.append(Cookie(x, y))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update and draw the cookies
    for cookie in cookies:
        cookie.update()
        cookie.draw()

    # Update the screen
    pygame.display.flip()

