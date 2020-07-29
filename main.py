import tkinter as tk
import game as gm
from util import Vector
win = tk.Tk()
win.title('Destroy Rectangles')
win.resizable(False,False)
cnv = gm.Game(win)
cnv.pack()

win.mainloop()