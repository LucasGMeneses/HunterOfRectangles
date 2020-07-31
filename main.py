import tkinter as tk
import game as gm

win = tk.Tk()
win.title('Hunter of Rectangles')
win.iconphoto(False, tk.PhotoImage(file='icon.png'))
win.resizable(False,False)
cnv = gm.Game(win)
cnv.pack()

win.mainloop()