from tkinter import *

editor_hammer = Tk()
editor_hammer.title("Editor/Hammer")
editor_hammer.geometry("1208x640") 
editor_hammer.resizable(width=False, height=False)
 
toolBarEditor = Menu()

tools_in_toolbar_options = Menu()

tools_in_toolbar = Menu()
tools_in_toolbar.add_command(label="New")
tools_in_toolbar.add_cascade(label="Options", menu= tools_in_toolbar_options)
tools_in_toolbar_options.add_command(label="Editor setings")
tools_in_toolbar.add_cascade(label="Exit", command=exit)

toolBarEditor.add_command(label="Save")
toolBarEditor.add_command(label="Open")
toolBarEditor.add_cascade(label="File", menu=tools_in_toolbar)
toolBarEditor.add_cascade(label="Edit")
toolBarEditor.add_cascade(label="View")

def exit():
    editor_hammer.destroy()
 
editor_hammer.config(menu=toolBarEditor)
 
editor_hammer.mainloop()