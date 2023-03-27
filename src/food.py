from object import Object
from constants import C
from getrandomitem import GetRandomItem
import pygame as pg
import random

FOOD_COLORS = [
        C.COLORS["FOOD_RED"],
        C.COLORS["FOOD_YELLOW"],
        C.COLORS["FOOD_GREEN"],
        ]

class Food(Object):
    def __init__(self, pos):
        super().__init__(pos)
        self.color = GetRandomItem(FOOD_COLORS)
        self.width = 10
        self.height = 2
        self.ChangeSize(random.uniform(0.8, 2.5))
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.is_wet = False

    def ChangeSize(self, num):
        self.width *= num
        self.height *= num

    def Update(self):
        if self.is_wet:
            self.yVel = .5
            #self.color = C.COLORS["WHITE"]
        else:
            if self.y >= C.WATER_LINE:
                self.is_wet = True
        super().Update()


