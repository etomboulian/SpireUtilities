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
        self.child_window = CopyShipIdToPo()

# New Window to handle the "Copy Shipping IDs to Customer PO Field Button" functions
class CopyShipIdToPo(tk.Toplevel):
    def __init__(self):
        super().__init__(padx=10, pady=10)

        self.label_orders_to_update = tk.Label(self, text="Sales Orders to Update")
        self.field_orders_to_update = tk.Label(self, text=self.orders_to_update)
        self.update_orders_button = tk.Button(self, text="Update Orders", command=self.update_orders)

        self.label_orders_to_update.grid(row=0, column=0)
        self.field_orders_to_update.grid(row=0, column=1)
        self.update_orders_button.grid(row=1, column=0, columnspan=2)

    @property
    def orders_to_update(self):
        return 0

    @orders_to_update.setter
    def get_updatable_orders(self):
        pass

    def update_orders(self):
        pass
        
