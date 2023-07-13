import tkinter as tk
from tkinter import ttk


def imprimir_texto():
    print(entry.get())


ventana_principal = tk.Tk()
ventana_principal.title("Mi primera aplicación")
ventana_principal.config(width=300, height=200)


entry = ttk.Entry()
entry.place(x=10, y=10)
boton = ttk.Button(text="Imprimir texto", command=imprimir_texto)
boton.place(x=10, y=50)

# Inserta el texto al comienzo del control.
entry.insert(0, "Hola mundo")
# Borra los primeros 10 caracteres.
entry.delete(0, 10)
# Borra todo el texto.
entry.delete(0, tk.END)

label = ttk.Label(text="Hola mundo")
label.place(x=20, y=80)




ventana_principal.mainloop()