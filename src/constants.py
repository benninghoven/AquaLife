class Constants:
    def __init__(self):
        self.FPS = 60
        self.WIDTH = 800
        self.HEIGHT = 600

        self.FLOOR = self.HEIGHT * 0.9
        self.WATER_LINE = self.HEIGHT * 0.2

        self.COLORS ={
                "RED": (255,0,0),
                "GREEN": (0,255,0),
                "BLUE": (0,0,255),
                "AQUA": (0, 255, 255,50),
                "BLACK": (0, 0, 0),
                "WHITE": (255,255,255),
                "ORANGE": (255,165,0),
                "CORAL": (255, 127, 80),
                "FOOD_RED": (236, 38, 39),
                "FOOD_YELLOW": (255, 255, 102),
                "FOOD_GREEN": (46, 184, 46),
                }

C = Constants()
