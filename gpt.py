import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption
pygame.display.set_caption("My Game")

# Set the clock
clock = pygame.time.Clock()

# Set the player
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_size, player_size)

# Set the enemy
enemy_size = 50
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = 0
enemy_speed = 5
enemy_speed_multiplier = 1.1
enemy_speed_next = enemy_speed * enemy_speed_multiplier
enemy = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

# Set the font
font = pygame.font.SysFont(None, 36)

# Set the score
score = 0
prevScore = -1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle Keys
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_h]) and player.x > 0:
        player.x -= player_speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_l] and player.x < screen_width - player_size:
        player.x += player_speed
    elif keys[pygame.K_q]:
        pygame.quit()
        quit()


    # Move the enemy
    enemy.y += enemy_speed
    if enemy.y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = 0
        enemy.x = enemy_x
        enemy.y = enemy_y
        score += 1

    # Check for collision
    if player.colliderect(enemy):
        running = False

    # Fill the screen
    screen.fill((255, 255, 255))

    # Draw the player and enemy
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Set the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()

