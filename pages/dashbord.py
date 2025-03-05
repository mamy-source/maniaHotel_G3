from ttkthemes import ThemedTk
from tkinter import ttk
import tkinter as tk 
from tkinter.ttk import Treeview
from PIL import Image, ImageTk

from .clear_frame import clear_data
from .customers.show_customer import Customers
#from .customers.add_customers import AddCustomer
from .rooms.main import Rooms
from .reservations.main import Reservations

class Dasboard:
    def __init__(self, window):
        self.window = window
        self.customers_page = Customers(window)
        self.rooms_page = Rooms(window)
        self.reservation_page = Reservations(window)
        #self.add_customer_page = AddCustomer(window)

        self.Frame3 = ttk.Frame(self.window,width=300,style='Custom.TFrame')
        self.Frame3.pack(side='left', padx=0, pady=0)

        self.image = Image.open("./image/but_1.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.label_maniaHotel = ttk.Label(self.Frame3, image=self.photo,style="Custom.TButton")
        self.label_maniaHotel.pack(pady=2)
        self.label_maniaHotel.image = self.photo

        self.image = Image.open("./image/but_2.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.btn_home = ttk.Button(self.Frame3, image=self.photo,style="Custom.TButton")
        self.btn_home.pack(pady=2)
        self.btn_home.image = self.photo

        self.image = Image.open("./image/but_3.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.btn_customer = ttk.Button(self.Frame3, image=self.photo,style="Custom.TButton",command=lambda:self.get_customer())
        self.btn_customer.pack(pady=2)
        self.btn_customer.image = self.photo

        self.image = Image.open("./image/but_4.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.btn_reservation = ttk.Button(self.Frame3, image=self.photo,style="Custom.TButton",command=lambda:self.get_reservation())
        self.btn_reservation.pack(pady=2)
        self.btn_reservation.image = self.photo

        self.image = Image.open("./image/but_5.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.btn_room = ttk.Button(self.Frame3, image=self.photo,style="Custom.TButton",command=lambda:self.get_rooms())
        self.btn_room.pack(pady=2)
        self.btn_room.image = self.photo

        self.image = Image.open("./image/but_6.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.btn_paiment = ttk.Button(self.Frame3, image=self.photo,style="Custom.TButton")
        self.btn_paiment.pack(pady=2)
        self.btn_paiment.image = self.photo

        self.image = Image.open("./image/but_7.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.btn_user = ttk.Button(self.Frame3, image=self.photo,style="Custom.TButton")
        self.btn_user.pack(pady=2)
        self.btn_user.image = self.photo

        self.image = Image.open("./image/but_8.png") 
        self.photo = ImageTk.PhotoImage(self.image)
        self.btn_log_out = ttk.Button(self.Frame3, image=self.photo,style="Custom.TButton")
        self.btn_log_out.pack(pady=2)
        self.btn_log_out.image = self.photo

    def get_customer(self):
        self.customers_page.show()   
        self.rooms_page.hide() 
        self.reservation_page.hide()      
        #self.add_customer_page.hide()

    def get_rooms(self):
        self.rooms_page.show()       
        self.customers_page.hide()
        self.reservation_page.hide()
        #self.add_customer_page.hide() 

    def get_reservation(self):
        self.reservation_page.show()
        self.customers_page.hide()
        self.rooms_page.hide() 




    



   

  
    
