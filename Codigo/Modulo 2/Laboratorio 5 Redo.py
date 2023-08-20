

diccionario = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

file=open("C:/Users/alefo/OneDrive/Escritorio/PyDeFi/Codigo/Modulo 2/personasRedo.txt","w")

list=[]

for n in diccionario:
        info=f"{n.lower()} - {diccionario[n]}\n"
        list.append(info)
print(list)
file.writelines(list)
file.close()