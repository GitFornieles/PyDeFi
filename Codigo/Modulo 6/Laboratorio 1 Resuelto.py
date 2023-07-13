import tkinter as tk
from tkinter import messagebox


def saludar():
    # Me permite acceder a la variable "saludos" definida
    # fuera de la función.
    global saludos
    # Chequear que los saludos no sean mayores a cinco.
    # Una vez alcanzados, se muestra un mensaje de error.
    if saludos == 5:
        messagebox.showerror(
            title="Error",
            message="Ya se han emitido demasiados saludos."
        )
        # Terminar la función.
        return
    # Obtener el nombre ingresado en la caja de texto.
    nombre = texto_nombre.get()
    # Chequear que no esté vacío.
    if nombre:
        # Mostrar el saludo en una etiqueta.
        label_saludo.configure(
            text=f"¡Hola, {nombre}!")
        # Añadir el nombre a la lista.
        lista_nombres.insert(tk.END, nombre)
        # Borrar el contenido de la caja de texto.
        texto_nombre.delete(0, tk.END)
        # Aumentar el contador de saludos.
        saludos += 1
    else:
        messagebox.showinfo(
            title="Falta información",
            message="Debe ingresar un nombre."
        )


saludos = 0


ventana = tk.Tk()
ventana.title("Ejercicio integrador")
ventana.config(width=300, height=200)
# Variable que lleva la cuenta de los saludos emitidos.
texto_nombre = tk.Entry()
texto_nombre.place(x=10, y=10, width=200, height=23)
boton_saludar = tk.Button(text="¡Saludar!", command=saludar)
boton_saludar.place(y=9, x=215)
label_saludo = tk.Label()
label_saludo.place(x=10, y=35)
lista_nombres = tk.Listbox()
lista_nombres.place(x=10, y=60, width=278, height=120)
ventana.mainloop()