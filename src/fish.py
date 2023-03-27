from object import Object
from constants import C
import pygame as pg

class Fish(Object):
    def __init__(self, pos):
        super().__init__(pos)
        self.width = 10
        self.height = 10
        self.name = "Henry"
        self.color = C.COLORS["ORANGE"]
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def Update(self):
        self.x += self.xVel
        self.y += self.yVel


