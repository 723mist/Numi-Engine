import subprocess
import platform

def open_console():
    if platform.system() == "Windows":
        subprocess.Popen('start cmd', shell=True)
    else:
        subprocess.Popen(['gnome-terminal'])
        # subprocess.Popen(['xterm'])

if __name__ == "__main__":
    open_console()
    import manager
