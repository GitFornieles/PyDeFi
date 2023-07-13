def serieFibo(num):
    if num<=2:return "Número debe ser mayor a 2"
    lista=[0,1,1]
    c=3
    while c<=num-1:
        lista.append(lista[c-1]+lista[c-2])
        c+=1
    return lista

print(serieFibo(10))
