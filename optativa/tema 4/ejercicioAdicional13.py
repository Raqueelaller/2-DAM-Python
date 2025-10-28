'''Ejercicio 13 — Contar vocales y consonantes (sin listas)
Escribe una función contar_vocales_consonantes(s: str) -> tuple[int, int] que recorra la
cadena y cuente
cuántas vocales y cuántas consonantes tiene. Ignora espacios y signos.
Pista: usa 'aeiouAEIOU' y .isalpha() para detectar letras.'''
def contar_vocales_consonantes(s: str) -> tuple[int, int]:
    vocales = 0
    consonantes = 0
    for c in s:
        if c.isalpha():  # solo letras
            if c in "aeiouAEIOU":
                vocales += 1
            else:
                consonantes += 1
    return (vocales, consonantes)

palabra = str(input("dime el textito que quieras"))

vocales, consonantes = contar_vocales_consonantes(palabra)

print(f"vocales {vocales}, consonantes {consonantes}")