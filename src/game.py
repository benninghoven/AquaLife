import pygame as pg

from object import Object
from food import Food

MAX_ENTITIES = 64
WATER_LINE = 50

"""
Rectangles 
Circles 
Ellipses 
Lines
Polygons
"""

class Game:
    def __init__(self):
        pg.init()
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))
        self.background = pg.Surface((self.screenWidth,self.screenHeight))
        self.water = pg.Surface((self.screenWidth,self.screenHeight), pg.SRCALPHA)
        self.uiScreen = pg.Surface((self.screenWidth,self.screenHeight))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 40) #WHAT
        self.ticks= 0
        self.eventHandlersDict= {
            pg.QUIT: self.QuitGameEvent,
            pg.KEYDOWN: self.KeyDownEvent,
            pg.MOUSEBUTTONDOWN: self.MouseButtonDownEvent,
            # add more event types and associated functions as needed
        }
        self.objects= []

    def QuitGameEvent(self, event = None):
        print("quitting game")
        pg.quit()
        quit()

    def KeyDownEvent(self, event):
        key = pg.key.name(event.key)
        print(key)
        # MOVEMENT TODO
        pass
        if key == 'q':
            self.QuitGameEvent()
        elif key == 'escape':
            print("MENU") #TODO

    def MouseButtonDownEvent(self, event):
        button = event.button
        pos = event.pos
        print(f"button pressed: {button}\t pos: {pos}")
        if button == 1:
            self.objects.append(Food(pos))
            pass

    def EventHandler(self):
        for event in pg.event.get():
            if event.type in self.eventHandlersDict:
                self.eventHandlersDict[event.type](event)

    def Update(self):
        self.ticks += 1
        for object in self.objects:
            object.y += object.yVel
            object.yVel += .01

    def DrawFrame(self):
        pg.display.get_surface().blit(self.background,(0,0))  # Draw surface2
        for object in self.objects:
            pg.draw.circle(self.screen, object.color, (object.x, object.y), 10)

        pg.display.get_surface().blit(self.water,(0,WATER_LINE))  # Draw surface2
        pg.display.update()

    def DrawBackground(self):
        self.water.fill((0, 191, 255,128))
        self.background.fill((255, 255, 255))


    def Run(self):
        self.DrawBackground()
        while True:
            self.clock.tick(60)
            self.EventHandler()
            self.Update()
            self.DrawFrame()












