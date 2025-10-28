#2. Escribe un programa que recoja un número y calcule su factorial.
numero=int(input("dime el número que quieras para calcular su factorial: "))
inicial=1
for i in range (1,numero):
    numero=numero*i
    print(numero)
    
    
