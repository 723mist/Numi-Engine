import pylibary
from pylibary import *
import pyconf
from pyconf import *
import functions.centerWindow
from functions.centerWindow import *


DASHBOARD = Tk()
DASHBOARD.title("Py.name.LME")
DASHBOARD.geometry("640x600")
DASHBOARD.config(bg="gray")
DASHBOARD.resizable(False, False)
center_window(DASHBOARD)

def new():
    import ENGINE
    DASHBOARD.destroy()

button = ttk.Button(text="New", command=new)
button.place(relx=0.90365, rely=0.01, anchor=NW)

DASHBOARD.mainloop()

