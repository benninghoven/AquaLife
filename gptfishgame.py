import pygame
import random

# DOES NOT WORK

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 255)
FISH_COLOR = (255, 255, 0)
FOOD_COLOR = (255, 0, 0)
FISH_SIZE = 20
FOOD_SIZE = 10
FISH_SPEED = 3
FOOD_SPAWN_RATE = 50
SCORE_FONT_SIZE = 30
GAME_OVER_FONT_SIZE = 50

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the font for the score and game over messages
font = pygame.font.SysFont(None, SCORE_FONT_SIZE)
game_over_font = pygame.font.SysFont(None, GAME_OVER_FONT_SIZE)

# Define a class for the fish
class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = FISH_SIZE
        self.speed = FISH_SPEED

    def move(self):
        # Move the fish in the direction of the mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 0:
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

    def draw(self):
        # Draw the fish on the screen
        pygame.draw.circle(screen, FISH_COLOR, (int(self.x), int(self.y)), self.size)

    def collide_with_food(self, food):
        # Check if the fish collides with the food
        dx = self.x - food.x
        dy = self.y - food.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist < self.size + food.size:
            return True
        else:
            return False

# Define a class for the food
class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = FOOD_SIZE

    def draw(self):
        # Draw the food on the screen
        pygame.draw.circle(screen, FOOD_COLOR, (int(self.x), int(self.y)), self.size)

# Create a list to store the fish and food
fish = [Fish(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
food = []

# Initialize the score
score = 0

# Enter the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Spawn food at random intervals
    if random.randint(0, FOOD_SPAWN_RATE) == 0:
        food.append(Food(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

    # Move the fish
    for f in fish:
        f.move()

    # Check for collisions between fish and food
    for f in fish:
        for i, fd in enumerate(food):
            if f.collide_with_food(fd):
                # Remove the food and increase the score
                food.pop(i)
                score += 1

                # Create a new fish that is bigger and faster
                new_fish = Fish(f.x, f.y)
                new_fish.size = FISH_SIZE + score

