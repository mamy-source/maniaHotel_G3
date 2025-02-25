from ttkthemes import ThemedTk
from tkinter import ttk
from tkinter.ttk import Treeview
from PIL import Image, ImageTk

from .clear_frame import clear_data


def home_page(window):
    
    clear_data(window)

     # frame 
    Frame2 = ttk.Frame(window, borderwidth=2, relief='groove',)
    Frame2.pack(fill='both', padx=2, pady=2)

 

    # frame  menu
    Frame3 = ttk.Labelframe(Frame2,width=300,style='Custom.TFrame')
    Frame3.pack(side='left', padx=0, pady=0)

    image = Image.open("./image/but_1.png") 
    photo = ImageTk.PhotoImage(image)
    label_maniaHotel = ttk.Label(Frame3, image=photo,borderwidth=0, relief='flat')
    label_maniaHotel.pack(pady=2)
    label_maniaHotel.image = photo

    image = Image.open("./image/but_2.png") 
    photo = ImageTk.PhotoImage(image)
    home = ttk.Button(Frame3, image=photo, style= 'Custom.TButton')
    home.pack(pady=2)
    home.image = photo

    image = Image.open("./image/but_3.png") 
    photo = ImageTk.PhotoImage(image)
    home = ttk.Button(Frame3, image=photo, style= 'Custom.TButton')
    home.pack(pady=2)
    home.image = photo

    image = Image.open("./image/but_4.png") 
    photo = ImageTk.PhotoImage(image)
    home = ttk.Button(Frame3, image=photo, style= 'Custom.TButton')
    home.pack(pady=2)
    home.image = photo

    image = Image.open("./image/but_5.png") 
    photo = ImageTk.PhotoImage(image)
    home = ttk.Button(Frame3, image=photo, style= 'Custom.TButton')
    home.pack(pady=2)
    home.image = photo

    image = Image.open("./image/but_6.png") 
    photo = ImageTk.PhotoImage(image)
    home = ttk.Button(Frame3, image=photo, style= 'Custom.TButton')
    home.pack(pady=2)
    home.image = photo

    image = Image.open("./image/but_7.png") 
    photo = ImageTk.PhotoImage(image)
    home = ttk.Button(Frame3, image=photo, style= 'Custom.TButton')
    home.pack(pady=2)
    home.image = photo

    image = Image.open("./image/but_8.png") 
    photo = ImageTk.PhotoImage(image)
    home = ttk.Button(Frame3, image=photo, style= 'Custom.TButton')
    home.pack(pady=2)
    home.image = photo



    # frame who show all managements
    Frame4 = ttk.Labelframe(Frame2, width=250,relief='flat')
    Frame4.pack(fill='both', padx=2, pady=1, expand='yes')
    lbname = ttk.Label(Frame4, text="Liste des Clients ")
    lbname.pack(pady=0, padx=50)

  
    
