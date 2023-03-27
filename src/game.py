import pygame as pg
import math

from object import Object
from food import Food
from fish import Fish
from constants import C

def FindClosestFood(foodList, fish):
    closestFood = None
    closestDistance = float("inf")
    for food in foodList:
        if food.is_wet == False:
            continue
        distance = math.sqrt((fish.x - food.x)**2 + (fish.y - food.y)**2)
        if distance < closestDistance:
            closestDistance = distance
            closestFood = food
    return closestFood

class Game:
    def __init__(self):
        pg.init()
        self.FONT = pg.font.Font(None, 50)
        self.screen = pg.display.set_mode((C.WIDTH, C.HEIGHT))
        pg.display.set_caption("AquaLife")
        self.background = pg.Surface((C.WIDTH, C.HEIGHT))
        self.background.fill(C.COLORS["WHITE"])
        self.water= pg.Surface((C.WIDTH, C.HEIGHT)).convert_alpha()
        self.water.fill(C.COLORS["AQUA"])
        self.clock = pg.time.Clock()
        self.eventHandlerDict= {
            pg.QUIT: self.QuitGameEvent,
            pg.KEYDOWN: self.KeyDownEvent,
            pg.MOUSEBUTTONDOWN: self.MouseButtonDownEvent,
            # add more event types and associated functions as needed
        }
        self.food_list = []
        self.fish = Fish((C.WIDTH/2,C.HEIGHT/2))

    def QuitGameEvent(self, event = None):
        print("quitting game")
        pg.quit()
        quit()

    def KeyDownEvent(self, event):
        key = pg.key.name(event.key)
        print(key)
        if key == 'q':
            self.QuitGameEvent()

    def MouseButtonDownEvent(self, event):
        button = event.button
        pos = event.pos
        print(f"button pressed: {button}\t pos: {pos}")
        if button == 1:
            self.SpawnFood(pos)

    def SpawnFood(self, pos):
            for i in range(1):
                self.food_list.append(Food(pos))



    def EventHandler(self):
        for event in pg.event.get():
            if event.type in self.eventHandlerDict:
                self.eventHandlerDict[event.type](event)

    def Process(self):
        self.textSurface = self.FONT.render(f"Food: {len(self.food_list)}", False,C.COLORS["BLACK"])
        closestFood = None
        if self.fish.hungry:
            closestFood = FindClosestFood(self.food_list,self.fish)
        if closestFood:
            print("MOVING")
            self.fish.Move((closestFood.x,closestFood.y))
            if self.fish.rect.colliderect(closestFood.rect):
                self.food_list.remove(closestFood)
                self.fish.Grow()

        for object in self.food_list:
            object.Update()

        self.fish.Update()


    def Draw(self):
        # BACKGROUND
        self.screen.blit(self.background,(0,0))
        # OBJECTS
        for object in self.food_list:
            pg.draw.rect(self.screen,object.color, object.rect)

        # PLAYER
        pg.draw.rect(self.screen,self.fish.color, self.fish.rect)
        # FOREGROUND
        self.screen.blit(self.water,(0,C.WATER_LINE))
        # UI
        self.screen.blit(self.textSurface,(C.WIDTH/2 - self.textSurface.get_width()/2,0))

        pg.display.update()

    def FrameCeiling(self):
            self.clock.tick(C.FPS)


    def Run(self):
        while True:
            #ticks = pg.time.get_ticks()
            self.EventHandler() #Event Looop
            self.Process()
            self.Draw() #Place shit on screen
            self.FrameCeiling()
