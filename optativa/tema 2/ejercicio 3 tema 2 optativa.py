#3. Escribe un programa que lea tres números y que muestre los números mayor
#y menor.
num1=int(input("dime el primer número: "))
num2=int(input("dime el segundo número: "))
num3=int(input("dime el tercer número: "))

mayor=num1
menor=num1

if num2 > mayor:
    mayor=num2
if num3 > mayor: 
    mayor=num3
if num2 < menor:
    menor=num2
if num3 < menor:
    menor=num3

print("el número mayor es",mayor,"el número menor es",menor)


