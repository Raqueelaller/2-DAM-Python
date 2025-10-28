'''Ejercicio 18 — Detección de número capicúa
Función es_capicua(n: int) -> bool que determine si el número leído de izquierda a derecha
es igual que de derecha a izquierda.
Pista: convierte a cadena y compara con su inversa.'''
def es_capicua(n: int) -> bool:
    s = str(abs(n))  # Convertir a cadena y asegurar positivo
    return s == s[::-1]

numero = int(input("dime un número para saber si es capicúo"))
print(es_capicua(numero))