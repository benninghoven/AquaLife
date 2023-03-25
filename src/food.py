from object import Object

class Food(Object):
    def __init__(self, pos):
        super().__init__(pos)
        self.size = 10
        self.color = (255, 215, 0)

