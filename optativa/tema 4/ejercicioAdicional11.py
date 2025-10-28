'''Ejercicio 11 — Contador de dígitos pares e impares
Escribe una función contar_pares_impares(n: int) -> tuple[int, int] que recorra los dígitos de
un número
y devuelva cuántos son pares y cuántos impares.
Ejemplo: n = 4827 → (3 pares, 1 impa)
Pista: usa // y % para extraer dígitos. Convierte temporalmente a positivo si es negativo.'''

def contar_pares_impares(n: int) -> tuple[int, int]:
    n = abs(n)  # asegurar que sea positivo
    pares = 0
    impares = 0

    if n == 0:
        return (1, 0)  # 0 se considera par

    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        n //= 10  # quitar el último dígito

    return (pares, impares)

numero = int(input("dime un número"))
par,impar=contar_pares_impares(numero)
print(f"pares{par}, impares{impar}")