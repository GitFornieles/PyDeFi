def conversion(cantidad):
    hh=cantidad//3600
    mm=(cantidad%3600)//60
    ss= cantidad - hh*3600 - mm*60
    if hh<=9 and hh!=0:
        hh= "0"+str(hh)
    elif hh==0:
        hh="00"
    else:
        hh=str(hh)
    if mm<=9 and mm!=0:
        mm= "0"+str(mm)
    elif mm==0:
        mm="00"
    else:
        mm=str(mm)
    if ss<=9 and ss!=0:
        ss= "0"+str(ss)
    elif ss==0:
        ss="00"
    else:
        ss=str(ss)
    resultado= str(hh)+":"+str(mm)+":"+str(ss)
    return resultado


segundos=int(input("Ingrese la cantidad de segundos: "))

tiempo=conversion(segundos)
print(tiempo)

#Reso del profe
# def conversion(segundos):
#     minutos = int(segundos / 60)
#     horas = int(minutos / 60)
#     minutos_resto = minutos - (horas*60) 
#     segundos_resto = segundos - (horas*60*60) - (minutos_resto *60)
#     if horas<10:
#         horast = "0" + str(horas)
#     else:
#         horast = str(horas)
#     if minutos_resto < 10:
#         minutost = "0" + str(minutos_resto)
#     else:
#         minutost = str(minutos_resto)
#     if segundos_resto < 10:
#         segundost = "0" + str(segundos_resto)
#     else:
#         segundost = str(segundos_resto)

#     return(horast + ":" + minutost + ":" + segundost)

# #####################################################

# print(conversion(1000))