'''Ejercicio 3 — Contador de vocales  
Define una función contar_vocales(cadena: str) -> dict que devuelva un diccionario con el  número  
de apariciones de cada vocal (a, e, i, o, u) en la cadena (sin diferenciar  mayúsculas/minúsculas).  
Pide al usuario una frase y muestra el conteo ordenado de mayor a menor frecuencia.  
'''
import operator
def contar_vocales(cadena: str) -> dict:
    
    contadora = 0
    contadore = 0
    contadori = 0
    contadoro = 0
    contadoru = 0
    for i in cadena:
        if "a" == i:
            contadora= contadora +1
        elif "e" == i:
            contadore=contadore +1
        elif "i" == i:
            contadori=contadori+1
        elif "o"==i:
            contadoro=contadoro+1
        elif "u"==i:
            contadoru=contadoru+1
    
    contador_vocales={"a":contadora,"e":contadore,"i":contadori,"o":contadoro,"u":contadoru}
    contadorOrdenado = sorted(contador_vocales.items(), key=lambda item: item[1], reverse=True)
    print(contadorOrdenado)
    
    
    return contadorOrdenado

def main():
    bandera = False
    while bandera == False:
        cadena = str(input("dime una cadena de texto")).lower()
        if cadena == "salir":
            bandera=True
        else:
            contar_vocales(cadena)
main()




