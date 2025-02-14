from ttkthemes import ThemedTk
from tkinter import ttk
from .clear_frame import clear_data


def home_page(window):
    
    clear_data(window)

     # frame 
    Frame2 = ttk.Frame(window, borderwidth=2, relief='groove',)
    Frame2.pack(fill='both', padx=2, pady=2)

 

    # frame  menu
    Frame3 = ttk.Labelframe(Frame2,width=300,style='Custom.TFrame')
    Frame3.pack(side='left', padx=2, pady=1)

    label_maniaHotel = ttk.Label(Frame3, text='Mania Hotel',font=('arial',14,'bold'), foreground='#fff', background='#5a68f0')
    label_maniaHotel.pack(pady=2)


    home = ttk.Button(Frame3, text='Accueil & Statistique', style= 'Custom.TButton')
    home.pack(pady=2)

    home = ttk.Button(Frame3, text='Gestion des Clients', style= 'Custom.TButton')
    home.pack(pady=2)

    home = ttk.Button(Frame3, text='Gestion des chambres', style= 'Custom.TButton')
    home.pack(pady=2)

    home = ttk.Button(Frame3, text='Gestion des réservations', style= 'Custom.TButton')
    home.pack(pady=2)

    home = ttk.Button(Frame3, text='Gestion des Paiements', style= 'Custom.TButton')
    home.pack(pady=2)

    home = ttk.Button(Frame3, text='Utilisateurs', style= 'Custom.TButton')
    home.pack(pady=2)

    home = ttk.Button(Frame3, text='Déconnexion', style= 'Custom.TButton')
    home.pack(pady=2)



    # frame who show all managements
    Frame4 = ttk.Labelframe(Frame2, borderwidth=2, width=250,relief='groove')
    Frame4.pack(fill='both', padx=2, pady=1, expand='yes')
    lbname = ttk.Label(Frame4, text="statistique ")
    lbname.pack(pady=1, padx=50)
    name = ttk.Entry(Frame4)
    name.pack(pady=2, padx=2)
    
