# импортирование библиотек
import tkinter as tk
import tkinter.messagebox as tk_msg
import tkinter.simpledialog as tk_dial
import tkinter.font as tk_font
import tkinter.ttk as tkk
import os

# создание окна
root = tk.Tk()

# все папки, которые начинаются на "AntProj_"
def update_folders():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
    filtered_folders = [folder for folder in folders if folder.startswith('AntProj_')]

    listbox.delete(0, tk.END)

    for folder in filtered_folders:
        display_name = folder.replace('AntProj_', '', 1)
        listbox.insert(tk.END, display_name)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (800 // 2)
y = (screen_height // 2) - (600 // 2)

# цвета
color = '#808080'
color2 = '#606060'

# настройки окна
root.geometry(f'800x600+{x}+{y}')
root.resizable(width=False, height=False)
root.title('Ant Engine')
root['bg'] = color

# создание фрейма (на нем легче все размещать)
frame = tk.Frame(root, bg=color)
frame.place(relwidth=1, relheight=1)

# шрифт
path = 'Poppins/Poppins-Bold.ttf'
tkfont = ('Arial', 24)

# стили
style = tkk.Style()
style.configure('TButton', font=tkfont)

# текст
title = tk.Label(frame, text="Main Menu", font=tkfont, bg=color2)
title.place(relx=0.5, y=50, anchor='center')

# кнопка new
def new_proj():
    proj_name = tk_dial.askstring('Enter your project name', 'Enter your project name:', parent=root)
    if proj_name is not None and proj_name.strip():
        folder_name = f'AntProj_{proj_name}'

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            file_path = os.path.join(folder_name, 'main.txt')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('Это мой файл в новой папке.')
            tk_msg.showinfo("Project Created", f"Project '{proj_name}' created successfully!", parent=root)

            update_folders()
        else:
            tk_msg.showerror("ERROR", "A project with this name already exists!", parent=root)

btn_new = tkk.Button(frame, text='New', style='TButton', command=new_proj)
btn_new.place(x=125, y=150, anchor='center')

# cписок папок
folders_text = tk.Label(frame, text="Your Projects", font=tkfont, bg=color2)
folders_text.place(relx=0.2, y=225, anchor='n')

listbox = tk.Listbox(frame, width=25, height=10, font=('Arial', 16))
listbox.place(relx=0.2, y=275, anchor='n')

update_folders()

# запуск программы
root.mainloop()
