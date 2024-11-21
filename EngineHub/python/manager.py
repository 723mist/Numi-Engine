import pylibary
from pylibary import *
import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import platform
import sys

def open_console():
    if platform.system() == "Windows":
    #   process = subprocess.Popen('start cmd', shell=True)
        print("Windows")
    else:
    #     process = subprocess.Popen(['gnome-terminal'])
    #     process = subprocess.Popen(['xterm'])
    #     process = subprocess.Popen(['konsole'])
        print("Linux")
    # return process

def window_manager():

    python_path = [sys.executable,] + sys.path

    if platform.system() == "Windows":
        workInPC = True
    else:
        workInPC = False

    def errorLinuxMesseg():
        messagebox.showerror("Error!", "Error engine not starting in your OS!")

    def ProgramNotBuld():
        messagebox.showwarning("Attention!", "Attention! The engine is not finished, if you find a bug, write on the GitHub page")

    if workInPC == True:
        ProgramNotBuld()
        print("work")
    else:
        ProgramNotBuld()
        errorLinuxMesseg() 

    # Colors
    color4 = "#2d333d"
    color5 = "#48688a"
    color6 = "#8787a5"

    # MainFrame
    Manager = Tk()
    Manager.title("Manager v01 GitHub ")
    Manager.geometry("602x598")
    Manager.config(bg="gray")
    Manager["bg"] = color5  
    Manager.resizable(False, False) 

    def new():
        name_floder = tk_dial.askstring("Name", "Project name" , parent=Manager)
        path_fld = filedialog.askdirectory(title="Create floder")

        if path_fld:
            new_floder_path = os.path.join(path_fld, name_floder)
            path_fld2 = path_fld
            try:
                os.makedirs(new_floder_path)
                messagebox.showinfo("Great!", f"Folder '{name_floder}' successfully created!")
                # import new_settings_project
            except FileExistsError:
                messagebox.showwarning("Attention!", "Such folder exists! New folder will not be created. Choose another name or delete the folder")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create folder due to: {e}")

        save_floder = "none" 

    BuNe = Button(text="New", command=new)
    BuNe.place(x=10, y=10)

    Manager.mainloop()

if __name__ == "__main__":
    open_console()
    window_manager()
