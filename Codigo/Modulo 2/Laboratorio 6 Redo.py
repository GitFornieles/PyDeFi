file = open("C:/Users/alefo/OneDrive/Escritorio/PyDeFi/Codigo/Modulo 2/personasRedo.txt","r")

fileContent=file.readlines()

content=[]
for n in fileContent:
    temp=n.strip()
    temp=temp.split(" - ")
    content.append(temp)
diccionario={}
for n in content:
    diccionario[n[0].title()]=int(n[1])
file.close()
print(diccionario)