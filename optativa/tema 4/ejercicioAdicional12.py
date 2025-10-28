'''Ejercicio 12 — Repetición controlada de texto
Pide una palabra y un número entero n. Escribe una función repetir_palabra(palabra: str, n:
int) -> str
que devuelva la palabra repetida n veces separada por guiones.
Ejemplo: repetir_palabra('sol', 3) → 'sol-sol-sol'.
Pista: usa un bucle o multiplicación de cadenas y cuida el separador final.'''

def repetir_palabra(palabra: str, n: int) -> str:
    resultado = ""
    for i in range(n):
        resultado = resultado + palabra
        if i < n - 1:   # evita el guion final
            resultado = resultado + "-"
    return resultado

palabra = str(input("dime la palabra a repetir: "))
repeticiones= int(input("dime cuantas veces quieres repetirla"))

print(repetir_palabra(palabra,repeticiones))
