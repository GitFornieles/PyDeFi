"""
Esta función sirve para validar que un input es un float.
El argumento que se pasa es el mensaje que se muestra para pedir el númoer ("Por favor ingrese su edad" por ejemplo)

"""


def ingresar_numeros(mensaje="Por favor ingrese el número: "):
    valor = input(mensaje)
    while True:
        try:
            valor = float(valor)
            break
        except ValueError:
            print("Solo números")
        valor = input(mensaje)
    return valor



numero=ingresar_numeros("ingrese su edad: ")

print(numero)