nombres=["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]
def titular(lista):
    resultado=[]
    for i in lista:
        resultado.append(i.title())
    return resultado

titulados=titular(nombres)
print(titulados)


