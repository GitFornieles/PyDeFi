"""Desarrollar un script buscar_archivos.py que reciba
como argumentos la ruta a una carpeta y una extensión
para buscar archivos dentro de ella. Luego debe
mostrar los archivos que terminen con dicha extensión
en la carpeta indicada. Por ejemplo, en el caso siguiente
se listan los archivos con extensión “.exe” en la carpeta
llamada “carpeta”:
> python buscar_archivos.py "C:\ruta\carpeta" .exe
Archivos con extensión .exe:
- hola.exe
- chau.exe"""

import sys
import os

os.system("cls")

try:
    ruta=sys.argv[1]
    ext=sys.argv[2]
except:
    print("""Recuerde ingresar "nombre.py ruta_de_carpeta extension_buscada""")

if ext.startswith(".")==False:
    ext= "."+ext

if os.path.exists(ruta):
    listado=os.listdir(ruta)
    resultado=[]
    for n in listado:
        if n.endswith(ext):
            resultado.append(n)
    print(resultado)
else:
    print("La ruta no existe")