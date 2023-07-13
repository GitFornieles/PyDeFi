"""
Hacer un pequeño programa con un menú
muy sencillo:
Menú:
1 – Ingreso de empleado
2 – Egreso de empleado
3 – Salir del sistema
>>>
Este sistema es básico, lo utiliza el personal
de seguridad que registra el nombre de la
persona que ingresa (opción 1), y que egresa
del edificio (opción 2).

Además, es necesario registrar el horario de
los eventos se podría usar el módulo time, y
la función asctime() que devuelve un str
con fecha y hora.
Cuando se quiere salir del programa se usa la
opción 3.
Tanto el ingreso y el egreso se registra en un
archivo txt. Cada renglón representa un
registro.
"""

import time

"""
No se detalla en el enunciado, pero el codigo parte de la base de que los archivos ya existen, y se les agrega información.
Se Guardan ingresos y egresos por separado
"""
def registro(operacion):
    nombre=input("Por favor ingrese el nombre del empleado que INGRESA: ")
    registro=time.asctime() + " - " + nombre + " - " + operacion + "\n"
    with open("Modulo 2\\Desafios Ej2\\registro.txt","a") as f:
        f.write(registro)

def ingreso(ent):
    """
    Esta función es un bucle de validación de ingreso de un número
    No recibe argumentos pero devuelve una lista de dos componentes.
     - El primero es el número validado, o el mensaje de error.
     - El segundo es un booleano utilizado para maniupal el bucle
    """
    try:
        a=float(ent)
        return [a, False]
    except ValueError:
        a="No ha ingresado un número"
        return [a, True]
    else:
        a="No se sabe qué, pero algo pasó"
        return [a, True]

def validar():
    """
    Bucle de validación
    No toma argumentos pero devuelve el número que se solicita en formato float.
    """
    cont=True
    rta=[]
    while cont==True:
        entrada=input("Ingrese opción: ")
        print()
        rta=ingreso(entrada)
        num=rta[0]
        cont=rta[1]
        if cont==True:
            print(num)
    return num


varmenu=0
while varmenu!=3:
    print()
    print("-------------------------MENÚ-------------------------")
    print("1. Ingreso de Empleado")
    print("2. Egreso de Empleado")
    print("3. SALIR")
    print("------------------------------------------------------")
    print()
    varmenu=validar()
    if varmenu==1:
        registro("Ingreso")
        print("Registro Exitoso")
    elif varmenu==2:
        registro("Egreso")
        print("Registro Exitoso")
    elif varmenu==3:
        print("Gracias, vuelva pronto")
    else:
        print("Opción no válida")


    
