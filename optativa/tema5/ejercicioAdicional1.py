'''1. Definir una función que, al recibir una cadena de texto, cuente cuántas vocales hay y
devuelva dicho valor.'''
def contadorVocales(texto:str) -> int:
    texto = texto.lower()
    contador=0
    for letras in texto:
        if letras=="a" or letras =="e" or letras == "i" or letras == "o" or letras=="u":
            contador= contador +1
    
    return contador

texto = str(input("dime un text para saber sus vocales"))

print("Hay",contadorVocales(texto),"vocales")
