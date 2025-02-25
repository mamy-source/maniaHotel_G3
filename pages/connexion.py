from ttkthemes import ThemedTk
import tkinter as tk 
from tkinter import ttk, messagebox
from .clear_frame import clear_data
from .dashbord import home_page
from controller import *
from PIL import Image, ImageTk

def connection(window):
    name_entry = None
    password_entry = None
    def Seconnecter():
        
        try:
            name = name_entry.get()
            mdp = password_entry.get()
            if checkUser(username="",password=""):
                messagebox.showerror('','veiller remplire tous le champs')
                name_entry.delete("0", "end")
                password_entry.delete("0", "end")
                
            elif checkUser(username=name,password=mdp):
                clear_data(window)
                home_page(window)
            else:
                messagebox.showerror('','nom ou mot de pass incorrect')
                name_entry.delete("0", "end")
                password_entry.delete("0", "end")
        except Exception as e:

            messagebox.showwarning("",f"{e}")
            name_entry.delete("0", "end")
            password_entry.delete("0", "end")

    frame = ttk.Labelframe(window, style='Custom.TLabel')
    frame.pack(fill="both",padx=50, pady=50)

    image = Image.open("./image/logo.png") 
    photo = ImageTk.PhotoImage(image)

    label = ttk.Label(frame, image=photo, style='Custom.TLabel')
    label.pack(pady=20)
    label.image = photo 



    lbname = ttk.Label(frame, text="Username: ", style='Custom.TLabel')
    lbname.pack(pady=1, padx=0)
    name_entry = ttk.Entry(frame)
    name_entry.pack(pady=10, padx=50)

    lbpassword = ttk.Label(frame, text="Password: ", style='Custom.TLabel')
    lbpassword.pack(pady=1, padx=20)
    password_entry = ttk.Entry(frame, show='*')
    password_entry.pack(pady=10, padx=50)

    img = Image.open("./image/button_seco1.png") 
    login = ImageTk.PhotoImage(img)
    button = ttk.Button(frame, image=login,style='Custom.TLabel',command=lambda:Seconnecter())
    button.pack(pady=10)
    label.img = login 