# personas={"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
# lista=[]
# for n in personas:
#     lista.append(n +"-"+str(personas[n]))

# with open("Modulo 2\\Laboratorio 5 - personas.txt", "w") as f:
#     for i in lista:
#         f.write(i.lower())
#         f.write("\n")

# Solucion del Profesor

personas={"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

with open("Modulo 2\\Laboratorio 5 - personas.txt", "w") as f:
    for n in personas:
        f.write(f"{n.lower()} - {personas[n]}\n")