'''10.Escribe un programa que recoja un número y muestre un triángulo 
formado por  secuencias decrecientes de números impares. 
Por ejemplo, si se introduce el  5 se debe mostrar: '''

numero = 2

while numero%2 ==0:
    numero = int(input("dime un número: "))

    contador=1

for i in range(1, numero + 1):
    # Calculamos el mayor impar de la fila actual
    mayor_impar = 2 * i - 1
    
    # Imprimimos la secuencia decreciente desde mayor_impar hasta 1 de 2 en 2
    for j in range(mayor_impar, 0, -2):
        print(j, end=" ")
    print()  # salto de línea al terminar la fila