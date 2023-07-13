import requests


""" Módulo que se usa para comunicar con servicios WEB
La estructura de información que se envía y recibe es en JSON
Python (a través del "requests") se encarga de convertir a JSON para enviar, y si es un comando de solicitud (el servidor devuelve un JSON), con el método json() convierte el JSON que nos mandan a un diccionario
"""

#GET (Solicita info al servidor)

rta=requests.get("URL del recurso")
rta_dicc = rta.json()

"""
rta es el objeto que guarda toda la información de la respuesta del servidor
con el método json() podemos armar un diccionario con esa info

Si en el URL del recurso se agrega al final "/id" (id es el número de id del registor buscado), el GET sólo trae la info de ese registro
Ej (de los slides)

En la web está la tabla de alumnos con la cantidad de cursos, y quiero la info del registor 3:

rta=requests.get("URL del recurso/3")
rta_dicc = rta.json() taerá sólo la info del registro 3


"""

#POST (Envía información de nuevo registro al servidor)

dicc_info={} # Este es el diccionario en el que está la infomración a enviar al servidor

requests.post("URL del recurso",json=dicc_info)

"""
Para cada POST el sistema devolverá un "id"
Recordar que cada "post" es para generar un registro independiente
Es decir, si tengo que enviar varios registros, tengo que hacer un post para cada uno:

Ej (de los slides)
Si quiero enviar a una base de alumnos información de varios alumnos, tengo que hacer un "post" para cada uno:

Creo un array en donde cada fila será un registro nuevo; la primer columna el nombre de la clave y la segunda el valor

Entonces, si quiero enviar una tabla en donde diga la cantidad de cursos aprobados de cada alumno:

TABLA
ALUMNO - CURSOS
alumno1     2
alumno2     1
alumno3     3
alumno4     7
alumno5     8

El array a trabajar es:

datos = [("alumno1",2),("alumno2",1),("alumno3",3),("alumno4",7),("alumno5",8)]

Luego, para hacer el "post": (donde los campos a registrar se llaman "name" y "courses")

for n, c in datos: (n de nombre, c de cursos)
    requests.post("URL del servicio", json={"name":n, "courses":c})

"""

#PUT (Modifica informaci´n de un registro en el servidor)
"""Debe armarse un diccionario con todos los campos que se modificarán y sus nuevos valores"""

valor1=9
valor2=2
datos={"campo1": valor1, "campo2": valor2}
requests.put("URL del recurso/id", jason=datos)

#DELETE (Elimina un registro del servidor)

requests.delete("URL del recurso/id")





