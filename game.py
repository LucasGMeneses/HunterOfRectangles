from tkinter import Canvas
from gameObj import *
import random as rdm

FPS = 30
DELAY = 1000//FPS
time = 0
score = 0
stop = False
class Game(Canvas):
    def __init__(self, mst):
        super().__init__()
        self.mst = mst
        self["width"]= 800
        self["height"]= 480
        self["bg"]= '#000000'
        mst.bind_all('<Key>', self.inputs)
        mst.bind_all('<1>', self.inputs)
        self.rectangles = []
        self.life = Life(self,180,10,400,25,3) # bar life
        self.tic()
    
    def tic(self):
        if stop is False: # game running
            self.update()
            self.draw()
        else: # game over
            self.create_text(400,240,fill='snow',font=("Times", "24", "bold"), text='GAME OVER') # screen Game Over
            self.create_text(400,270,fill='gray70',font=("Times", "18", "normal"),text='Press key Enter to restart game or press key Esc to quit') 
        self.after(DELAY, self.tic)

    def draw(self):
        
        self.delete('all')
        self.create_text(160,25,fill='snow', font=("Times", "13", "bold"), text='Life') #title life
        self.create_text(700,25,fill='snow', font=("Times", "13", "bold"), text='Score: '+ str(score)) # score
        self.life.draw()
        
        for rect in self.rectangles:
            if rect.kill is False:
                rect.draw()

    def inputs(self, e):
        global score
        if e.num == 1: #click
            for rect in self.rectangles:
                if rect.is_colision(e) is True:
                    score +=1
                    rect.kill = True

        if e.keysym == 'Escape': # quit game
            self.mst.destroy()
        if e.keysym == 'Return' and stop is True: # reset game 
            self.reset()

    def update(self):
        global time,stop
        flg = False
        if time <= 0:
            self.rectangles.append(Rect(self,0,32,32))
            time = rdm.randrange(5,20)
        time-=1

        for rect in self.rectangles:
            if rect.x <= 800:
                rect.update()
            else:
                if rect.kill is False:
                    flg = True
                else:
                    flg = False
        
        if flg == True:
            self.life.w -= 5
            self.rectangles.pop(0)
            flg = False

        if self.life.w < 0:
            self.life.w = 400
            self.rectangles.clear()
            stop = True

    def reset(self):
        global score,time,stop
        score = 0
        self.life.w = 400
        stop = False
