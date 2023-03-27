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

    def Update(self):
        self.y += self.yVel
        self.yVel += self.gravity
        if self.y >= C.FLOOR:
            self.y = C.FLOOR
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

