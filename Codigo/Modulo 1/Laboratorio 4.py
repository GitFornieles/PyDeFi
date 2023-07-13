# PRIMERA ALTERNATIVA, AUNQUE NO TRABAJA CON *ARGS (DEFINICIÓN DE CANTIDAD VARIABLE DE INGRESOS)
# PRIMERO DEFINO EL VECTOR, Y LUEGO A ESE VECTOR LO PASO A LA FUNCIÓN PROMEDIAR

# def promedio_variable(vector):
#     l=len(vector)
#     total=0
#     for i in vector:
#         total =+ i
#     return total/l



# print("Ingrese la lista de valores numéricos a promediar. Presione ENTER sin ingresar valor para terminar con la carga")
# variables=[]
# continuar=True
# j=0
# while continuar==True:
#     aux=input("Ingrese valor de posición " + str(j) + ": ")
#     if aux != "":
#         variables.append(int(aux))
#         j=j+1
#     else:
#         continuar=False
# promedio=promedio_variable(variables)
# print(promedio)

#---------------------------------------------------------------------------------------------------------------------
#ver que acá es la cantidad de argumentos lo que puede variar

def promedio2(*valores):
    l=len(valores)
    for i in valores:
        total =+ i
    return total/l

a=promedio2(2, 3, 4, 5, 6, 7)
print(a)
b=promedio2(5,3)
print(b)
c=promedio2(1,2,3,4,5,6,7,8,9,33,44,55,66,77,88)
print(c)

