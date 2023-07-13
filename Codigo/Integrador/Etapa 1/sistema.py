import sys
import os
import tabulate
import time

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
    print("Armado del pedido")
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
    pago=ingresar_numeros("Abona con $")
    vuelto=pago-total
    print(f"Vuelto ${vuelto}")
    opc=""
    while opc not in ["S", "N", "s", "n"]:
        opc=input("¿Confirma el pedido? (S/N): ")
    if opc in ["S", "s"]:
        pedido.append(total)
        registrar("ventas.txt", pedido, "; ")

def registrar(archivo, informacion, separador):
    registro=""
    for n in informacion:
        registro= registro + str(n) + separador
    registro = registro + "\n"
    with open("Integrador/Etapa 1/registro/"+archivo,"a") as f:
        f.write(registro)

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
    os.system("cls")
    registrar("registro.txt",["IN", time.asctime(), "Encargad@"+nombre], "  ")
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
            nvopedido(menu)
            pass
        elif opc=="2":
            os.system("cls")
            registrar("registro.txt",["OUT", time.asctime(), "Encargad@"+nombre], "  ")
            registrar("registro.txt",["##################################################"],"")
            break
        elif opc=="3":
            print("Saludos!")
            sys.exit()