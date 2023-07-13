from tkinter.tix import FileSelectBox


def fib(a):
    
    fibo=[0,1,1]
    i=2
    if a<=2:
        rta="De nuevo: el número debe ser mayor a 2"
        return rta
    else:
        while len(fibo)<a:
            fibo.append(fibo[i]+fibo[i-1])
            i=i+1
        return fibo

valor=int(input("Ingrese la cantidad de términos a visualizar (valor mayor a 2): "))
lista=fib(valor)
print(lista)


# RESOLUCIÓN DEL PROFESOR:
# Conceptualmente es lo mismo, pero parte de la base de que se puede usar números engativos en el índice para llamar a los últimos valores:
# fibo[-1] llama al último valor, fibo[-2] llama al anteúltimo... etc.
# def fibo(cantidad):
#     # Chequear que la cantidad sea un valor válido.
#     if cantidad <= 2:
#         # Terminar la función.
#         return "La cantidad de terminos debe ser mayor que 2"
#     # Esta es la lista que vamos a retornar. Por definición empieza
#     # con los términos 0 y 1.
#     f = [0, 1]
#     # Añadir elementos hasta haber alcanzado la cantidad indicada.
#     while len(f) < cantidad:
#         # Agregamos al final de la lista un elemento que es la suma
#         # de los dos anteriores.
#         f.append(f[-1] + f[-2])
#     return f


# print(fibo(1))
# print(fibo(10))