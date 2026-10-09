import tkinter as tk
from tkinter import ttk

def stworz_okno():
    root = tk.Tk()
    root.title("WARZYWNIAK")
    root.geometry("1050x850")
    root.config(bg="#acffb5")

    # Styl dla tabeli produktów
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", rowheight=26, font=("Arial", 10))
    style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

    # Górny pasek ze stanem konta
    saldo_bar = tk.Label(root, text="Stan konta: 1000.00 zł", font=("Arial", 14, "bold"), bg="#39E047", fg="black")
    saldo_bar.pack(fill="x", pady=5)

    tk.Label(root, text="WARZYWNIAK", font=("Arial", 20, "bold"), bg="#39E047", fg="black").pack(fill="x", pady=5)
    tk.Label(root, text="Dostępne Produkty:", font=("Arial", 13, "bold"), bg="#acffb5", fg="black").pack(anchor="w", padx=10)

    # Tabela produktów (Treeview)
    columns_prod = ("nazwa", "cena", "stan")
    tree_asc = ttk.Treeview(root, columns=columns_prod, show="headings", height=6)
    tree_asc.heading("nazwa", text="Nazwa")
    tree_asc.heading("cena", text="Cena za szt./kg")
    tree_asc.heading("stan", text="Stan magazynowy")
    tree_asc.pack(fill="x", padx=10, pady=5)

    # Panel sterowania ilością i dodawaniem
    frame_sterowanie = tk.Frame(root, bg="#acffb5")
    frame_sterowanie.pack(fill="x", padx=10, pady=10)

    tk.Label(frame_sterowanie, text="Wpisz ilość:", font=("Arial", 11), bg="#acffb5").pack(side="left", padx=5)
    quantity_entry = tk.Entry(frame_sterowanie, font=("Arial", 11), width=10)
    quantity_entry.pack(side="left", padx=5)

    btn_dodaj = tk.Button(frame_sterowanie, text="Dodaj do koszyka", font=("Arial", 11, "bold"), bg="#4caf50", fg="white")
    btn_dodaj.pack(side="left", padx=15)

    btn_usun = tk.Button(frame_sterowanie, text="Usuń zaznaczone z koszyka", font=("Arial", 11), bg="#e53935", fg="white")
    btn_usun.pack(side="left", padx=5)

    # Sekcja Koszyka
    tk.Label(root, text="Koszyk", font=("Arial", 15, "bold"), bg="#0C9300", fg="black").pack(fill="x", pady=10)

    # Używamy Listboxa, który gwarantuje, że dodane produkty zawsze będą widoczne
    frame_koszyk = tk.Frame(root, bg="#acffb5")
    frame_koszyk.pack(fill="x", padx=10, pady=5)

    list_cart = tk.Listbox(frame_koszyk, font=("Arial", 11), height=6, bg="white", fg="black", selectbackground="#0C9300")
    list_cart.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_koszyk, orient="vertical", command=list_cart.yview)
    scrollbar.pack(side="right", fill="y")
    list_cart.config(yscrollcommand=scrollbar.set)

    # Podsumowanie i przycisk zakupu
    frame_dol = tk.Frame(root, bg="#acffb5")
    frame_dol.pack(fill="x", padx=10, pady=15)

    lbl_suma = tk.Label(frame_dol, text="ŁĄCZNIE DO ZAPŁATY: 0.00 zł", font=("Arial", 13, "bold"), bg="#acffb5", fg="black")
    lbl_suma.pack(side="left", padx=5)

    btn_kup = tk.Button(frame_dol, text="KUP", font=("Arial", 14, "bold"), bg="#ff9800", fg="white", width=12)
    btn_kup.pack(side="right", padx=5)

    # Słownik wiążący elementy interfejsu dla main.py
    gui = {
        "tree_asc": tree_asc,
        "list_cart": list_cart,
        "quantity_entry": quantity_entry,
        "btn_dodaj": btn_dodaj,
        "btn_usun": btn_usun,
        "btn_kup": btn_kup,
        "lbl_suma": lbl_suma,
        "saldo_bar": saldo_bar
    }

    return root, gui