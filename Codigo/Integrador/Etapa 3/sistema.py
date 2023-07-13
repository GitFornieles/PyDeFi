import sqlite3
import sys
import os
from tabulate import tabulate
import time


# conexión a BBDD y verificación de existencia de tablas

conexion=sqlite3.connect("C:\\Users\\alefo\\Desktop\\EducacionIT\\03 - Python Programing\\Codigo\\Integrador\\Etapa 2\\registro\\comercio.sqlite")
cursor=conexion.cursor()
try:
    cursor.execute("""CREATE TABLE ventas(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente varchar(20),
        fecha varchar(50),
        ComboS int,
        ComboD int,
        ComboT int,
        Flurby int,
        Total int
        )
        """)
    cursor.execute("""CREATE TABLE registro(
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        Encargado varchar(20),
        Fecha varchar(50),
        Evento varchar(3),
        Caja int
        )
        """)
except:
     print("No se crearon las tablas")
conexion.commit()
conexion.close()

# Tabla de Productos

menu=[["Combo Simple + Bebida", 5],
      ["Combo Doble + Bebida", 6], 
      ["Combo Triple + Bebida", 7],
      ["McFlurby", 2]]

# FUNCIONES

def nvopedido(precios):
    """Esta función arma el pedido y muestra el precio
    Recibe de argumento la lista de precios (tabla de dos columnas) y el nombre del encargado
    Si se acepta, guarda la información del pedido
    Si no se acepta, vuelve al menú
    INFO QUE SE GUARDA:
    En Archivo Ventas: se registra
    [nombrecliente, fecha, cant combo1, cant combo2, cant combo3, cant postre, ingreso total]
    """
    pedido=[]
    os.system("cls")
    print(tabulate(precios, headers=["Opción","Precio"]))
    print("")
    pedido.append(input("Ingrese nombre del cliente: "))
    pedido.append(time.asctime())
    pedido.append(ingresar_numeros("Ingrese cantidad de combo S: "))
    pedido.append(ingresar_numeros("Ingrese cantidad de combo D: "))
    pedido.append(ingresar_numeros("Ingrese cantidad de combo T: "))
    pedido.append(ingresar_numeros("Ingrese cantidad de Flurby: "))
    total=0
    for i in range(2, len(pedido)):
        total= pedido[i]*precios[i-2][1] + total
    
    print(f"\nTotal ${total}")
    pago=0
    while pago<total:
        pago=ingresar_numeros("Abona con $: ")
        if pago<total:
            print("Monto insuficiente")
    vuelto=pago-total
    print(f"Vuelto ${vuelto}")
    opc=""
    while opc not in ["S", "N", "s", "n"]:
        opc=input("¿Confirma el pedido? (S/N): ")
    if opc in ["S", "s"]:
        pedido.append(total)
        registrarvta(pedido)
        return total

def registrarvta(informacion):
    try:
        conexion=sqlite3.connect("C:\\Users\\alefo\\Desktop\\EducacionIT\\03 - Python Programing\\Codigo\\Integrador\\Etapa 2\\registro\\comercio.sqlite")
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO ventas (cliente, fecha, ComboS, ComboD, ComboT, Flurby, Total) VALUES (?,?,?,?,?,?,?)",informacion)
        conexion.commit()
        conexion.close()
        print("Pedido Registrado con Éxito")
        time.sleep(1)
    except:
        input("No pudo registrarse el pedido")

def registrarturno(informacion):
    try:
        conexion=sqlite3.connect("C:\\Users\\alefo\\Desktop\\EducacionIT\\03 - Python Programing\\Codigo\\Integrador\\Etapa 2\\registro\\comercio.sqlite")
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO registro (Encargado, Fecha, Evento, Caja) VALUES (?,?,?,?)", informacion)
        conexion.commit()
        conexion.close()
        print("Cambio Registrado con Éxito")
        time.sleep(1)
    except:
        input("No pudo registrarse el cambio")

def ingresar_numeros(mensaje):
    valor = input(mensaje)
    while True:
        try:
            valor = int(valor)
            break
        except ValueError:
            print(mensaje)
        valor = input()
    return valor


#-----------------------------MENÚ PRINCIPAL----------------
opc="0"
while opc!="3":
    os.system("cls")
    print("Bienvenido a Hamburguesas IT")
    nombre=input("Ingrese su nombre: ")
    caja=0
    os.system("cls")
    registrarturno([nombre, time.asctime(), "IN", caja])
    while opc!="3":
        os.system("cls")
        print("Hamburguesas IT")
        print(f"Encargad@ -> {nombre}")
        print("Recuerda, siempre hay que recibir al\ncliente con una sonrisa :)\n")
        print("1 - Ingreso de nuevo pedido")
        print("2 - cambio de turno")
        print("3 - Apagar Sistema")
        opc=input("\nIngrese su opción: ")
        while opc not in ["1", "2", "3"]:
            opc=input("\nIngrese su opción: ")
        if opc=="1":
            os.system("cls")
            caja=nvopedido(menu)+caja
            pass
        elif opc=="2":
            os.system("cls")
            registrarturno([nombre, time.asctime(), "OUT", caja])
            break
        elif opc=="3":
            registrarturno([nombre, time.asctime(), "OUT", caja])
            print("Saludos!")
            sys.exit()