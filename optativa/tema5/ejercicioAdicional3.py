'''3. Definir una función que devuelva la suma dos números. Utilizar esa función para sumar tres
números.'''

def suma(numero1:int, numero2:int) -> int:
    resultado = numero1 +numero2

    return resultado

numero1 = int(input("dime el primer número"))
numero2=int(input("dime el segundo número"))
resultado=suma(numero1,numero2)
numero3=int(input("dime el tercer número"))

print("la suma de los tres número sería:",suma(resultado,numero3))