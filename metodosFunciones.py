# repaso de metodos y funciones

'''
Diferencia entre metodo y funcion

metodo : se declara el metodo y se llama
funcion: se declara y devuelve el valor con return

'''

#Metodo
'''
Sintaxis
def nombreMetodo():
    bloque

se llama la funcion para que lo muestre en la consola

nombreMetodo()

'''

def mySaludo():
    print("Hola este en un metodo")

# Llamo a la funcion creada para que lo muestre en la consola
mySaludo()

numero1 =10
numero2= 5
def sumarValores():
    resultado = 0 # empezar el contador en 0
    resultado = numero1 + numero2
    print("La suma de los dos numero es :",resultado)

sumarValores()

#Funcion
'''
Sintaxis de funciones

def nombreFuncion():
    bloque
    return


'''
numero_uno = 5
numero_dos = 20

def multiplicaValores():
    resultado = numero_uno * numero_dos
    return resultado

respuesta = multiplicaValores()

print(respuesta)

print("--------------------------------------------")

# funciones con parametros

'''
Sintaxis
def nombreFuncion(parametro1, parametro2)
'''

def myDatos(pNombre, pApellido):
    print("--------------------------------------------")
    print("---------- funcion dos parametros ----------")
    print("--------------------------------------------")
    print(pNombre + " " + pApellido)

# si se omite un parametro mostrará con error
# myDatos("lucia") mostrar el error
myDatos("Lucía","García")

# funcion con argumentos arbitrarios *args
'''
 * el asterisco significa que espera muchos
'''
print("--------------------------------------------")
print("--funcion con argumentos arbitrarios *args--")
print("--------------------------------------------")

def misAlumnos(*alumnos):
    print("El alumno mas pequeño del listado es: "+ alumnos[3])
misAlumnos("Luis", "Julia", "Sergio", "Lucía", "Rosario", "Estefany", "Juan Fer")

#argumentos con palabras claves
print("--------------------------------------------")
print("-----Argumento con palabras claves----------")
print("--------------------------------------------")

def myAlumno(alumno3,alumno2,alumno1):
    print("el alumno con la mejor nota es: " + alumno2)
myAlumno(alumno1 ="Marcos", alumno3="Vilma", alumno2="Roky")

#Palabras arbitratias 
print("--------------------------------------------")
print("--------   Claves arbitrarias --------------")
print("--------------------------------------------")

'''
 Diccionario **

 '''
def inscritos(**alumnos):
    print("El segundo nombre del alumno : " + alumnos["sNombre"])
inscritos(sNombre = "Eleonora", sApellido = "García ")

# valor predeterminado
print("--------------------------------------------")
print("----------Valor predetermiando -------------")
print("--------------------------------------------")

def myPaises(pais ="España"):
    print("Yo soy del pais de : " + pais)

# llamare a la funcion de paises con diferentes paises pero dejare uno en blanco 
# por ende se tiene predeterminado que si no tiene pais mueste le pasis de España

myPaises("Guatemala")
myPaises("Francia")
myPaises() #debera de mostrar el pais de España
myPaises("Roma")
myPaises("El Salvador")

print("--------------------------------------------")
print("--------- pasar lista como Argumento -------")
print("--------------------------------------------")

def myFrutasFavoritas(fruta):
    for x in fruta:
        print(x)

#Lista de mis frutas
frutas = ["Mango","Banano", "Fresa", "Uva"]

myFrutasFavoritas(frutas)

print("--------------------------------------------")
print("-------- valores devueltos -----------------")
print("--------------------------------------------")

def multiplicaValor(x):
    return 5 * x
resultado = multiplicaValor(2)
print(" El valor del resultado es: " , resultado)

print("--------------------------------------------")
print("------- Recursividad sin retorno -----------")
print("--------------------------------------------")

#Recursividad es llamar a la funcion n veces hasta que se cumpla un condion
def myCuentaRegresiva (numero):
    numero -=1 # aqui desincrementa el valor de numero en -1
    if numero > 0:
        print(numero)
        myCuentaRegresiva(numero)
    else:
        print("fin de la funcion ya que no puede ser menor a:  ", numero)
myCuentaRegresiva(10)


print("--------------------------------------------")
print("---------Recursividad con retorno ----------")
print("--------------------------------------------")

# Factorial de un numero 
'''
factorial se define como el producto de todos los numeros enteros positivos desde 1
5!  es decir 1*2*3*4*5 = 120
entonces el factorial de 5!=120
'''

def myfactorial(numero):
    print ("Valonur inicial del factorial ",numero)
    if numero > 1:
        numero = numero * myfactorial(numero -1)
    print ("Resultado del factorial ",numero)
    return numero

myfactorial(10)

print("--------------------------------------------")
print("--------------------------------------------")