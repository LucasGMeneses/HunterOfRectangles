from color import COLORS
import random

class Life:
    def __init__(self, cnv, x,y,w, h,spr):
        self.cnv = cnv
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.spr = spr

    def draw(self): # draw life
        ax = self.x + self.w # position x2
        ay = self.y + self.h # position y2

        self.cnv.create_rectangle(self.x, self.y, ax, ay,fill="red") # fill bar
        self.cnv.create_rectangle(self.x, self.y, self.x + 400, ay,outline='snow') # outline bar

class Rect:
    def __init__(self, cnv, x, w, h):
        self.cnv = cnv
        self.x = x
        self.y = random.randrange(35,480-h) # random position y
        self.w = w
        self.h = h
        self.spr = random.randrange(len(COLORS)) # random color
        self.kill = False

    def draw(self): # draw rect
        ax = self.x + self.w # position x2
        ay = self.y + self.h # position y2
        self.cnv.create_rectangle(self.x, self.y, ax, ay,fill=COLORS[self.spr])
    
    def update(self): # logic rect
        self.x+=5
    
    def is_colision(self,obj): # check collision
        ax = self.x + self.w # position x2
        ay = self.y + self.h # position y2
        
        if (obj.x >= self.x) and (obj.x <= ax) and (obj.y >= self.y) and (obj.y <= ay):
            return True
        
        else:
            return False



