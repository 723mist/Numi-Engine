from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

# colors
color1 = "#252426"

# Window
wengine = Tk()
wengine.title("Engine")
wengine.geometry("1024x600")

# MenuBar
menuBar = Menu()

toolsInMenuUpBar = Menu()

menuBar = Menu(wengine, tearoff=0)
File = Menu(tearoff=0)
Engine = Menu(tearoff=0)
Edit = Menu(tearoff=0)
View = Menu(tearoff=0)
Build = Menu(tearoff=0)
menuBar.add_cascade(label="File", menu=File)
menuBar.add_cascade(label="Engine", menu=Engine)
menuBar.add_cascade(label="Edit", menu=Edit)
menuBar.add_cascade(label="View", menu=View)
menuBar.add_cascade(label="Build", menu=Build)

#MenuFile
File.add_command(label="Create")
File.add_command(label="Open")
File.add_command(label="Save")
File.add_command(label="Exit")

#MenuEngine
Engine.add_command(label="Config")

#MenuEdit
Edit.add_command(label="Copy")
Edit.add_command(label="Cut")
Edit.add_command(label="Past")
Edit.add_command(label="Delete")

#MenuView
View.add_command(label="IDK :)")

#MenuBuild
Build.add_command(label="Build and run")
Build.add_command(label="Compil(Not work)")

wengine.config(bg=color1, menu=menuBar)
wengine.mainloop()