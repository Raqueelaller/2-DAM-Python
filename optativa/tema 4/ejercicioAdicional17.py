'''Ejercicio 17 — Contador de caracteres específicos
Función contar_caracter(s: str, c: str) -> int que devuelva cuántas veces aparece el carácter c
en s.
Pista: recorre la cadena con un bucle y suma 1 cuando ch == c.'''
def contar_caracter(s: str, c: str) -> int:
    contador = 0
    for ch in s:
        if ch == c:
            contador += 1
    return contador

cadena = str(input("dime la cadena de texto: "))
letra=str(input("dime la letra que quieres buscar: "))
numero = contar_caracter(cadena,letra)
print(f"la letra {letra}, aparece {numero} veces")
