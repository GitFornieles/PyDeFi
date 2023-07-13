def tictoc(num):
    horas=0
    minutos=0
    segundos=0
    horas=num//3600
    minutos=(num-(horas*3600))//60
    segundos=num-(horas*3600+minutos*60)
    rta= str(horas) + ":" + str(minutos) + ":" + str(segundos)
    return rta
print(tictoc(1000))