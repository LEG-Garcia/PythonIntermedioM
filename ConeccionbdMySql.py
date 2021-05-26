#conector
import mysql.connector

mydb = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    password = "Legg2021",
    database = "cursos" # este se agrega cuando  ya se alla creado la base de datos para crear las tablas 

)

mycursor = mydb.cursor()
print("\n--- conecxion de base de datos ---\n")
print(mydb)

# CREAR DB
# mycursor.execute("CREATE DATABASE cursos")

# Crear Tablas
# mycursor.execute("CREATE TABLE cursos (id_curso INT NOT NULL AUTO_INCREMENT PRIMARY KEY, curso VARCHAR(250) NOT NULL, descripcion VARCHAR(250), activa BOOL)")

# ---- Insertar datos a la tabla
'''
sql = "INSERT INTO cursos (curso , descripcion , activa)  values (%s, %s, %s) "
valor = [
    ('Programacion','Progrmar en Python',1),
    ('Base de datos','Mysql Workbench',1),
    ('Calculo','Calculo ',1),
    ('Electronica','Electronica Basica ',1)
]

mycursor.executemany(sql , valor)
mydb.commit()

print(mycursor.rowcount, "insertados")

'''

print("\n--- Mostrar los datos de la tabla Cursos  -----\n")
#SELECT 
mycursor.execute("SELECT * FROM cursos")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Mostrar Base de datos

print("\n--- Mostrar Base de datos -----\n")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
