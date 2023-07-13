personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]

nombres=[]
ingresos={}

for i in personas:
    if i not in nombres:
        nombres.append(i)

for i in nombres:
    ingresos[i]=personas.count(i)

print(ingresos)

# REso del profe

# personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]

# ingresos = {}

# for n in personas:
#     if n not in ingresos:
#         ingresos[n] = 1
#     else:
#         ingresos[n] += 1

# print(ingresos)