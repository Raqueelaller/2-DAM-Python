'''2. Definir una función que, al recibir una cadena de texto, cuente cuántas palabras hay y
devuelva dicho valor.'''
def contadorPalabras(texto:str) -> int:
    texto = texto.strip()#quita los espacions iniciales y finales
    partes = texto.split() #separa la cadena de texto en palabras

    palabras=[] 
    for palabra in partes:
        palabras.append(palabra)
    
    return len(palabras)
    

texto=str(input("dime un texto para saber cuantas palabras tiene"))



print("tiene",contadorPalabras(texto),"palabras")