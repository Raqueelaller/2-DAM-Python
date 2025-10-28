'''Escribe funciones para dibujar: (a) un triángulo rectángulo de altura h, (b) una escalera de h
peldaños,
(c) un rectángulo de ancho w y alto h. Pide las dimensiones y valida que sean enteros
positivos.
Ejemplo de triángulo h=4:
*
**
***
****'''

def triangulo(a:int):
    for i in range (1,a+1):
        print(i*"*")

def escalera(a:int):
    contador=0
    for i in range(0,a):
        contador=contador+1
        print(contador*"*"," ")

def rectángulo(a:int, b: int):

    contador = 1  

    for i in range(a):  # Bucle externo: recorre las filas
        for j in range(b):  # Bucle interno: recorre las columnas
            print("*", end=" ")  # Imprime el número con espacio fijo
            contador += 1  # Aumentamos el contador en 1
        print()


bandera = False
while bandera == False:
    print()
    print("a)triángulo")
    print("b)escalera")
    print("c)rectángulo")
    print("d)salir")
    teclado=str(input("dime qué quieres hacer"))

    if teclado == "a":
        numero=int(input("dime tamaño de triángulo"))
        if numero>0:
            triangulo(numero)
    elif teclado == "b":
        numero=int(input("dime tamaño de escalera"))
        if numero>0:
            escalera(numero)
    elif teclado == "c":
        fila = int(input("dime el tamaño de las filas"))
        columna= int(input("dime el tamaño de las columnas"))
        if fila > 0 and columna > 0:
            rectángulo(fila,columna)