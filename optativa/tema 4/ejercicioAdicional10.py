'''Ejercicio 10 — Normaliza nombres (cadenas)
Escribe una función normaliza_nombre(s: str) -> str que:
- Elimine espacios al inicio/fin y reduzca espacios múltiples internos a uno.
- Convierta a "Title Case" (primera letra de cada palabra en mayúscula, resto minúsculas),
sin usar .title() directamente.
Entrada de ejemplo: " aNa péRez loPEz " → "Ana Pérez Lopez"
Pista: separa por espacios, filtra vacíos, y vuelve a unir con ' '. Usa slicing y
.lower()/.upper().'''
def  normaliza_nombre(s:str)->str:
    s.strip() #quita los espacios del principio y final
    partes = s.split() #separa la cadena de texto en palabras

    palabras=[] 
    for palabra in partes:
        palabra = palabra.lower() 
        if len(palabra)>0:
            palabra = palabra[0].upper() + palabra[1:] #el 1: significa que en la posición 1 y las posiciones siguiente
        palabras.append(palabra)
    resultado = " ".join(palabras)
    return resultado