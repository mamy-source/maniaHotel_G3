from ttkthemes import ThemedTk
from tkinter import ttk
from .clear_frame import clear_data
from .dashbord import home_page

def connection(window):
    def navigate_to_home():
        clear_data(window)
        home_page(window)
        

    frame = ttk.Labelframe(window, borderwidth=2, relief='groove')
    frame.pack(fill="both",padx=50, pady=50)

    # Ajouter un widget avec ttk (Button, Label, etc.)
    label = ttk.Label(frame, text="Mania Hotel", font=("arial", 16))
    label.pack(pady=20)

    lbname = ttk.Label(frame, text="Username: ")
    lbname.pack(pady=1, padx=20)
    name = ttk.Entry(frame)
    name.pack(pady=10, padx=50)

    lbname = ttk.Label(frame, text="Password: ")
    lbname.pack(pady=1, padx=20)
    name_entry = ttk.Entry(frame)
    name_entry.pack(pady=10, padx=50)


    button = ttk.Button(frame, text="connecter", command=navigate_to_home)
    button.pack(pady=10)