import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from one2many import Customer, Item, Order, OrderLine, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

class Main_langas():
    def __init__(self):
        self = tk.Tk()
        self.title('Treeview demo')
        self.geometry('1220x750')

        def get_order_info():
            selected_item = self.order_tree.selection()
            details = self.order_tree.item(selected_item)
            print(details.get("values"))
            order_id = details.get("values")[0]
            for item in self.order_info_tree.get_children():
                self.order_info_tree.delete(item)
            order_info = session.query(OrderLine).filter_by(order_id=order_id).all()
            for order in order_info:
                self.order_info_tree.insert(parent='', index='end', text='', values=(order.id, order.item.name, order.item_id, order.amount, order.price, order.total_price))
            

        def get_selection():
            selected_item = self.customer_tree.focus()
            details = self.customer_tree.item(selected_item)
            customer_id = details.get("values")[0]
            for item in self.order_tree.get_children():
                self.order_tree.delete(item)
            orders = session.query(Order).filter_by(customer_id=customer_id).all()
            for order in orders:
                self.order_tree.insert(parent='', index='end', text='', values=(order.id, order.date))
            

        # item select
        def item_selected(event):
            for selected_item in self.customer_tree.selection():
                item = self.customer_tree.item(selected_item)
                record = item['values']
                # show a message
                # showinfo(title='Information', message=','.join(str(record)))

        def order_item_selected(event):
            for selected_item in self.order_tree.selection():
                item = self.order_tree.item(selected_item)
                record = item['values']
                # show a message
                # showinfo(title='Information', message=','.join(str(record)))



        self.f_customers = Frame()
        self.f_orders = Frame()
        self.f_order_info = Frame()
        self.b_get_selection = Button(border=5, text="Get selection", command=get_selection)
        self.b_get_order_info = Button(border=5, text="Get order information", command=get_order_info)
        

        self.f_customers.pack(side=TOP)
        self.b_get_selection.pack()
        self.f_orders.pack()
        self.b_get_order_info.pack()
        self.f_order_info.pack()


        # define columns
        customer_columns = ('id', 'first_name', 'last_name', 'email', 'address')
        self.customer_tree = ttk.Treeview(self.f_customers, columns=customer_columns, show='headings')

        # define headings
        self.customer_tree.heading('id', text='ID')
        self.customer_tree.heading('first_name', text='Name')
        self.customer_tree.heading('last_name', text='Surname')
        self.customer_tree.heading('email', text='Email')
        self.customer_tree.heading('address', text='Address')

        # add content to customer_tree
        customers = session.query(Customer).all()
        for customer in customers:
            self.customer_tree.insert(parent='', index='end', text='', values=(customer.id, customer.name, customer.surname, customer.email, customer.address))




        self.customer_tree.bind('<<TreeviewSelect>>', item_selected)
        self.customer_tree.pack(side=LEFT)


        # add a scrollbar
        self.customer_scrollbar = ttk.Scrollbar(self.f_customers, orient=tk.VERTICAL, command=self.customer_tree.yview)
        self.customer_tree.configure(yscroll=self.customer_scrollbar.set)
        self.customer_scrollbar.pack(side=RIGHT, fill=Y)

        # add order_tree
        order_columns = ('id', 'date')
        self.order_tree = ttk.Treeview(self.f_orders, columns=order_columns, show='headings')

        self.order_tree.heading('id', text='ID')
        self.order_tree.heading('date', text='Date')

        self.order_tree.bind('<<TreeviewSelect>>', order_item_selected)
        # add scrollbar
        self.order_scrollbar = ttk.Scrollbar(self.f_orders, orient=tk.VERTICAL, command=self.order_tree.yview)
        self.customer_tree.configure(yscroll=self.order_scrollbar.set)
        self.order_scrollbar.pack(side=RIGHT, fill=Y)
        self.order_tree.pack(side=LEFT)


        # add order_info tree
        order_columns = ('id', 'item_name', 'item_id', 'amount', 'price', 'total_price')
        self.order_info_tree = ttk.Treeview(self.f_order_info, columns=order_columns, show='headings')

        self.order_info_tree.heading('id', text='ID')
        self.order_info_tree.heading('item_name', text='Item name')
        self.order_info_tree.heading('item_id', text='Item id')
        self.order_info_tree.heading('amount', text='Amount')
        self.order_info_tree.heading('price', text='Price')
        self.order_info_tree.heading('total_price', text='Total price')

        self.order_info_tree.pack(side=LEFT)

        self.order_info_scrollbar = ttk.Scrollbar(self.f_order_info, orient=tk.VERTICAL, command=self.order_info_tree.yview)
        self.order_info_tree.configure(yscroll=self.order_info_scrollbar.set)
        self.order_info_scrollbar.pack(side=RIGHT, fill=Y)
        self.order_tree.pack(side=RIGHT)

        self.mainloop()

Main_langas()