from cgitb import text
import tkinter as tk

# Main Landing page with utility functions accessible from
class LandingPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=20)
        self.parent = parent
        
        self.copy_ship_id_to_cust_po_button = tk.Button(self, text="Copy Shipping IDs to Customer PO Field", command=self.copy_ship_id_to_cust_po)
        self.copy_ship_id_to_cust_po_button.pack()
    
    def copy_ship_id_to_cust_po(self):
        self.parent.show_frame(CopyShipIdToPo)

# New Window to handle the "Copy Shipping IDs to Customer PO Field Button" functions
class CopyShipIdToPo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=10, pady=10)
        
        self.parent = parent
        self._orders_to_update = 0
        self._updatable_orders = []

        self.label_orders_to_update = tk.Label(self, text="Sales Orders to Update")
        self.field_orders_to_update = tk.Label(self, text=self.orders_to_update)
        self.update_orders_button = tk.Button(self, text="Update Orders", command=self.update_orders)
        self.back_button = tk.Button(self, text="Back to Main", command=lambda: self.parent.show_frame(self.parent.last_frame.__class__))

        self.label_orders_to_update.grid(row=0, column=0)
        self.field_orders_to_update.grid(row=0, column=1)
        self.update_orders_button.grid(row=1, column=1)
        self.back_button.grid(row=1, column=0)

    @property
    def orders_to_update(self):
        client = self.parent.api_client
        return self._orders_to_update

    def update_orders(self):
        pass
        
