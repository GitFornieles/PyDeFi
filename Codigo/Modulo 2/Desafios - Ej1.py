"""
Crear una función que use lo visto de excepciones
para que tome por input() el número como str y
lo transforme directamente a float, sea entero o
decimal. Deberíamos pasar como argumento la
frase para mostrar en pantalla el pedido. Además,
deberíamos de volver a pedir, hasta que se pueda
hacer el ingreso de forma correcta.
A partir de ahora cada vez que tomemos un número
por teclado podemos hacer uso de esta función que
vamos a crear.
"""

def ingreso(ent):
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
    cont=True
    rta=[]
    while cont==True:
        entrada=input("Ingrese el número: ")
        rta=ingreso(entrada)
        num=rta[0]
        cont=rta[1]
        if cont==True:
            print(num)
    return num





