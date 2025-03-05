import tkinter as tk
from tkinter import ttk, StringVar, messagebox
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
from controller import get_customer, add_customer, update_customer, delete_customer
from ..rooms.main import Rooms



class Customers:
    def __init__(self, window):
        self.window = window

        #self.add_customer_page = AddCustomer(window)
        
        self.rooms_page = Rooms(window)
        # Frame principal
        self.customerList = tk.Frame(window, bg='#fff')

        # Titre
        self.titre = tk.Label(self.customerList, text='Liste des Clients', font=('arial', 13, 'bold'), fg='black', bg='#fff')
        self.titre.pack(pady=3)

        # Définition des colonnes
        columns = ("ID", "Nom", "Email", "Adresse", "Téléphone", "Date")

        # Tableau (Treeview)
        self.table = Treeview(self.customerList, columns=columns, show="headings", height=15)
        self.table.pack(pady=5)

        # Configuration des colonnes
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=100, anchor="center")

        # Chargement des données
        self.load_data()

        # Frame des boutons
        self.frame1 = tk.LabelFrame(window, width=900, height=600, bg='#fff')
        
        # Chargement des images (évite les recréations inutiles)
        self.btn_delete_img = ImageTk.PhotoImage(Image.open("./image/btn_sup.png"))
        self.btn_add_img = ImageTk.PhotoImage(Image.open("./image/btn_add.png"))
        self.btn_update_img = ImageTk.PhotoImage(Image.open("./image/btn_update.png"))

        # Boutons
        self.btn_delete = tk.Button(self.customerList, image=self.btn_delete_img, bg='#fff', relief='flat', borderwidth=0)
        self.btn_delete.place(x=20, y=400)

        self.btn_add = tk.Button(self.customerList, image=self.btn_add_img, bg='#fff', relief='flat', borderwidth=0,command=lambda:self.add_customer())
        self.btn_add.place(x=220, y=400)

        self.btn_update = tk.Button(self.customerList, image=self.btn_update_img, bg='#fff', relief='flat', borderwidth=0)
        self.btn_update.place(x=400, y=400)

        #frame pour afficher formulaire d'ajouter
        self.frame = tk.Frame(window , bg='#fff',width=100,height=470,borderwidth=0,relief='flat')
        self.lb_title = tk.Label(self.frame, text="Ajouter nouveaux Clients",bg='#fff',font=('arial',14,'bold'),fg="black")
        self.lb_title.pack(pady=10, padx=0)
        
        self.lbname = ttk.Label(self.frame, text="Enter Your Name: ", style='Custom.TLabel')
        self.lbname.pack(pady=1, padx=0)
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.pack(pady=10, padx=50)

        self.lbEmail = ttk.Label(self.frame, text="Enter Your Email: ", style='Custom.TLabel')
        self.lbEmail.pack(pady=1, padx=0)
        self.Email_entry = ttk.Entry(self.frame)
        self.Email_entry.pack(pady=10, padx=50)

        self.lbAddress = ttk.Label(self.frame, text="Enter Your Address: ", style='Custom.TLabel')
        self.lbAddress.pack(pady=1, padx=0)
        self.Address_entry = ttk.Entry(self.frame)
        self.Address_entry.pack(pady=10, padx=50)

        self.lbphone = ttk.Label(self.frame, text="Enter Your Phone: ", style='Custom.TLabel')
        self.lbphone.pack(pady=1, padx=0)
        self.phone_entry = ttk.Entry(self.frame)
        self.phone_entry.pack(pady=10, padx=50)

        #self.image = Image.open("./image/btn_add.png") 
        #self.photo = ImageTk.PhotoImage(self.image)
        #self.btn_submit = tk.Button(self.frame, image=self.photo,bg='#fff', relief='flat',
                                    #command=lambda:self.add())
        #self.btn_submit.pack(pady=10)
        #self.btn_submit.image = self.photo

        

    def load_data(self):
        """Charge la liste des clients"""
        customers = get_customer()  # Fonction qui récupère les données

        if not customers:
            self.list_none = tk.Label(self.customerList, text='Aucune liste trouvée !', font=('arial', 13, 'bold'), fg='black', bg='#fff')
            self.list_none.pack(pady=2)
        else:
            for customer in customers:
                if customer:
                    self.table.insert("", "end", values=(
                        customer.get('id', ''),
                        customer.get('name', ''),
                        customer.get('email', ''),
                        customer.get('address', ''),
                        customer.get('phone', ''),
                        customer.get('created_at', '')
                    ))

    def show(self):
        """Affiche la section 'customers'"""
        self.customerList.pack(fill='both', side='right', padx=10, pady=10)
        #self.frame1.place(x=270, y=430)
        self.frame.place(x=210, y=10)

    def hide(self):
        """Cache la section 'customers'"""
        self.customerList.pack_forget()
        #self.frame1.pack_forget()
        self.frame.pack_forget()
    
    def add(self,name,email,address,phone):
        """
        Ajoute un nouveau client avec effacement des champs.
        """
        customers = add_customer() #requette sql
        try:
            name = self.name_entry.get()
            email = self.Email_entry.get()
            address = self.Address_entry.get()
            phone = self.phone_entry.get()

            if not name or not email or not address or not phone:
                messagebox.showwarning("Avertissement", "Veuillez remplir tous les champs !")
                return
            customers
            messagebox.showinfo("Succès", "Client ajouté avec succès !")

            # Vider les champs après l'ajout
            self.name_entry.delete(0, tk.END)
            self.Email_entry.delete(0, tk.END)
            self.Address_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)

            self.frame.pack_forget()
            

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

   

