# from functions.centerWindow import *
from pylibary import *
import tkinter as tk

# Цвета
color4 = '#2d333d'
color5 = '#48688a'
color6 = '#8787a5'

NEW_PROJECT = Tk()
NEW_PROJECT.title("New project")
NEW_PROJECT.geometry("366x196")
# center_window(NEW_PROJECT)

nframe = tk.Frame(NEW_PROJECT, bg=color6)
nframe.place(relwidth=1, relheight=1)
CNB = Button(text="Create")
CNB.place(x=280,y=15)

NEW_PROJECT.mainloop()