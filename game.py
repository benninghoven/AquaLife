import pygame as pg

class Game:
    def __init__(self):
        pg.init()
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 40) #WHAT
        self.ticks= 0
        #self.player_pos = [self.screenW/2, self.screenH/2]
        #self.player_speed = 8
        #self.size = 10
        self.eventHandlersDict= {
            pg.QUIT: self.QuitGameEvent,
            pg.KEYDOWN: self.KeyDownEvent,
            pg.MOUSEBUTTONDOWN: self.MouseButtonDownEvent,
            # add more event types and associated functions as needed
        }
        self.entities = []

    def QuitGameEvent(self, event = None):
        print("quitting game")
        pg.quit()
        quit()

    def KeyDownEvent(self, event):
        key = pg.key.name(event.key)
        print(key)
        # MOVEMENT
        pass
        if key == 'q':
            self.QuitGameEvent()
        elif key == 'escape':
            print("MENU") #TODO

    def SpawnCookie(self, pos):
        print(f"spawning cookie at {pos}")
        self.entities.append((1, pos))

    def MouseButtonDownEvent(self, event):
        button = event.button
        pos = event.pos
        print(f"button pressed: {button}\t pos: {pos}")
        if button == 1:
            self.SpawnCookie(pos)

    def EventHandler(self):
        for event in pg.event.get():
            if event.type in self.eventHandlersDict:
                self.eventHandlersDict[event.type](event)

    def Update(self):
        self.ticks += 1
        for entity in self.entities:
            pass
        #print(entity)

    def DrawFrame(self):
        self.screen.fill((255, 255, 255))
        for entity in self.entities:
            pg.draw.circle(self.screen, (0, 165, 0), entity[1], 5)
        pg.display.update()


    def Run(self):
        while True:
            self.clock.tick(60)
            self.EventHandler()
            self.Update()
            self.DrawFrame()












