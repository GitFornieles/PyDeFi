lista=[1,2,3,4,5,6]
c=0
for n in (lista2:=lista[:-1]):
    c=c+n
print(c)

# (lista2:=lista[:-1])=> esta linea crea una lista nueva que es igual a la lista original (usando el wallrus)
# luego el bucle suma los valores de esta lista 2