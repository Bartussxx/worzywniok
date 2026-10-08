import tkinter as tk


root = tk.Tk()
root.title("WARZYWNIAK")
root.geometry("1000x1500")
root.config(bg="#acffb5")

tk.Label(root, text="WARZYWNIAK", font=("Arial", 22, "bold"), bg="#39E047", fg="black").pack(fill="x", pady=10)
tk.Label(root, text="Produkty:", font=("Arial", 15, "bold"), bg="#39E047", fg="black").pack(fill="x", pady=10)

frame_kafelek = tk.Frame(root, bg="#2d2d2d", bd=2, relief="groove")
frame_kafelek.pack(fill="x", padx=10, pady=6)


kafelek_tekst = tk.Label(
    frame_kafelek,
    text=f"{nazwa}\nPoziom: {poziom}\nCena: {cena:.2f} PLN",
    font=("Arial", 10),
    bg="#2d2d2d",
    fg="white",
    justify="left",
)
kafelek_tekst.pack(side="left", padx=10, pady=8)

kup_przycisk = tk.Button(
    frame_kafelek,
    text="Kup to jeśli cię stać!",
    font=("Arial", 15, "bold"),
    bg="#4caf50",
    fg="white",
    command=funkcja_klikniecia,
)
kup_przycisk.pack(side="right", padx=10, pady=8)

tk.Label(root, text="Koszyk", font=("Arial", 15, "bold"), bg="#0C9300", fg="black").pack(fill="x", pady=10)

root.mainloop()

    