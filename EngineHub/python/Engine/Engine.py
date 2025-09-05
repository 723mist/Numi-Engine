from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import time

def ofd():
    print("ofd = Open file dialog")
    filename = fd.askopenfilename()

def exit():
    print("Exit")
    editor_hammer.destroy()

def config():
    print("Config open")
    e_config = Tk()
    e_config.title("Editor/Hammer config")
    e_config.geometry("546x256")
    e_config.config(bg=color)

def opendashboard():
    print("Dashboard open")
    print("Hammer close")
    #import LP_MISTIC_HAMMER.python.manager
    editor_hammer.destroy()

def func_save():
    print("not work")

color = "#252426"

editor_hammer = Tk()
editor_hammer.title("Editor/Hammer")
editor_hammer.geometry("1208x640") 
editor_hammer.option_add("*tearOff", FALSE)
editor_hammer.config(bg=color)
#editor_hammer.resizable(width=False, height=False)

toolBarEditor = Menu()

tools_in_toolbar_options = Menu()

tools_in_toolbar = Menu()
tools_in_toolbar.add_command(label="New")
tools_in_toolbar.add_command(label="Open", command=ofd)
tools_in_toolbar.add_command(label="Save", command=func_save)
# tools_in_toolbar.add_cascade(label="Options", menu= tools_in_toolbar_options)
tools_in_toolbar.add_separator()
tools_in_toolbar.add_command(label="Open deshboard", command=opendashboard)
tools_in_toolbar.add_command(label="Exit", command=exit)


tool_bar_edit = Menu(toolBarEditor, tearoff=0)
tool_bar_edit.add_command(label="Copy")
# tool_bar_edit.add_command(label="Cut")
tool_bar_edit.add_command(label="Past")
tool_bar_edit.add_separator()
tool_bar_edit.add_command(label="Config", command=config)
toolBarEditor.add_cascade(label="File", menu=tools_in_toolbar)
toolBarEditor.add_cascade(label="Edit", menu=tool_bar_edit)
toolBarEditor.add_cascade(label="View")

editor_hammer.config(menu=toolBarEditor)

editor_hammer.mainloop()
