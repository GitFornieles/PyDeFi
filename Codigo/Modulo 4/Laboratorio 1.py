import sqlite3

conexion=sqlite3.connect("eduit_PRODUCTOS.sqlite")

cursor=conexion.cursor()

cursor.execute("CREATE TABLE productos (id int primary key, nombre varchar(20) not null, precio int not null)")

articulos=[
    [1, "Teclado", 25],
    [2, "Mouse", 18],
    [3, "Monitor", 300],
    [4, "Parlantes", 100]
    ]

for n in articulos:
    cursor.execute("insert into productos values (?,?,?)", n)

conexion.commit()
conexion.close()

