import tkinter as tk
from .frames import LoginFrame

class App(tk.Tk):
    frames = {}

    def __init__(self):
        super().__init__()
        self.api_client = None
        self.frame = None
        self.last_frame = None
        self.company = {}

        self.title('Spire Tools')
        #self.show_frame(LoginFrame)
        self.frame = LoginFrame(self)
        self.frame.pack()
    
    def show_frame(self, frameType):
        # if there is already a frame then remove it
        if self.frame:
            self.last_frame = self.frame
            self.frame.pack_forget()

        # if we already have an instance of this frametype then show it
        if frameType in self.frames:
            self.frame = self.frames[frameType]
            
        # if not then create a new instanace of the frametype to show
        else:
            new_frame = frameType(self)
            self.frames[frameType] = new_frame
            self.frame = self.frames[frameType]
        
        # display the frame
        self.frame.pack()