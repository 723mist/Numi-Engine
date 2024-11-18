import pylibary
from pylibary import *
import tkinter as tk
# import functions.centerWindow
# from functions.centerWindow import *
import subprocess
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

# Цвета
color = '#2d333d'
color2 = '#48688a'
color3 = '#8787a5'

Dashboard = Tk()
Dashboard.title("Py.name.MISTIC_HAMMER")
Dashboard.geometry("602x598")
Dashboard.config(bg="gray")
Dashboard.resizable(False, False)
Dashboard['bg'] = color
# center_window(Dashboard)

# Шрифт
tkfont = ('Poppins', 24)

# Стили
style = tkk.Style()
style.configure("MH.Button")

# Фрейм
frame = tk.Frame(Dashboard, bg=color3)
frame.place(relwidth=1, relheight=1)

# Функцыя
def new_prj_set():
    import new_settings_project

# Функцыя
def nsfldd():   
    defult_name_floder = tk_dial.askstring("Name", "Project name" , parent=Dashboard)
    path_to_floder = filedialog.askdirectory(title="Create floder")

    if path_to_floder:
        new_floder_path = os.path.join(path_to_floder, defult_name_floder)
        try:
            os.makedirs(new_floder_path)
            messagebox.showinfo("Успех", f"Папка '{defult_name_floder}' успешно создана!")
            import new_settings_project
        except FileExistsError:
            messagebox.showwarning("Ошибка", "Такая папка уже существует!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось создать папку: {e}")

    save_floder = "none" 

# Функцыя
def osfd():
    print("sfd")
    path_to_file = filedialog.askopenfilename(title="Open", filetypes=[("MHP", ".mhp")])

# Функцыя
def NBCreate():
    nsfldd()

# Кнопка New
NB = Button(text="New", command=NBCreate)
NB.place(x=525,y=30)

Dashboard.mainloop()