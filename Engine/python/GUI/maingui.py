from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import time
import webbrowser
import os

# colors
color1 = "#252426"
color2 = "#312f33"

# Window

wengine = Tk()
wengine.title("Engine")
wengine.geometry("1024x600")

#Functions

def Test_Window():
    test_wnd = Tk()
    test_wnd.title("Test_Window")
    test_wnd.geometry("200x200")

    test_w_label = ttk.Label(test_wnd,  text="Test", background=color1, foreground="white")
    test_w_label.place(x=90, y=95)

    test_wnd.config(bg=color1)
    test_wnd.mainloop()

def BugReport():
    webbrowser.open("https://github.com/723mist/Numi-Engine/issues?q=is%3Aissue+is%3Aopen+-label%3Abug")

def Exit():
    wengine.destroy()

def ReloadStep2():
    import maingui

def Reload():
    print("Reload")
    wengine.destroy()
    time.sleep(0.5)
    ReloadStep2()


def Config():
    print("Config func")
    w_config = Tk()
    w_config.geometry("600x250")
    w_config.title("Config")

    bc_test = ttk.Button(w_config, text="test button")
    bc_test.place(x=100, y=100)

    w_config.config(bg=color1)
    w_config.mainloop()

# MenuBar
menuBar = Menu(wengine, tearoff=0, background=color2, fg="white", border=0)

#ToolsInMenuBar
toolsInMenuUpBar = Menu()

File = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
recent_prj = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Engine = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Edit = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
View = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Build = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Help = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
menuBar.add_cascade(label="File", menu=File)
menuBar.add_cascade(label="Engine", menu=Engine)
menuBar.add_cascade(label="Edit", menu=Edit)
menuBar.add_cascade(label="View", menu=View)
menuBar.add_cascade(label="Build", menu=Build)
menuBar.add_cascade(label="Help", menu=Help)

#MenuFile
File.add_command(label="New")
File.add_command(label="Open")
File.add_cascade(label="Recent projects", menu=recent_prj)
File.add_command(label="Save")
File.add_command(label="Save as")
File.add_separator()
File.add_command(label="Reload(Work)", command=lambda:Reload())
File.add_command(label="Exit(Work)", command=lambda:Exit())

#MenuRecent
recent_prj.add_command(label="Test func 'Recent Projects 1'")
recent_prj.add_separator()
recent_prj.add_command(label="Test func 'Recent Projects 2'")
recent_prj.add_separator()
recent_prj.add_command(label="Test func 'Recent Projects 3'")

#MenuEngine
Engine.add_command(label="Engine floder")
Engine.add_command(label="Engine documentation")
Engine.add_separator()
#Engine.add_command(label="tearoff to 1", command=0)
Engine.add_command(label="Config(Work)", command=lambda:Config())

#MenuEdit
Edit.add_command(label="Copy")
Edit.add_command(label="Cut")
Edit.add_command(label="Past")
Edit.add_separator()
Edit.add_command(label="Delete")

#MenuView
View.add_command(label="Tools")
View.add_command(label="Window")
View.add_separator()
View.add_command(label="Test open window(Work)", command=lambda:Test_Window())

#MenuBuild
Build.add_command(label="Launch(Not working (under development))")
Build.add_command(label="Build and run(Not working (under development))")

#MenuHelp
Help.add_command(label="Help!")
Help.add_separator()
Help.add_command(label="Bug report!(Work)", command=lambda:BugReport())

wengine.config(bg=color1, menu=menuBar)
wengine.mainloop()