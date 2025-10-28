'''Escribe una función es_primo(n: int) -> bool que determine si n es primo.
Luego, pide un entero N (>1) y muestra todos los números primos hasta N inclusive en una
sola línea.
Optimiza es_primo para que solo pruebe divisores hasta la raíz cuadrada de n.'''

def es_primo(n:int) -> bool:
    if n%2 == 0 and n%3 == 0:
       bandera = False
    elif n==2 and n==3:
        bandera=True
    else :
        bandera = True
    return bandera

def numeros_primos(n:int):
    lista = []
    for i in range (0,n):
        if i%2 != 0 and i%3 != 0:
            lista.append(i)
    return lista
    

numero = int(input("dime un número para saber si es primo o no "))

print(es_primo(numero))

num = int(input("dime un número > 1 "))

numerosprimos = numeros_primos(num)
print(numerosprimos)

