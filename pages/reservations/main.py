import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
from controller import get_reservation

import tkinter as tk
from tkinter.ttk import Treeview
from PIL import Image, ImageTk

class Reservations:
    def __init__(self, window):
        self.window = window
        
        # Frame principal
        self.reservationsList = tk.Frame(window, bg='#fff')

        # Titre
        self.titre = tk.Label(self.reservationsList, text='Liste des Reservations', font=('arial', 13, 'bold'), fg='black', bg='#fff')
        self.titre.pack(pady=3)

        # Définition des colonnes
        columns = ("ID", "Customer", "Date R", "Entrer", "Sortir","Chambres","Payer", "Date")

        # Tableau (Treeview)
        self.table = Treeview(self.reservationsList, columns=columns, show="headings", height=15)
        self.table.pack(pady=5)

        # Configuration des colonnes
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=90, anchor="center")

        # Chargement des données
        self.load_data()

        # Frame des boutons
        #self.frame1 = tk.LabelFrame(window, width=900, height=600, bg='#fff')
        

        # Stocker les images dans l'objet
        self.btn_delete_img = ImageTk.PhotoImage(Image.open("./image/btn_sup.png"))
        self.btn_add_img = ImageTk.PhotoImage(Image.open("./image/btn_add.png"))
        self.btn_update_img = ImageTk.PhotoImage(Image.open("./image/btn_update.png"))

        # Boutons (s'assurer qu'ils sont dans le bon frame)
        self.btn_delete = tk.Button(self.reservationsList, image=self.btn_delete_img, bg='#fff', relief='flat', borderwidth=0)
        self.btn_delete.place(x=20, y=400)

        self.btn_add = tk.Button(self.reservationsList, image=self.btn_add_img, bg='#fff', relief='flat', borderwidth=0)
        self.btn_add.place(x=220, y=400)

        self.btn_update = tk.Button(self.reservationsList, image=self.btn_update_img, bg='#fff', relief='flat', borderwidth=0)
        self.btn_update.place(x=400, y=400)

        #frame pour afficher formulaire d'ajouter
        self.frame = tk.Frame(window , bg='#fff',width=100,height=470,borderwidth=0,relief='flat')
        self.lb_title = tk.Label(self.frame, text="Ajouter nouveaux Reservations",bg='#fff',font=('arial',14,'bold'),fg="black")
        self.lb_title.pack(pady=10, padx=0)
        
        self.lbname = ttk.Label(self.frame, text="Type:  ", style='Custom.TLabel')
        self.lbname.pack(pady=1, padx=0)
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.pack(pady=10, padx=50)

        self.lbEmail = ttk.Label(self.frame, text="Numero : ", style='Custom.TLabel')
        self.lbEmail.pack(pady=1, padx=0)
        self.Email_entry = ttk.Entry(self.frame)
        self.Email_entry.pack(pady=10, padx=50)

        self.lbAddress = ttk.Label(self.frame, text="Prix : ", style='Custom.TLabel')
        self.lbAddress.pack(pady=1, padx=0)
        self.Address_entry = ttk.Entry(self.frame)
        self.Address_entry.pack(pady=10, padx=50)

        #self.image = Image.open("./image/btn_add.png") 
        #self.photo = ImageTk.PhotoImage(self.image)
        #self.btn_submit = tk.Button(self.frame, image=self.photo,bg='#fff', relief='flat',
        #                            command=lambda:self.add())
        #self.btn_submit.pack(pady=10)
        #self.btn_submit.image = self.photo



    def load_data(self):
        
        reservations = get_reservation()  # Fonction correcte pour récupérer les données

        if not reservations:
            self.list_none = tk.Label(self.reservationsList, text='Aucune liste trouvée !', font=('arial', 13, 'bold'), fg='black', bg='#fff')
            self.list_none.pack(pady=2)
        else:
            for reservation in reservations:
                if reservation:
                    self.table.insert("", "end", values=(
                        reservation.get('id', ''),
                        reservation.get('customer_id', ''),  
                        reservation.get('resevation_date', ''),
                        reservation.get('check_in', ''),
                        reservation.get('check_out', ''),
                        reservation.get('room_id', ''),
                        reservation.get('paiments', ''),
                        reservation.get('created_at', ''),
                    ))

    def show(self):
        """Affiche la section 'rooms'"""
        self.reservationsList.pack(fill='both', side='right')
        self.frame.place(x=205, y=10)

        #self.frame1.pack(fill='both', side='bottom', padx=0, pady=5)

    def hide(self):
        """Cache la section 'rooms'"""
        self.reservationsList.pack_forget()
        self.frame.pack_forget()
        #self.frame1.pack_forget()


