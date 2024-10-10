# импортирование библиотек
from pylibary import *

# создание окна
root = tk.Tk()

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
        else:
            tk_msg.showerror("ERROR", "A project with this name already exists!", parent=root)

btn_new = tkk.Button(frame, text='New', style='TButton', command=new_proj)
btn_new.place(x=125, y=150, anchor='center')

# запуск программы
root.mainloop()