from constants import C
import pygame as pg

class Object:
    def __init__(self, pos = None):
        if pos == None:
            self.x = 0
            self.y = 0
        else:
            self.x = pos[0]
            self.y = pos[1]
        self.xVel = 0
        self.yVel = 0
        self.gravity = .05
        self.width = 10
        self.height = 10
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def Update(self):
        self.x += self.xVel
        self.y += self.yVel
        self.yVel += self.gravity
        if self.y >= C.FLOOR:
            self.y = C.FLOOR
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

