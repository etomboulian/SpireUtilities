import tkinter as tk
from .frames import LoginFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Spire Tools')
        self.frame = LoginFrame(self)
        self.frame.pack()