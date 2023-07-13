import tkinter as tk
from tkinter import messagebox
import requests


################################################

def borrar():
    ccompra.delete(0,tk.END)
    cventa.delete(0,tk.END)




def consultar():
    borrar()
    try:
        r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolaroficial")
        data = r.json()
        compra = data["compra"]
        venta = data["venta"]
        ccompra.insert(0,compra)
        cventa.insert(0,venta)
    except Exception:
        messagebox.showerror(title="Error",message="Se produjo un error")
        ccompra.insert(0,"No hay data")
        cventa.insert(0,"No hay data")
    




################################################


ventana = tk.Tk()
ventana.config(height=200,width=200)
ventana.title("Dolar")

ecompra = tk.Label(text="Compra:")
ecompra.place(x=40,y=20)
ccompra = tk.Entry()
ccompra.place(x=40,y=45)

eventa = tk.Label(text="Venta:")
eventa.place(x=40,y=80)
cventa = tk.Entry()
cventa.place(x=40,y=110)

bconsulta = tk.Button(text="Consulta",command=consultar)
bconsulta.place(x=40,y=150,width=125,height=30)

consultar()

ventana.mainloop()