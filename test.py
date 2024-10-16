import python.pylibary
from python.pylibary import *
import python.functions.centerWindow
from python.functions.centerWindow import *
import subprocess

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
center_window(Dashboard)

# Шрифт
tkfont = ('Poppins', 24)

# Стили
style = tkk.Style()
style.configure('TButton', font=tkfont)

# Фрейм
frame = tk.Frame(Dashboard, bg=color2)
frame.place(relwidth=1, relheight=1)

Dashboard.mainloop()