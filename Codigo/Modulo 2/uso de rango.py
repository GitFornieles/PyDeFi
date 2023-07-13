
with open("Modulo 2\\Desafios Ej2\\registro.txt","r") as f:
    registros=f.readlines()
l=len(registros)
print(l)
n=min(l,5)
print(n)
if l==0:
    print("No existen registros")
for i in range(-1,-n-1,-1):
    print(registros[i])