"""Tomar de la sección llamada Descarga, el
Programa Buscar Archivos. El mismo recibe
como argumento una ruta y una extensión.
Transformar el mismo creando un menú,
donde tengamos las siguientes opciones.
Menú
1 - Buscar archivos con determinada
extensión
2 – Salir
>>>
Si se selecciona la opción 1, se procede a
pedir la ruta y la extensión por teclado.
Tratar de usar alguna manera para borrar
pantalla y que siempre volvamos al menú
recurrentemente, pero que la pantalla
quede limpia.
Además, podríamos implementar el uso del
módulo “tabulate” (investigar) que se instala
con “pip”, y sirve para armar una tabla,
entonces se podría listar los archivos con un
número de costado indicando el orden que
se fueron encontrando en esa tabla."""

import os
import sys
from tabulate import *





while True:
    os.system("cls")
    print("------------ MENÚ ------------")
    print("1. Buscar archivos por extensión")
    print("2. Salir")
    opc=input("Ingrese una opción: ")

    if opc=="1":
        os.system("cls")
        ruta=input("Por favor ingrese la ruta: ")
        ext=input("Por favor ingrese la extensión: ")
        try:
            # Obtener la lista de archivos en la ruta especificada.
            archivos = os.listdir(ruta)
        except FileNotFoundError:
            print("La ruta no existe.")
            sys.exit()

        # Si la extensión no empieza con un punto, agregárselo.
        if not ext.startswith("."):
            ext = "." + ext

        print(f"Archivos con extensión {ext}:")
        # Recorrer la lista de archivos.
        resultado=[]
        i=0
        for archivo in archivos:
            # Imprimir únicamente los que terminan con la extensión ingresada.
            if archivo.endswith(ext):
                resultado.append([i, archivo])
                i=i+1
        os.system("cls")
        print(tabulate(resultado, headers=["Num","Archivo"]))
        input("Presione cualquier tecla para continuar")
    elif opc=="2":
        print("Gracias. Saludos")
        break
    else: 
        print("Opción no váliva. Reintente")
        input("Presione cualquier tecla para continuar")

