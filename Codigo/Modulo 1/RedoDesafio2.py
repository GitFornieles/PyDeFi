def ingresos(arr):
    ingresos={}
    for name in arr:
        if name in ingresos:
            ingresos[name]+=1
        else:
            ingresos[name]=1
    return ingresos

personas=["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]

print(ingresos(personas))