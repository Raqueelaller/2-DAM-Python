'''Ejercicio 8 — Tabla de multiplicar extendida
Pide dos enteros a y b (a ≤ b). Muestra, mediante una función imprimir_tablas(a, b),
las tablas de multiplicar desde a hasta b, cada una de 1 a 10. Formatea con columnas
alineadas.'''

numero1 = int(input("dime el primer número: "))
numero2 = int(input("dime el segundo número: "))

for i in range(numero1,numero2+1):
    print("")
    for j in range(1,11):
        multiplicacion = i*j
        print(i,"x",j,"=",multiplicacion)
        