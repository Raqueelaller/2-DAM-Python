import random
import math
bandera = False
contador=1
def numAleatorio(teclado):
    numero=random.randint(0,10)
    if numero==teclado:
        print("correcto! :)")
    else:
        print("Incorrecto :(")

def ecuacion(a,b,c):
    try:
        numero1=-(b+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
        numero2=-(b-math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
        print("el primer valor es",numero1,"el seegundo valor es",numero2)
    except ValueError:
        print("ERROR")

def tabla_multiplicar(numero):
    for i in range(0,11):
                multiplicacion= numero*i
                print("número:",numero,"x",i,"=",multiplicacion)

def factorial(numero):
    factorial= math.factorial(numero)
    print("el factorial es", factorial)

def tabla(fila, columna):
    contador = 1  

    for i in range(fila):  
        for j in range(columna):  
            print(random.randint(0,10), end=" ")  
            contador += 1  
        print() 
def operacion (numero):
    resultado1 = numero + numero  
    resultado2=0
    for i in range(1,11):
        resultado1 = resultado1 + resultado2
        resultado2 = resultado1+resultado2
        print(resultado1,resultado2, end=" ")

while bandera == False:
    print("MENÚ DE OPCIONES ")
    print("a) Mostrar un rombo.")
    print("b) Adivinar un número. ")
    print("c) Resolver una ecuación de segundo grado.")
    print("d) Tabla de números.")
    print("e) Cálculo del número factorial de un número. ")
    print("f) Cálculo de un número de la sucesión de Fibonacci.")
    print("g) Tabla de multiplicar.")
    print("h) Salir ")
    print(" ")
    
    opcion = str(input("introduce una opción:"))

    match opcion:
        case "a" | "A":
            fila = (3+1) //2
            for i in range (fila): 
                espacios= fila - i -1
                print(" " * espacios + "*" * contador)
                contador=contador+2
            print("","*")
        case "b" | "B":
            teclado = int(input("dime un número entre 0 y 10"))
            numAleatorio(teclado)
        case "c"|"C":
                a = float(input("dime a: "))
                b = float(input("dime b: "))
                c = float(input("dime c: "))  
                ecuacion(a,b,c)
        case "g"|"G":
            numero=int (input("dime un número para saber su tabla de multiplicar"))
            tabla_multiplicar(numero)
        case "e"|"E":
            numero = int(input("dime de qué número quieres sabe su factorial: "))
            factorial(numero)
        case "d"|"D":
            fila = int(input("Dime el número de filas: "))
            columna = int(input("Dime el número de columnas: "))
            tabla(fila, columna)
            
        case "f"|"F":
            numero=int(input("dame un número para hacer su operación"))
            operacion(numero)
        case "h"|"H":
            bandera = True 
        case _:
            print("Letra errónea, elige otra opción")



