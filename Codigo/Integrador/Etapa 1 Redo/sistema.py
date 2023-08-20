import time


menu=[
["Combo Simple (Hamburguesa simple + Bebida + Fritas)",5],
["Combo Doble (Hamburguesa doble + Bebida + Fritas)",6],
["Combo Triple (Hamburguesa Triple + Bebida + Fritas)",7],
["McFlurby (Helado de dulce de leche)",2]
]

pedidosTurno=[]

def validar(texto="Ingrese un número: ",minimo=0):
    while True:
        try:
            temp=input(texto)
            temp=int(temp)
            if(temp>=minimo):
                return temp
            else:
                print("Valor insuficiente. Ingrese nuevamente:  ")
        except:
            print("Debe ingresar un número")

def montoTotal(varMenu,varPedido): # varMenu tiene que tener el formato de la variable "menu", varPedido, un array de cantidades.
    acum=0
    for n in range(0,varPedido.__len__()):
        acum=acum + varMenu[n][1]*varPedido[n]
    return acum

def opc1():
    pedido={"nombre":"",
            "cantidades":[],
            "total":0
            }
    print()
    print("------------------")
    pedido["nombre"]=input("Nombre del cliente:  ")
    print("Ingrese las cantidades de cada menú:")
    for n in menu:
        cant=validar(f"{n[0]}: ")
        pedido["cantidades"].append(cant)
    print()
    total = montoTotal(menu,pedido["cantidades"])
    print()
    print(f"Valor total del pedido: {total}")
    pago=validar("Ingrese Monto Recibido:  ",total)
    vuelto=pago-total
    print(f"Pago efectuado: {pago}")
    print(f"Vuelto a entregar: {vuelto}")
    guardar=input("Confirma pedido? Y/N: ")
    if guardar=="Y":
        pedido["total"]=total
        almacenarPedido(pedido)
    print(pedidosTurno)

def almacenarPedido(pedido):
        print(pedido["cantidades"])
        cantidades= [str(x) for x in pedido["cantidades"]] # convierto el array de cantidades (integer) en array de strings
        newLine=f"{pedido['nombre']}, {time.asctime()}, {','.join(cantidades)}, {pedido['total']}"
        pedidosTurno.append(newLine)

def guardarPedidos():
    #Escribir código para escribir en el archivo ventas.txt el contenido del array pedidosTurno
    return
##############################################################################################

try:
    with open("Codigo\\Integrador\\Etapa 1 Redo\\registro\\ventas.txt","a") as fileVentas:
        print("Archivo cargado")
except:
    with open("Codigo\\Integrador\\Etapa 1 Redo\\registro\\ventas.txt","w") as fileVentas:
        print("Archivo creado")

print("Bienvenido")
nombre=input("Ingrese su nombre:  ")
opc=""
pedidosTurno=[]
while (opc!="3"):
    print(f"Hola {nombre}")
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")
    print("---------------")
    print("1 - Ingresar pedido")
    print("2 - Cambio de turno")
    print("3 - Apagar Sistema")
    print("---------------")
    opc=input("Ingrese opción:  ")
    if opc=="1":
        print("")
        opc1()
        print("")
    elif opc=="2":
        print("")
        print("opcion 2")
        print("")
    elif opc=="3":
        print("")
        print("CHAU!")
        print("")
    else:
        print("")
        print("Ingrese una opción válida")
        print("")


    


