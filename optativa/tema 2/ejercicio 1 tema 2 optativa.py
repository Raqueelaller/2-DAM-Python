#1. Escribe un programa que recoja un número e indique si se trata de un número
#par o impar.
numero=int(input("dime un número para saber si es par o impar: "))
if numero % 2 ==0:
    print("el número",numero,"es par")
else:
    print("el número",numero,"no es par")

