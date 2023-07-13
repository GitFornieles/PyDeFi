
from decimal import DivisionByZero


continuar=True

while continuar==True:
    try:
        a=input("Ingrese el valor A: ")
        a=int(a)
        continuar=False
    except TypeError:
            print("Ingrese un Número")
    except Exception:
            print("Algo pasó")

print(a)
continuar=True
while continuar==True:
    try:
        b=input("Ingrese el valor B: ")
        b=int(b)
        continuar=False
    except TypeError:
            print("Ingrese un Número")
    except Exception:
            print("Algo pasó")

try:
    c=a/b
except:
    c="No se puede dividir por cero"

print("a + b: ", a+b)
print("a - b: ", a+b)
print("a * b: ", a*b)
print("a + b: ", c)