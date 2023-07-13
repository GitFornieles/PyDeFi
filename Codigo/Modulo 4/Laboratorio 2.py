import sys
import os
import sqlite3
from tabulate import tabulate

conexion=sqlite3.connect("eduit_PRODUCTOS.sqlite")
cursor=conexion.cursor()

def registrar():
    os.system("cls")
    while True:
        try:
            id=int(input("Ingrese el ID del producto a agregar: "))
            break
        except:
            print("Sólo números por favor")
    nombre=input("Ingrese el nombre del producto a agregar: ")
    while True:
        try:
            precio=int(input("Ingrese el precio del producto a agregar: "))
            break
        except:
            print("Sólo números por favor")
    try:
        conexion=sqlite3.connect("eduit_PRODUCTOS.sqlite")
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO productos VALUES (?,?,?)", [id, nombre, precio])
        conexion.commit()
        conexion.close()
    except:
        print("Hubo un error")
        input()
    
def mostrar():
    try:
        conexion=sqlite3.connect("eduit_PRODUCTOS.sqlite")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos=cursor.fetchall()
        print(tabulate(productos, headers=("ID", "PRODUCTO", "PRECIO")))

    except:
        print("Hubo un error")


while True:
    os.system("cls")
    print("------- MENÚ -------")
    print("")
    print("1 - Agregar productos")
    print("2 - Ver Productos")
    print("3 - Salir")
    print("")
    opc=input("Ingrese una opción: ")
    if opc=="1":
        registrar()
    elif opc=="2":
        os.system("cls")
        mostrar()
        input()
    elif opc=="3":
        print("Gracias, Vuelva Pronto")
        sys.exit()
    else:
        print("Opción no válida. Presione algo para seguir")
        input()
