"""Crear una clase cliente que pida por argumento los
atributos: nombre_apellido(str) y el cuit
(str, usar guiones del medio).
Únicamente tendrá un método que sea
.mostrar_info() que muestra por pantalla el
nombre del cliente y su cuit.
Ejemplo al crear una instancia:
cliente1 = Cliente(nombreyapellido,cuit)"""


import os
import sys

class cliente():
    def __init__(self, nombrecom, ncuit) -> None:
        self.nombreyapellido=nombrecom
        self.cuit=ncuit
    
    def mostrarinfo(self):
        print(f"Nombre de Cliente: {self.nombreyapellido}")
        print(f"CUIT: {self.cuit}")

try:
    juancho=cliente(sys.argv[1],sys.argv[2])
except:
    print("Error. Programa finalizado. Recuerde escribir en el formato nombre_apellido XX-XXXXXXXX-XX")

juancho.mostrarinfo()

"""python "Ejercicio 1.py" juancho 2563"""