from cgitb import text
import tkinter as tk
from tkinter import messagebox
from turtle import width

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
        self.orders_to_update = 0
        self.updatable_orders = None
        
        self.label_orders_to_update = tk.Label(self, text="Sales Orders to Update")

        self.check_orders_button = tk.Button(self, text="Check Orders", command=self.check_for_orders_to_update)
        self.update_orders_button = tk.Button(self, text="Update Orders", command=self.update_orders)
        self.back_button = tk.Button(self, text="Back to Main", command=lambda: self.parent.show_frame(self.parent.last_frame.__class__))
        self.field_orders_to_update = tk.Label(self, text=self.orders_to_update)

        self.label_orders_to_update.grid(row=0, column=0)
        self.field_orders_to_update.grid(row=0, column=1)

        self.back_button.grid(row=1, column=0, ipadx=10, padx=10)
        self.check_orders_button.grid(row=1, column=1, ipadx=10, padx=10)
        self.update_orders_button.grid(row=1, column=2, ipadx=10, padx=10)

        self.set_orders_to_update()

    def check_for_orders_to_update(self):
        self.set_orders_to_update()

    def set_orders_to_update(self):
        client = self.parent.company['api_client']

        all_orders = client.SalesOrders.all()
        self.updatable_orders = [order for order in all_orders if order.shippingAddress.shipId != "" and order.customerPO != order.shippingAddress.shipId] 
        
        self.orders_to_update = len(self.updatable_orders)
        self.field_orders_to_update.config(text=self.orders_to_update)

    def update_orders(self):
        if(self.orders_to_update > 0):
            updates = self.updatable_orders
            for order in updates:
                if order.customerPO != order.shippingAddress.shipId:
                    order.customerPO = order.shippingAddress.shipId
                    order.save()

            self.set_orders_to_update()
            self.field_orders_to_update.config(text=self.orders_to_update)
        else:
            messagebox.showinfo('Update Customer PO Function', 'Nothing to update') 
        
