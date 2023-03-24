import pygame
import math

class Fish:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("fish.png").convert_alpha()
        self.pos = pygame.math.Vector2(self.screen_width/2, self.screen_height/2)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 5
        self.angle = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        if keys[pygame.K_UP]:
            self.speed += 0.2
        if keys[pygame.K_DOWN]:
            self.speed -= 0.2

        return True

    def update(self):
        self.direction.rotate_ip(-self.angle)
        self.pos += self.direction * self.speed

        if self.pos.x > self.screen_width:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = self.screen_width

        if self.pos.y > self.screen_height:
            self.pos.y = 0
        elif self.pos.y < 0:
            self.pos.y = self.screen_height

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotated_image, self.pos - pygame.math.Vector2(rotated_image.get_rect().size) / 2)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        running = True
        while running:
            running = self.handle_events()

            self.update()
            self.draw(screen)

            pygame.display.flip()

        pygame.quit()

fish = Fish(800, 600)
fish.run()

