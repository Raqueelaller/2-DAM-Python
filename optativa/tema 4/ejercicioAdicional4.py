'''Crea una función leer_enteros_hasta_fin() -> list[int] que lea enteros desde teclado hasta
que el usuario
introduzca 'fin'. Después, muestra el máximo y el mínimo de la lista con otra función
calcular_extremos(numeros: list[int]) -> tuple[int, int]. Si la lista queda vacía, indica que no
hay datos.'''


def leer_enteros_hasta_fin() -> list[int]:
    lista = []
    entrada = input("Dime un número o 'fin' para terminar: ")
    while entrada.lower() != 'fin':
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print("Por favor, introduce un número válido o 'fin'.")
        entrada = input("Dime un número o 'fin' para terminar: ")
    return lista

def calcular_extremos(numeros: list[int]) -> tuple[int, int]:
    if not numeros:
        print("No hay datos.")
        return None
    maximo = max(numeros)
    minimo = min(numeros)
    print("El mayor es", maximo, "y el menor es", minimo)
    return (maximo, minimo)

# Programa principal
lista = leer_enteros_hasta_fin()
calcular_extremos(lista)



