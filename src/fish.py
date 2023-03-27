from object import Object
from constants import C
import pygame as pg
import math

class Fish(Object):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "Henry"
        self.color = C.COLORS["ORANGE"]
        self.speed = 2.0
        self.gravity = 0
        self.size = 1
        self.hungry = True
        self.digest_time = 10000

    def Grow(self):
        self.size += 1
        self.width += 1
        self.height += 1
        self.speed += 1
        self.hungry = False
        #self.Digest()

    
    def Digest(self):
        start_time = pg.time.get_ticks()  
        while pg.time.get_ticks() - start_time < self.digest_time:
            pass  # do nothing THIS IS THE ISSUE
        self.hungry = True  # set the local value to True

        print("1")
        pg.time.delay(self.digest_time)
        print("2")
        self.hungry = True


    def Move(self, pos):
        if pos == None:
            return
        # calculate the vector between the fish and the food
        dx = pos[0] - self.rect.centerx
        dy = pos[1] - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)

        if distance != 0:
            dx /= distance
            dy /= distance

        self.x += dx * self.speed
        self.y += dy * self.speed






