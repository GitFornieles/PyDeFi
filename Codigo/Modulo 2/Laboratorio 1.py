from re import A


def cubo(x):
    return x**3

def cuadrado(x):
    return x**2

def listarrdos(func, listaentrada):
    listasalida=[]
    for x in listaentrada:
        listasalida.append(func(x))
    print(listasalida)
listarrdos(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
listarrdos(cubo, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

