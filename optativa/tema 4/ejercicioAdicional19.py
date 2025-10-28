'''Ejercicio 19 — Convertidor de mayúsculas/minúsculas
Pide una frase y una opción:
a) Convertir a mayúsculas
b) Convertir a minúsculas
c) Capitalizar (solo primera letra en mayúscula)
Implementa funciones separadas para cada caso.
Pista: usa .upper(), .lower(), .capitalize().'''

def a_mayusculas(frase: str) -> str:
    return frase.upper()

def a_minusculas(frase: str) -> str:
    return frase.lower()

def capitalizar(frase: str) -> str:
    return frase.capitalize()

bandera = True
while bandera== True:
    print("\nOpciones de conversión:")
    print("a) Convertir a mayúsculas")
    print("b) Convertir a minúsculas")
    print("c) Capitalizar")
    print("d) Salir")

    opcion = input("Elige una opción: ").lower()

    match opcion:
        case "a":
            frase = input("Introduce la frase: ")
            print(a_mayusculas(frase))
        case "b":
            frase = input("Introduce la frase: ")
            print(a_minusculas(frase))
        case "c":
            frase = input("Introduce la frase: ")
            print(capitalizar(frase))
        case "d":
            print("Saliendo del programa...")
            bandera = False
        case _:
            print("Opción no válida, intenta de nuevo.")