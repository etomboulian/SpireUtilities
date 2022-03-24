import tkinter as tk
from tkinter import messagebox

from ui.frames.main_frame import LandingPage

class CompanySelectionFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.set_widgets()

    def set_widgets(self):
        self.set_company_select_listbox()
        self.set_select_button()

    def set_company_select_listbox(self):
        company_list = self.parent.api_client.Companies.list()
        company_list = [company.name for company in company_list]
        companies = tk.StringVar(value=company_list)
        self.company_selection_listbox = tk.Listbox(self.parent, selectmode=tk.SINGLE, listvariable=companies)
        self.company_selection_listbox.pack()

    def set_select_button(self):
        self.select_button = tk.Button(text='Select', command=self.set_selected_company)
        self.select_button.pack()

    def set_selected_company(self):
        selected_index = self.company_selection_listbox.curselection()
        selected_company = self.company_selection_listbox.get(selected_index[0])

        self.company_selection_listbox.pack_forget()
        self.select_button.pack_forget()
        self.parent.frame.pack_forget()
        self.parent.frame.destroy()
        
        try:
            self.parent.company['api_client'] = self.parent.api_client.Company(selected_company)
            self.parent.frame = LandingPage(self.parent)
            self.parent.frame.pack()
        except Exception as e:
            messagebox.showerror("Company Selection Error", e)