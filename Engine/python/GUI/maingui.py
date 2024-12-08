#Libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import tkinter.simpledialog as tk_dial
import time
import webbrowser

# Сolors
color1 = "#252426"
color2 = "#312f33"

global_prj_name_file = "Test"
global_p_name = f"{" project: "}{global_prj_name_file}"

# Window
wengine = Tk()
wengine.title(f"Engine {global_p_name}")
wengine.geometry("1024x600")

#Functions

#New
def New():
    p_name = tk_dial.askstring("Project name", "Project name" , parent=wengine)

#Open
def Open():
    path_to_file_project = filedialog.askopenfilename(title="Select a project", filetypes=[("Numi engine project", "*.nep")])

#Save
def Save():
    namef = "TestEngine"
    saveFirsIs = True
    print(saveFirsIs)
    if saveFirsIs == True:
        print("Save if")
        fileSave = asksaveasfile(initialfile = f"{namef}.nep", defaultextension = ".nep", filetypes=[("Numi engine project", "*.nep")])

        print(fileSave)
        saveFirsIs = False
        print(saveFirsIs)
    elif saveFirsIs == False:
        print("Save elif")

#SaveAs
def SaveAs():
    print("Save As")

#Exit
def Exit():
    wengine.destroy()

#Reload
def Reload():
    print("Reload")
    wengine.destroy()
    import Reloader
    time.sleep(0.5)
    #ReloadStep2()

#E_Floder
def Engine_floder():
    print("._.")

#Project configuration
def Tool_prj_config():
    print("Prj conf")
    pConfig = Tk()
    pConfig.geometry("520x450")
    pConfig.title("Project configuration")

    pConfig.resizable(False, False)
    pConfig.config(bg=color1)
    pConfig.mainloop()


#Engine configuration
def Config():
    print("Config func")
    w_config = Tk()
    w_config.geometry("600x250")
    w_config.title("Config")

    bc_test = ttk.Button(w_config, text="test button")
    bc_test.place(x=100, y=100)

    w_config.config(bg=color1)
    w_config.mainloop()

#Test window
def Test_Window():
    test_wnd = Tk()
    test_wnd.title("Test_Window")
    test_wnd.geometry("200x200")

    test_w_label = ttk.Label(test_wnd,  text="Test", background=color1, foreground="white")
    test_w_label.place(x=90, y=95)

    test_wnd.config(bg=color1)
    test_wnd.mainloop()

#Wiki
def Wiki():
    webbrowser.open("https://github.com/723mist/Numi-Engine/wiki")

#Bug report
def BugReport():
    webbrowser.open("https://github.com/723mist/Numi-Engine/issues")

#Game mini window
def GameMiniWindow():
    print("GameMiniWindow")

# MenuBar
menuBar = Menu(wengine, tearoff=0, background=color2, fg="white", border=0)

#ToolsInMenuBar
toolsInMenuUpBar = Menu()

#All menus
File = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
recent_prj = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Engine = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Edit = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
View = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Tool = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Window = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Build = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
Help = Menu(menuBar, tearoff=0, background=color2, fg="white", border=0)
#Up bar
menuBar.add_cascade(label="File", menu=File)
menuBar.add_cascade(label="Engine", menu=Engine)
menuBar.add_cascade(label="Edit", menu=Edit)
menuBar.add_cascade(label="View", menu=View)
menuBar.add_cascade(label="Build", menu=Build)
menuBar.add_cascade(label="Help", menu=Help)

#MenuFile
File.add_command(label="New", command=lambda:New())
File.add_command(label="Open", command=lambda:Open())
File.add_cascade(label="Recent projects", menu=recent_prj)
File.add_command(label="Save", command=lambda:Save())
File.add_command(label="Save as", command=lambda:SaveAs())
File.add_separator()
File.add_command(label="Reload", command=lambda:Reload())
File.add_command(label="Exit", command=lambda:Exit())

#MenuRecent
recent_prj.add_command(label="Test func 'Recent Projects 1'")
recent_prj.add_separator()
recent_prj.add_command(label="Test func 'Recent Projects 2'")
recent_prj.add_separator()
recent_prj.add_command(label="Test func 'Recent Projects 3'")

#MenuEngine
Engine.add_command(label="Engine floder", command=lambda:Engine_floder())
#Engine.add_command(label="Engine documentation")
Engine.add_separator()
#Engine.add_command(label="tearoff to 1", command=lambda:)
Engine.add_command(label="Config(Work)", command=lambda:Config())

#MenuEdit
Edit.add_command(label="Copy")
Edit.add_command(label="Cut")
Edit.add_command(label="Past")
Edit.add_separator()
Edit.add_command(label="Delete")

#MenuView
View.add_cascade(label="Tools", menu=Tool)
#In tool
Tool.add_command(label="Project configuration", command=lambda:Tool_prj_config())
View.add_cascade(label="Window", menu=Window)
#Window
Window.add_command(label="Game")
View.add_separator()
View.add_command(label="Test open window(Work)", command=lambda:Test_Window())

#MenuBuild
Build.add_command(label="Launch(Not working (under development))")
Build.add_command(label="Build and run(Not working (under development))")

#MenuHelp
Help.add_command(label="Wiki/Documentation", command=lambda:Wiki())
Help.add_command(label="Help")
Help.add_separator()
Help.add_command(label="Bug report!", command=lambda:BugReport())

#Interface
g_PanedWindow_Type_Horizontal = PanedWindow(orient ="horizontal")

label_ver = Label(text="Attention the engine is in an early stage. If you want to help or support, we are waiting for you on GitHub!")
label_ver.place(x=10, y=10)

#bt = ttk.Button(text="Test")
#bt.place(x=40, y=40)
#g_PanedWindow_Type_Horizontal.add(bt)

#bt1 = ttk.Button(text="Test2")
#bt1.place(x=40, y=40)
#g_PanedWindow_Type_Horizontal.add(bt1)

#g_PanedWindow_Type_Horizontal.pack(fill = BOTH, expand = True)
#g_PanedWindow_Type_Horizontal.configure(sashrelief = RAISED)

wengine.config(bg=color1, menu=menuBar)
wengine.mainloop()