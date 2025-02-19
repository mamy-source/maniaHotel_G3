from ttkthemes import ThemedTk
from tkinter import ttk, messagebox
from .clear_frame import clear_data
from .dashbord import home_page

def connection(window):
    def Seconnecter():
        username = name.get()
        password = password_entry.get()

        try:
            if (username == "" and password == ""):
                messagebox.showerror("","veuiller remplire tous les champs")
                name.delete("0", "end")
                password_entry.delete("0","end")
            elif (username == "Admin" and password == "admin"):
                name.delete("0", "end")
                password_entry.delete("0","end")
                clear_data(window)
                home_page(window)
            else:
                messagebox.showwarning("","Erreur! nom ou mot de passe incorrect")
                name.delete("0", "end")
                password_entry.delete("0","end")
        except:
            messagebox.showwarning("","Erreur! veuiller remplire tous les champs")
            name.delete("0", "end")
            password_entry.delete("0","end")


    frame = ttk.Labelframe(window, relief='flat')
    frame.pack(fill="both",padx=50, pady=50)

    # Ajouter un widget avec ttk (Button, Label, etc.)
    label = ttk.Label(frame, text="Mania Hotel", font=("arial", 16))
    label.pack(pady=20)

    lbname = ttk.Label(frame, text="Username: ")
    lbname.pack(pady=1, padx=20)
    name = ttk.Entry(frame)
    name.pack(pady=10, padx=50)

    lbpassword = ttk.Label(frame, text="Password: ")
    lbpassword.pack(pady=1, padx=20)
    password_entry = ttk.Entry(frame, show='*')
    password_entry.pack(pady=10, padx=50)

 
    button = ttk.Button(frame, text="connecter",style='Custom.TButton',command=Seconnecter)
    button.pack(pady=10)