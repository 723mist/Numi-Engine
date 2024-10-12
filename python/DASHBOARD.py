import pylibary
from pylibary import *
import functions.centerWindow
from functions.centerWindow import *
import subprocess

color = '#808080'
color2 = '#606060'

DASHBOARD = Tk()
DASHBOARD.title("Py.name.MISTIC_HAMMER")
DASHBOARD.geometry("602x598")
DASHBOARD.config(bg="gray")
DASHBOARD.resizable(False, False)
DASHBOARD['bg'] = color
center_window(DASHBOARD)

tkfont = ('Arial', 24)

# стили
style = tkk.Style()
style.configure('TButton', font=tkfont)

# создание фрейма (на нем легче все размещать)
frame = tk.Frame(DASHBOARD, bg=color)
frame.place(relwidth=1, relheight=1)    

# все папки, которые начинаются на "mhle_"
def update_folders():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
    filtered_folders = [folder for folder in folders if folder.startswith('mhle_')]

    listbox.delete(0, tk.END)

    for folder in filtered_folders:
        display_name = folder.replace('mhle_', '', 1)
        listbox.insert(tk.END, display_name)

def new():
    import Engine.Engine
    DASHBOARD.destroy()

    proj_name = tk_dial.askstring('Enter your project name', 'Enter your project name:', parent=DASHBOARD)
    if proj_name is not None and proj_name.strip():
        folder_name = f'mhle_{proj_name}'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            file_path = os.path.join(folder_name, 'settings.spmh')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("Create with MISTIC_HAMMER")
            tk_msg.showinfo("Project created, now open engine", f"Project '{proj_name}' created successfully!", parent=DASHBOARD)
        else:
            tk_msg.showerror("ERROR", "A project with this name already exists!", parent=DASHBOARD)


folders_text = tk.Label(frame, text="Your Projects", font=tkfont, bg=color2)
folders_text.place(relx=0.2, y=225, anchor='n')

listbox = tk.Listbox(frame, width=25, height=10, font=('Arial', 16))
listbox.place(relx=0.2, y=275, anchor='n')

update_folders()

button = ttk.Button(text="New", command=new)
button.place(relx=0.90365, rely=0.01, anchor=NW)

DASHBOARD.mainloop()
