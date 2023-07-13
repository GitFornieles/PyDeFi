import os
"""Crear un script buscar_proceso.py que reciba
como argumento a través de la consola el
nombre de un proceso, ejecute vía subprocess
el programa processinfo.py e imprima su PID y
usuario. Si hay varios procesos con el mismo
nombre, debe imprimir la información de todos
ellos. Por ejemplo:
> python buscar_proceso.py firefox.exe
PID: 4764. Usuario: Lautaro.
PID: 11080. Usuario: Lautaro.
Si el nombre del proceso no es indicado, debe
mostrar un error en la consola y finalizar.
> python buscar_proceso.py
Indique el nombre de un proceso."""


import sys
import os
import subprocess

os.system("cls")
try:
    proceso=sys.argv[1]
except:
    print("Ingrese el nombre del preceso a busacar")

rta=subprocess.run("python processinfo.py", capture_output=True, encoding="cp850") # rta.stdout será un string (aunque se vea como tabla. es como trabaja el módulo tabulate)
os.system("cls")
print("Desde aca\n")

lista_procesos=rta.stdout.split("\n")

final=len(lista_procesos)

tabla_procesos=[]
for i in range(0,3):
    tabla_procesos.append(lista_procesos[i])

for i in range(3,final):
    if lista_procesos[i].count(proceso)>0:
        tabla_procesos.append(lista_procesos[i])

for n in tabla_procesos:
    print(n)

print("\n")

