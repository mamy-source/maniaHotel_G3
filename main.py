import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
from pages import connexion


root = ThemedTk()
root.geometry("500x400")
root.configure(bg = 'lightblue')
#print(root.get_themes())  # Affiche tous les thèmes disponibles

root.set_theme("scidpurple")
style = ttk.Style()
style.theme_use('clam')
style.configure('Custom.TButton', background='#5a68f0',foreground='#fff',relief = 'flat',font=('arial', 12))
style.configure('Custom.TLabel', background = '#fff', font=('arial', 12))
style.configure('Custom.TFrame', background='#5a68f0', fg = 'light', font = ('arial', 12),relief='flat')
print(style.lookup('TLabel','fg'))



'''def clear_frame():
    for widget in root.winfo_children(): #maka ny widget rehetra
        widget.destroy() #mamafa ny widget

def dashboard():
    clear_frame()
'''

connexion.connection(root)
    

# Lancer la boucle principale
root.mainloop()

