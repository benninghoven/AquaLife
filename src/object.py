class Object:
    def __init__(self, pos = None):
        if pos == None:
            self.x = 0
            self.y = 0
        else:
            self.x = pos[0]
            self.y = pos[1]
        self.xVel = 0
        self.yVel = .5 
        print("object spawned")

