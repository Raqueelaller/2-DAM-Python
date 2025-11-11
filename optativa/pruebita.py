def reemplazarVocales(frase:str ,caracter:str):
    frase.lower()
    palabra = ""
    for letra in frase:
        
        if letra == "a":
            letra=caracter
        elif letra == "e": 
            letra=caracter
        elif letra == "i" :
            letra=caracter
        elif letra == "o":
            letra=caracter
        elif letra == "u": 
            letra=caracter
        palabra=palabra+letra
    return palabra

print(reemplazarVocales("hola mundo","*"))

''' while bandera == True:
            numero=int(input("introduce un número "))
            
            contador=contador+1
            if numero < numero2:
                numero2=numero
                print("el número introducido es mayor al anterior")
            if contador==numerosAIntroducir:
                bandera=False'''
'''def numeroMayor(numerosAIntroducir:int):
    bandera = True
    numero2=int
    contador=0
    try:
       for i in range(numerosAIntroducir):
           (numero+i)=int(input("dime un número"))
           if 
    except(TypeError):
        print("tipo no correcto")

numeroMayor(4)'''

'''def rectangulo(filas:int, columnas:int):
    contador = 1  
    try:
        for i in range(filas):  # Bucle externo: recorre las filas
            for j in range(columnas):  # Bucle interno: recorre las columnas
                print(f"{contador:4}", end=" ")  # Imprime el número con espacio fijo
                contador += 2  # Aumentamos el contador en 1
                if contador == 99:
                    contador=1
            print()
    except (ValueError,TypeError):
        print("Error, introduce un valor apropiado")

print(rectangulo("a",12))'''
'''
def contador(cadena: str) -> dict:
    cadena.lower()
    contadora = 0
    contadorb = 0
    contadorc = 0
    contadord = 0
    contadore = 0
    contadorf=0
    contadorg=0
    contadorh = 0
    contadori = 0
    contadorj = 0
    contadork = 0
    contadorl = 0
    contadorm=0
    contadorn=0
    contadorñ = 0
    contadoro = 0
    contadorp = 0
    contadorq = 0
    contadorr = 0
    contadors=0
    contadort=0
    contadoru = 0
    contadorv = 0
    contadorw = 0
    contadorx = 0
    contadory = 0
    contadorz=0

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
        elif "b"==i:
            contadorb=contadorb+1
        elif "c" == i:
            contadorc=contadorc+1
        elif "d" == i:
            contadord=contadord+1
        elif "f" == i:
            contadorf=contadorf+1
        elif "g" == i:
            contadorg = contadorg + 1

        '''
def contadorPalabras(texto:str) -> str:
    texto = texto.strip()#quita los espacions iniciales y finales
    partes = texto.split() 
    elegida=""
    mayor=0
    for palabra in partes:
        if len(palabra) > mayor:
            mayor=len(palabra)
            elegida = palabra
        contar=len(palabra)
    return elegida

print(contadorPalabras("oooolaaaaaa mundo coooomo estas"))