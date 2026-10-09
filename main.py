import tkinter as tk
from tkinter import messagebox
import dane
import interfejs

root, gui = interfejs.stworz_okno()

indeksy_koszyka = {}

def akcja_dodaj():
    wybrane = gui["tree_asc"].selection()
    if not wybrane:
        dzieci = gui["tree_asc"].get_children()
        if dzieci:
            klucz = dzieci[0]
        else:
            return
    else:
        klucz = wybrane[0]
        
    prod = dane.produkty[klucz]

    try:
        tekst_ilosci = gui["quantity_entry"].get().strip().replace(",", ".")
        if not tekst_ilosci:
            ilosc = 1.0
        else:
            ilosc = float(tekst_ilosci)
            
        if ilosc <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Błąd", "Wpisz poprawną liczbę (np. 1 lub 1.5)!")
        return

    if prod["stan"] < ilosc:
        messagebox.showerror("Błąd", f"Brak w magazynie! Dostępne tylko: {prod['stan']} {prod['jednostka']}")
        return

    prod["stan"] -= ilosc
    dane.koszyk[klucz] = dane.koszyk.get(klucz, 0.0) + ilosc
    
    gui["quantity_entry"].delete(0, tk.END)
    odswiez()

def akcja_usun():
    wybrane_indeksy = gui["list_cart"].curselection()
    if not wybrane_indeksy:
        return
    
    idx = wybrane_indeksy[0]
    if idx in indeksy_koszyka:
        klucz = indeksy_koszyka[idx]
        if klucz in dane.koszyk:
            dane.produkty[klucz]["stan"] += dane.koszyk[klucz]
            del dane.koszyk[klucz]
            odswiez()

def akcja_kup():
    if not dane.koszyk:
        messagebox.showinfo("Koszyk", "Koszyk jest pusty!")
        return

    suma = sum(il * dane.produkty[k]["cena"] for k, il in dane.koszyk.items())

    if dane.saldo_konto < suma:
        messagebox.showerror("Błąd", "Za mało środków na koncie!")
        return

    dane.saldo_konto -= suma
    messagebox.showinfo("Sukces", f"Zakup udany! Pobrano: {suma:.2f} zł.")
    dane.koszyk = {}
    odswiez()

def odswiez():
    global indeksy_koszyka
    indeksy_koszyka = {}

    for row in gui["tree_asc"].get_children():
        gui["tree_asc"].delete(row)
    for k, p in dane.produkty.items():
        gui["tree_asc"].insert("", "end", iid=k, values=(p["nazwa"], f"{p['cena']:.2f} zł/{p['jednostka']}", f"{p['stan']:.1f} {p['jednostka']}"))

    gui["list_cart"].delete(0, tk.END)

    suma = 0
    i = 0
    for k, il in dane.koszyk.items():
        p = dane.produkty[k]
        cena_koncowa = il * p["cena"]
        suma += cena_koncowa

        tekst = f"{p['nazwa']} — {il:.1f} {p['jednostka']} = {cena_koncowa:.2f} zł"
        gui["list_cart"].insert(tk.END, tekst)
        indeksy_koszyka[i] = k
        i += 1

    gui["lbl_suma"].config(text=f"ŁĄCZNIE DO ZAPŁATY: {suma:.2f} zł")
    gui["saldo_bar"].config(text=f"Stan konta: {dane.saldo_konto:.2f} zł")

gui["btn_dodaj"].config(command=akcja_dodaj)
gui["btn_usun"].config(command=akcja_usun)
gui["btn_kup"].config(command=akcja_kup)

odswiez()
root.mainloop()