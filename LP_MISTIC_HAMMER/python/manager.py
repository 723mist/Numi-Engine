import pylibary
from pylibary import *
import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import platform

def open_console():
    if platform.system() == "Windows":
        process = subprocess.Popen('start cmd', shell=True)
    else:
        process = subprocess.Popen(['gnome-terminal'])
        # subprocess.Popen(['xterm'])
    return process


def window_manager():

    if platform.system() == "Windows":
        workInPC = True
    else:
        workInPC = False

    # Test prg
    def errorLinuxMesseg():
        messagebox.showerror("Error!", "Error engine not starting in your OS!")

    if workInPC == True:
        print("work")
    else:
        errorLinuxMesseg() 



    # Colors
    color4 = "#2d333d"
    color5 = "#48688a"
    color6 = "#8787a5"

    # MainFrame
    Manager = Tk()
    Manager.title("Manager")
    Manager.geometry("602x598")
    Manager.config(bg="gray")
    Manager["bg"] = color5  
    Manager.resizable(False, False)

    # Fonts
    mfont = ("Arial", 24)

    # Style
    mstyle = tkk.Style()
    mstyle.configure("MHBu", font=mfont)

    # 
    def new():
        name_floder = tk_dial.askstring("Name", "Name for floder" , parent=Manager)
        path_fld = filedialog.askdirectory(title="Location")

        if path_fld:
            path_nw_fld = os.path.join(path_fld, name_floder)
            try:
                os.makedirs(path_fld)
                messagebox.showinfo("Title", f"A folder named {name_floder} project has been successfully created")
            except FileExistsError:
                messagebox.showinfo("Error INFO", f"A folder named '{name_floder}' already exists. Delete or choose another name")
            except Exception as e:
                messagebox.showerror("Error INFO!", f"Error: Failed to create floder/project. The next message will describe the error")
                messagebox.showerror("Error INFO!", f"Error information: {e}")

    # Button create
    BuNe = Button(text="New", command=new)
    BuNe.place(x=10, y=10)

    Manager.mainloop()


if __name__ == "__main__":
    open_console()
    window_manager()

    