"""
Al programa anterior (ejercicio 2), agregarle una opción de ver los
últimos 5 registros (opción 3 y salir pasa a opción 4).
Solo los últimos 5 eventos tomarlos directamente del
txt. Si nuestro archivo está vacío, mostrar el mensaje
“No hay registros”, en caso de que tengamos menos
registros que 5, solo mostrar los que se tenga en el
archivo hasta ese momento.
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


def visualizar():
    with open("Modulo 2\\Desafios Ej2\\registro.txt","r") as f:
        registros=f.readlines()
    l=len(registros)
    n=min(l,5)
    if l==0:
        print("No existen registros")
    for i in range(-1,-n-1,-1):
        print(registros[i])
        

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
while varmenu!=4:
    print()
    print("-------------------------MENÚ-------------------------")
    print("1. Ingreso de Empleado")
    print("2. Egreso de Empleado")
    print("3. Visualizar Últimos 5 Registros")
    print("4. SALIR")
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
        print()
        print("Ultimos 5 registros")
        visualizar()
    elif varmenu==4:
        print("Gracias, vuelva pronto")
    else:
        print("Opción no válida")


    
