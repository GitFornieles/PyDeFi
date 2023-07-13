"""Como bien sabemos “pip” nos permite
instalar módulos de terceros. Pero además de
pasarle el argumento “install”, podemos
pasar otros.
Por ejemplo, “pip list” nos muestra una
lista de los módulos instalados. Existen más
comandos, para más información, puedes
ejecutar desde la consola del sistema
operativo: “ pip -h ”.
Este ejercicio trata de crear un script que use
el módulo subprocess para ejecutar “pip
list” y de esa manera con
capture_output tomar la lista y logremos
guardar en un “txt”, sólo los nombres de los
módulos.
Este programa será una automatización útil
para tener a mano y hacer un “backup”."""

import os
import subprocess

from click import open_file
os.system("cls")

instalados=subprocess.run("pip list", capture_output=True, encoding="cp850")
respuesta=instalados.stdout.split("\n")
print(respuesta)

for item in respuesta:
    item=item.split(" ")

for n in respuesta: #recorre cada línea de la lista "respuesta", y en cada una reasigna el valor de la lista
    fin=n.find(" ")
    n=n[0:fin]
    print(n)

with open("Modulo 3/Desafios/bkup.txt","a") as f:
    for n in respuesta:
        linea=f"{n}\n"
        f.write(linea)









# En este punto, respuesta es una lista de cadenas
# Este for de acá abajo lo que hace es convertir cada una de los cadenas (que en este caso cada una es "modulo       versión"):
# ['Package            Version', '------------------ ---------', 'certifi            2021.10.8', 'charset-normalizer 2.0.12', 'click              8.0.3', 'colorama           0.4.4', 'et-xmlfile         1.1.0', 'Flask              2.0.3', 'idna               3.3', 'itsdangerous       2.0.1', 'Jinja2             3.0.3', 'MarkupSafe         2.0.1', 'openpyxl           3.0.9', 'pip                22.0.3', 'psutil             5.9.0', 'PyMySQL            1.0.2', 'requests           2.27.1', 'setuptools         60.1.0', 'tabulate           0.8.9', 'urllib3            1.26.8', 'Werkzeug           2.0.3', 'wheel              0.37.1', '']
# 
# Este proceso de acá abajo, reemplaza la cadena de espacios por un solo ";" , que luego uso para separar en dos cadenas.
# El resultado es que cada elemento de "respuesta" es ahora una lista de dos posiciones. La posición 0 tiene le nombre y la posición 1 tiene la versión.
# for n in respuesta:
#     esp=n.count(" ") # Cantidad de espacios en la cadena de texto
#     separador= " " * esp
#     n.replace(separador,";")
#     n=n.split(";")
#     print(n)
