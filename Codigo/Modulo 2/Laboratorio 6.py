with open("Modulo 2\\Laboratorio 5 - personas.txt","r") as f:
    lista=f.readlines()

print(lista)
j=0
for i in lista:
    lista[j]=i.title()
    lista[j]=lista[j].split("-")
    j=j+1


#Recorro todo el array para eliminar espacios y caracteres especiales
for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista[i][j]=lista[i][j].strip()
print(lista)

dic={}

for i in range(len(lista)):
    a=lista[i][0]
    b=lista[i][1]
    dic[a]=int(b)

print(dic)
