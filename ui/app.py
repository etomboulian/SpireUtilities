import tkinter as tk
from .frames import LoginFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.api_client = None
        
        self.title('Spire Tools')
        self.show_frame(LoginFrame)
    
    def show_frame(self, frameType):
        self.frame = frameType(self)
        self.frame.pack()