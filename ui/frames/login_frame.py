import tkinter as tk
from .main_frame import LandingPage

class LoginFrame(tk.Frame):
    OUTSIDE_PADDING = 20
    PADDING = 2

    BUTTON_SEPARATOR = 10

    def __init__(self, master):
        super().__init__(master, pady=self.OUTSIDE_PADDING, padx=self.OUTSIDE_PADDING)

        self.parent = master
        
        self.hostname_field_label = tk.Label(self, text="Hostname: ")
        self.hostname_field = tk.Entry(self)
        self.hostname_field_label.grid(row=0, column=0, pady=(self.PADDING))
        self.hostname_field.grid(row=0, column=1, pady=(self.PADDING))

        self.username_field_label = tk.Label(self, text='Username: ')
        self.username_field = tk.Entry(self)
        self.username_field_label.grid(row=1, column=0, pady=(self.PADDING))
        self.username_field.grid(row=1, column=1, pady=(self.PADDING))

        self.password_field_label = tk.Label(self, text="Password: ")
        self.password_field = tk.Entry(self, show='*')
        self.password_field_label.grid(row=2, column=0, pady=(self.PADDING))
        self.password_field.grid(row=2, column=1, pady=(self.PADDING))

        self.login_button = tk.Button(self, text="Log In", command=self.try_login)
        self.cancel_button = tk.Button(self, text="Cancel", command=self.quit)

        self.login_button.grid(row=3, column=0, pady=(self.BUTTON_SEPARATOR, self.PADDING), columnspan=2, sticky='NEWS')
        self.cancel_button.grid(row=4, column=0, pady=(self.PADDING, self.PADDING), columnspan=2, sticky='NEWS')

    def try_login(self):
        hostname = self.hostname_field.get()
        username = self.username_field.get()
        password = self.password_field.get()

       
        try:
            from spire import ApiClient
            self.parent.api_client = ApiClient(hostname, username, password)
            if (self.parent.api_client.authenticated):
                self.parent.frame.pack_forget()
                self.parent.frame.destroy()
                # send the user to the landing page
                self.parent.show_frame(LandingPage)
            else:
                # TODO: pass any exceptions received at lower layers up to the GUI
                pass
        except Exception as e:
            popup_window = tk.Tk()
            popup_window.wm_title("Login Error")
            popup_window.geometry("300x200")
            message = e
            label = tk.Label(popup_window, text=message, wraplength=300, justify=tk.LEFT)
            label.pack()
            close_button = tk.Button(popup_window, text="Ok", command=popup_window.destroy)
            close_button.pack()
            
            print(e)

    def quit(self):
        self.parent.destroy()

