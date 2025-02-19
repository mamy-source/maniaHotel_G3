import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk

from pages import connexion


root = ThemedTk()
root.geometry("600x500")
#print(root.get_themes())  # Affiche tous les thèmes disponibles


root.set_theme("scidpurple")
style = ttk.Style()
style.theme_use('clam')
style.configure('Custom.TButton', background='#5a68f0',foreground='#fff',relief = 'flat',font=('arial', 12))

style.configure('Custom.TLabel', background = '#fff', font=('arial', 12))
style.configure('Custom.TFrame', background='#5a68f0', fg = 'light', font = ('arial', 12),relief='flat')
print(style.lookup('TLabel','fg'))



connexion.connection(root)
    

root.mainloop()

#lien repository https://github.com/mamy-source/maniaHotel_G3.git

