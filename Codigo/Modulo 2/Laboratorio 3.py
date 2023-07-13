paises = {
"ar": "Argentina",
"es": "España",
"us": "Estados Unidos",
"fr": "Francia"
}

c=""

while c!="SALIR":
    c=input("""ingrese código de pais o ""SALIR"" para cerrar""")
    try:
        print("El pais es: ", paises[c])
    except KeyError:
        if c=="SALIR":
            print("Muchas gracias")
        else: 
            print("Código no encontrado")

