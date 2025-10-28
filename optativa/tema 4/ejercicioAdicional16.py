'''Ejercicio 16 — Inversión de cadena (sin usar slicing inverso)
Escribe una función invertir_cadena(s: str) -> str que devuelva la cadena invertida.
Ejemplo: 'python' → 'nohtyp'.
Pista: usa un bucle que recorra la cadena al revés con índices o concatenando caracteres al
inicio.'''

def invertir_cadena(s: str) -> str:
    resultado = ""
    for c in s:
        resultado = c + resultado  # añadir cada carácter al inicio
    return resultado

cadena = str(input("dime la cadena para invertirla: "))

print(invertir_cadena(cadena))