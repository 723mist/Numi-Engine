from tkinter import *
from tkinter import ttk

saveDialog = Tk()
saveDialog.geometry("256x128")
saveDialog.title("Save and exit?")

def save():
    save_t = True

# button = ttk.Button(text="Save", command=save)
# button.place(relx=0.90365, rely=0.01, anchor=NW)

# button = ttk.Button(text="Don't save", command=dontsave)
# button.place(relx=0.90365, rely=0.01, anchor=NW)

# button = ttk.Button(text="Cancle", command=cancle)
# button.place(relx=0.90365, rely=0.01, anchor=NW)