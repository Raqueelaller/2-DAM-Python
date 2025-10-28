'''Muestra un menú con opciones:
a) Cuadrado b) Cubo c) Potencia n d) Salir
Según la opción, pide un número (y, si aplica, el exponente) y muestra el resultado.
Pista: usa un bucle while y una función calcular_potencia(base, exp).'''

def calcular_potencia(base: float, exp: int) -> float:
    return base ** exp

bandera = True

while bandera==True:
    print("\nMenú de opciones:")
    print("a) Cuadrado")
    print("b) Cubo")
    print("c) Potencia n")
    print("d) Salir")

    opcion = input("Elige una opción: ").lower()

    match opcion:
        case "a":
            num = float(input("Introduce un número: "))
            print(f"{num} al cuadrado = {calcular_potencia(num, 2)}")
        case "b":
            num = float(input("Introduce un número: "))
            print(f"{num} al cubo = {calcular_potencia(num, 3)}")
        case "c":
            num = float(input("Introduce la base: "))
            exp = int(input("Introduce el exponente: "))
            print(f"{num} elevado a {exp} = {calcular_potencia(num, exp)}")
        case "d":
            print("Saliendo del programa...")
            bandera=False
            break
        case _:
            print("Opción no válida, intenta de nuevo.")
