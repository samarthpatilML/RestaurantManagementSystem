
from mainwindow import MainWindow
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
