import tkinter as tk
from ui import LoginFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Spire Tools')
        self.frame = LoginFrame(self)
        self.frame.pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()