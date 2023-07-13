"""Crear una clase “Persona” que sea la clase padre de otra
clase “Estudiante”.
La clase “Persona” su método __init__() debe de estar
preparado para recibir nombre y apellido. Además, esta
clase , debe tener un método para mostrar
nombre_completo() el cual debe mostrar el nombre
acompañado del apellido.
La otra clase “Estudiante”, debe de poder heredar de
“Persona”, y además recibir los argumentos nombre y
apellido. También la clase “Estudiante”, recibe el valor
“carrera”, y además contar con un método
mostrar_carrera() . Las dos clases son obligatorias."""

""" OPCION 1 """
"""class Persona():
    def __init__(self, n, a):
        self.nombre=n
        self.apellido=a
    
    def getname(self):
        print(f"{self.nombre} {self.apellido}")

class Estudiante(Persona):
    def __init__(self, n, a, c):
        super().__init__(n,a)
        self.carrera=c
    
    def getcarrera(self):
        print(self.carrera)"""

class Persona():
    def __init__(self, n, a):
        self.nombre=n
        self.apellido=a
    
    def getname(self):
         return f"{self.nombre} {self.apellido}"

class Estudiante(Persona):
    def __init__(self, n, a, c):
        super().__init__(n,a)
        self.carrera=c
    
    def getcarrera(self):
        return f"{self.carrera}"

juan=Estudiante("Juan", "Salvo", "Ing Química")
nom=juan.getname()
carr=juan.getcarrera()
print(nom)
print(carr)





