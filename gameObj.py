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

    def draw(self):
        ax = self.x + self.w
        ay = self.y + self.h
        self.cnv.create_rectangle(self.x, self.y, ax, ay,fill="red")
        self.cnv.create_rectangle(self.x, self.y, self.x + 400, ay,outline='snow')

class Rect:
    def __init__(self, cnv, x, w, h):
        self.cnv = cnv
        self.x = x
        self.y = random.randrange(35,480-h)
        self.w = w
        self.h = h
        self.spr = random.randrange(len(COLORS))
        self.kill = False

    def draw(self):
        ax = self.x + self.w
        ay = self.y + self.h
        self.cnv.create_rectangle(self.x, self.y, ax, ay,fill=COLORS[self.spr])
    
    def update(self):
        self.x+=5
    
    def is_colision(self,obj):
        ax = self.x + self.w
        ay = self.y + self.h
        if (obj.x >= self.x) and (obj.x <= ax) and (obj.y >= self.y) and (obj.y <= ay):
            return True
        else:
            return False



