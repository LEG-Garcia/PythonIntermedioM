# Arvhivos en Python

'''
"r" Abre un archivo solo para lectura.
"r+" Abre un archivo para lectura y escritura.
"rb" Abre un archivo para lectura solo en formato binario.
"rb+" Abre un archivo para lectura y escritura en formato binario.
"w" Abre un archivo solo para escritura.
"a" Abierto para escritura. El archivo se crea si no existe.
"a+" Abierto para lectura y escritura. El archivo se crea si no existe.
'''

# definir rutas : donde se encuentran los archivos de tipo txt
# Windows \\ Linux y Mac //

RutaEscritorio = 'C:\\Users\\LucyPc\\Desktop\\PythonIntermedioM\\Datos estudiantes.txt'

# abrir el archivo  open(ruta,'r')
# leer un archivo  nombreArchivo.read()

# abrir el archivo y mostrar en la consola todo lo que contiene el archivo
archivoAgenda = open(RutaEscritorio,'r')

'''
print(" ---------- Lo que contienne el archivo --------------------- ")
print(archivoAgenda.read())
print(" ---------- fin de abrir y leer achivo  ----------------------")

'''

# Leer linea por linea con salto de linea
'''

print(" -------------------------------------------------------------")
print(" ----------------Leer linea por linea ------------------------")
print(" -------------------------------------------------------------")

print(archivoAgenda.readline()) # aqui imprime la primera linea del lo que contiene el archivo
print(archivoAgenda.readline()) # aqui imprime la segunda linea
print(archivoAgenda.readline()) # aqui imprime la tercera linea

'''


# Muestra todas las lineas de forma seguida solo que con \n el cual indica que otra linea
'''

print(" -------------------------------------------------------------")
print(" --------------Mostrar todas las lineas ----------------------")
print(" -------------------------------------------------------------")

print(archivoAgenda.readlines()) # aqui imprime todas las lineas que contenga el archivo

'''

# Leer el archivo con un for
'''
print(" -------------------------------------------------------------")
print(" ---------- leer el archivo con for --------------------------")
print(" -------------------------------------------------------------")

# Recordar que cuando se abra un archivo con for se debe de cerrar el archivo con nombreArchivo.close()
for x in archivoAgenda:
    print(x)
archivoAgenda.close()
print("fin Lectura del archivo")

'''

# Escritura datos en nuevo archivo , este permite crear el achivo si no existe

NuevaRutaEscritorio = 'C:\\Users\\LucyPc\\Desktop\\PythonIntermedioM\\Grado academico.txt'

# abrir y escribir datos en el archivo open(ruta,'w')
# podemos crear una variable para definir el contenido = " primaria " o archivo.write("Basico \n")
#  encoding="utf-8" son para los caracteres especiales como la tilde
'''

print(" -------------------------------------------------------------")
print(" ---------------Escritura de un archivo ----------------------")
print(" -------------------------------------------------------------")

contenido = "Primaria \n"
grado = open(NuevaRutaEscritorio, 'w', encoding="utf-8")
grado.write(contenido)
grado.write("Básico \n")
grado.write("Universidad")
grado.close()


#abrir el archivo para verlo en la consola
'''

'''
grado = open(NuevaRutaEscritorio,'r', encoding="utf-8")
print(grado.read())
grado.close()

'''


'''
# abrir el archivo con for para verlo en consola

grado = open(NuevaRutaEscritorio,'r', encoding="utf-8")

for linea in grado.readlines():
    print(linea)
grado.close()

print(" -------------------------------------------------------------")

'''

# Crear Metodos  de lectura y escritura
'''

print(" -------------------------------------------------------------")
print(" ----------- archivo lectura escritura r+ --------------------")
print(" -------------------------------------------------------------")

# Crear lo metodos 

def get_File(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def read_File(archivo):
    contenido = archivo.read()
    return contenido

def Write_File(archivo, texto):
    archivo.write(texto)


#test de los metodos creados arriba

# def get_File(ruta, permiso):
estudiante = get_File('C:\\Users\\LucyPc\\Desktop\\PythonIntermedioM\\Informacion Estudiante.txt', 'r+')  
# read_File(archivo):
print(read_File(estudiante))
#def Write_File(archivo, texto):  tomar en cuenta las mayusculas y minuscas escritas ya que python las reconoce
Write_File(estudiante, " \n María Castillo ")
print(read_File(estudiante))

print(" -------------------------------------------------------------")

'''
# para poder usar JSON se debe de importar el archivo es este caso 
# con import json
#convertir JSON en py

print(" -------------------------------------------------------------")
print(" ----------- -Convertir de JSON a python ---------------------")
print(" -------------------------------------------------------------")

#CLASE ARCHIVOS
import json

'''
# datos en JSON
x = '{"nombre":"Lucía", "edad":32,"departamento":"Sacatepequez"}'
#Conversion
y = json.loads(x)
# el resultado es un diccionaro de python
print(y["departamento"])

print(" -------------------------------------------------------------")
print(" ----------- -Convertir de python a JSON ---------------------")
print(" -------------------------------------------------------------")

# Un objeto dePython  (dict): un diccionario

x = {
    "snombre": "Eleonora",
    "edad"   : 32,
    "municipio": "Antigua Guatemala"
}

# dumps convierte en JSON
y = json.dumps(x)
# Imprimir datos
print(y)

'''

#Convertir todos los Tipos de Datos de Python a JSON

'''
print(" -------------------------------------------------------------")
print(" ----Convertir todos los Tipos de Datos de Python a JSON -----")
print(" -------------------------------------------------------------")

#CONVERTIR TODOS LOS Tipos de Datos DE PY A JSON
print("CONVERTIR TODOS LOS Tipos de Datos DE PY A JSON")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4 , sort_keys= True))