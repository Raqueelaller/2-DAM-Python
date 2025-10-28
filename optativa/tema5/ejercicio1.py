'''1. Escribe un programa que recoja números de teclado hasta que se introduce un
cero. Luego debe mostrar la secuencia de números de tres modos:
a. En el orden en que se introdujeron.
b. En orden creciente.
c. En orden decreciente.'''

listaNum = []

num = int(input("dime un número para guardarlo, si es 0, se paran de guardar "))

while(num != 0):
    listaNum.append(num)
    num = int(input("dime un número para guardarlo, si es 0, se paran de guardar "))
    
    

print("a) orden introducido")
print(listaNum)
print("b) orden creciente")
print(sorted(listaNum))
print("c) orden Decreciente")
print(sorted(listaNum, reverse=True))
