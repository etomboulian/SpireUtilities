import tkinter as tk

class LandingPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=100, pady=100)
        self.parent = parent
        
        self.copy_ship_id_to_cust_po_button = tk.Button(self, text="Copy Shipping IDs to Customer PO Field", command=self.copy_ship_id_to_cust_po)
        self.copy_ship_id_to_cust_po_button.pack()
    
    def copy_ship_id_to_cust_po(self):
        pass