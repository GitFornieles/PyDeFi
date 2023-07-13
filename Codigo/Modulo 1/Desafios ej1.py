lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2=[2, 4, 10, 10, 10]
lista3=[]

if len(lista2)>len(lista1):
    for i in lista1:
        if i in lista2:
            if i not in lista3:
                lista3.append(i)
else:
    for i in lista2:
        if i in lista1:
            if i not in lista3:
                lista3.append(i)

print(lista3)

print(len("hola"))
#-Reso del profesor
# primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
# segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

# tercera = []

# for n in primera:
#     if n in segunda and n not in tercera:
#         tercera.append(n)

# print(tercera)