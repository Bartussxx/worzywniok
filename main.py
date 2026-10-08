from tkinter import messagebox
import dane
import interfejs

# Uruchomienie okna i pobranie elementów graficznych
root, gui = interfejs.stworz_okno()

def oblicz_rabat(prod, ilosc):
    cena_bazowa = ilosc * prod["cena"]
    rabat = 0.0
    if ilosc >= prod["rabat_prog"]:
        rabat = cena_bazowa * prod["rabat_procent"]
    return cena_bazowa - rabat, rabat

def akcja_dodaj():
    wybrane = gui["tree_asc"].selection()
    if not wybrane:
        return
    klucz = wybrane[0]
    prod = dane.produkty[klucz]

    try:
        ilosc = float(gui["quantity_entry"].get().replace(",", "."))
        if ilosc <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Błąd", "Wpisz poprawną liczbę!")
        return

    if prod["stan"] < ilosc:
        messagebox.showerror("Błąd", "Brak w magazynie!")
        return

    prod["stan"] -= ilosc
    dane.koszyk[klucz] = dane.koszyk.get(klucz, 0.0) + ilosc
    odswiez()

def akcja_usun():
    wybrane = gui["tree_cart"].selection()
    if not wybrane:
        return
    klucz = wybrane[0]
    if klucz in dane.koszyk:
        dane.produkty[klucz]["stan"] += dane.koszyk[klucz]
        del dane.koszyk[klucz]
        odswiez()

def akcja_kup():
    if not dane.koszyk:
        messagebox.showinfo("Koszyk", "Koszyk jest pusty!")
        return

    suma = sum(oblicz_rabat(dane.produkty[k], il)[0] for k, il in dane.koszyk.items())

    if dane.saldo_konto < suma:
        messagebox.showerror("Błąd", "Za mało środków na koncie!")
        return

    dane.saldo_konto -= suma
    messagebox.showinfo("Sukces", f"Zakup udany! Pobrano: {suma:.2f} zł.")
    dane.koszyk = {}
    odswiez()

def odswiez():
    # Odświeżanie produktów
    for row in gui["tree_asc"].get_children():
        gui["tree_asc"].delete(row)
    for k, p in dane.produkty.items():
        gui["tree_asc"].insert("", "end", iid=k, values=(p["nazwa"], f"{p['cena']:.2f} zł/{p['jednostka']}", p["stan"]))

    # Odświeżanie koszyka
    for row in gui["tree_cart"].get_children():
        gui["tree_cart"].delete(row)

    suma = 0
    for k, il in dane.koszyk.items():
        p = dane.produkty[k]
        cena_koncowa, rabat_kwota = oblicz_rabat(p, il)
        suma += cena_koncowa

        tekst = f"{il} {p['jednostka']} = {cena_koncowa:.2f} zł"
        if rabat_kwota > 0:
            tekst += f" (rabat -{rabat_kwota:.2f} zł)"

        gui["tree_cart"].insert("", "end", iid=k, values=(p["nazwa"], tekst))

    gui["lbl_suma"].config(text=f"ŁĄCZNIE DO ZAPŁATY: {suma:.2f} zł")
    gui["saldo_bar"].config(text=f"Stan konta: {dane.saldo_konto:.2f} zł")

# Podpięcie funkcji pod przyciski z interfejsu
gui["btn_dodaj"].config(command=akcja_dodaj)
gui["btn_usun"].config(command=akcja_usun)
gui["btn_kup"].config(command=akcja_kup)

odswiez()
root.mainloop()