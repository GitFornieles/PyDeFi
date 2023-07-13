import requests
import os
import sys
import time
from tabulate import tabulate

#Recordar tener corriendo el servicio servicio_web.py
"""Para este ejercicio estaremos usando el mismo
servicio web que en el material de la clase, es decir,
el servicio web servicio_web.py, que tenés que
tener en ejecución.
Desarrollar un programa admin_alumnos.py que
permita añadir, modificar, eliminar y listar los
alumnos del servicio web.
A continuación, encontrará ejemplos de uso (en rojo
lo que ingresa el usuario)."""


def func_agregar():
    nombre=input("Ingrese el Nombre: ")
    cursos=input("Ingrese cantidad de Cursos: ")
    try:
        requests.post("http://localhost:7001/student", json={"name":nombre, "courses":cursos})
        print("Registro Exitoso")
        time.sleep(1)
    except:
        print("Pasó Algo")
        time.sleep(1)



def func_modif():
    os.system("cls")
    func_list()
    datos={}
    print("")
    id=input("Ingrese el ID del alumno a modificar: ")
    nombre=input("Ingrese el Nuevo nombre (o presione ENTER para no modificar): ")
    cursos=input("Ingrese cantidad de Cursos (o presione ENTER para no modificar): ")
    if nombre=="":
        datos={"courses":cursos}
    elif (cursos=="" or cursos==0):
        datos={"name":nombre}
    else:
        datos={"name":nombre, "courses":cursos}
    try:
        requests.put(f"http://localhost:7001/student/{id}", json=datos)
        print("Modificación Exitosa")
        time.sleep(1)
    except:
        print("Pasó Algo")
        time.sleep(1)

def listdic_to_array(list_dic): #diccionario es una lista de diccionarios
    array=[]
    i=0
    encabezados=list(list_dic[0]) # armo un vector con todas las claves del diccionario en la posición 0 del array list_dic
    for n in list_dic:
        aux=[]
        for k,v in n.items(): #este for recorre el diccionario k es de clave, v es de value. creo un array auxiliar con los valores del diccionario n.
            aux.append(v)
        array.append(aux)
    resultado=[encabezados, array]
    return resultado

def func_list():
    students=requests.get("http://localhost:7001/student")
    response=students.json() #Recordar que el diccionario que devuelve es ["recurso":[{dicc1},{dicc2},{dicc3}....]]
    """ list(diccionario) devuelve un array con las claves del diccionario. En este caso, solo tiene una clave, que está en la posicion 0. 
    Por otro lado llamar a diccionario["clave"] devuelve el valor para esa clave
    El resultado de "response[list(response[0])]" es el array de diccionarios. (el array es el valor para la clave "recurso") """
    lista_dic=response[list(response)[0]] 
    informacion=listdic_to_array(lista_dic)
    encabezados=informacion[0]
    listado=informacion[1]
    print(tabulate(listado, headers=encabezados ,tablefmt="pretty"))


def func_elim():
    os.system("cls")
    func_list()
    print("")
    id=input("Ingrese el ID del alumno a eliminar: ")
    try:
        requests.delete(f"http://localhost:7001/student/{id}")
        print("Eliminación Exitosa")
        time.sleep(1)
    except:
        print("Pasó Algo")
        time.sleep(1)
    

while True:
    os.system("cls")
    print("-------------- Menú --------------")
    print("1. Agregar un alumno")
    print("2. Modificar alumno existente")
    print("3. Listar alumnos")
    print("4. Eliminar un alumno")
    print("5. Salir")
    print("")
    opc=input("Opción: ")
    if opc=="1":
        func_agregar()
    elif opc=="2":
        func_modif()
    elif opc=="3":
        func_list()
        print("")
        input("Presione ENTER para continuar")
    elif opc=="4":
        func_elim()
    elif opc=="5":
        print("Gracias. Vuelva pronto")
        sys.exit()
    else:
        print("Seleccione un número de 1 a 4 y presione ENTER")
        time.sleep(1)