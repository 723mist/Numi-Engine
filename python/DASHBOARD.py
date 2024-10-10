import pylibary
from pylibary import *
import pyconf
from pyconf import *
import functions.centerWindow
from functions.centerWindow import *


DASHBOARD = Tk()
DASHBOARD.title("Py.name.MISTIC_HAMMER")
DASHBOARD.geometry("602x598")
DASHBOARD.config(bg="gray")
DASHBOARD.resizable(False, False)
center_window(DASHBOARD)

def new():

    proj_name = tk_dial.askstring('Enter your project name', 'Enter your project name:', parent=DASHBOARD)
    if proj_name is not None and proj_name.strip():
        folder_name = f'mhle_{proj_name}'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            file_path = os.path.join(folder_name, 'settings.hml')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('DevTest')
            tk_msg.showinfo("Project created, now open engine", f"Project '{proj_name}' created successfully!", parent=DASHBOARD)

            import ENGINE
            DASHBOARD.destroy()
        else:
            tk_msg.showerror("ERROR", "A project with this name already exists!", parent=DASHBOARD)

    

button = ttk.Button(text="New", command=new)
button.place(relx=0.90365, rely=0.01, anchor=NW)

DASHBOARD.mainloop()

