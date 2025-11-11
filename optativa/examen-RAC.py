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

def rectangulo(filas:int, columnas:int):
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

def contadorPalabras(texto:str) -> str:
    texto = texto.strip()
    partes = texto.split() 
    elegida=""
    mayor=0
    for palabra in partes:
        if len(palabra) > mayor:
            mayor=len(palabra)
            elegida = palabra
        contar=len(palabra)
    return elegida

bandera=False
while bandera == False:
    print("MENÚ DE OPCIONES ")
    print("a) Reemplazar vocales de una frase")
    print("b) Mensaje cuando el numero introducido no sea mayor que el primero ")
    print("c) Encontrar la primera palabra más larga")
    print("d) Mostrar rectángulo con números impares entre 0 y 100")
    print("e) Contar la aparición de cada carácter en una palabra ")
    print("f) Salir")
    print(" ")
    
    opcion = str(input("introduce una opción:"))

    match opcion:
        case "a" | "A":
          palabra=str(input("dime una palabra: "))
          caracter= str(input("dime el caracter para remplazar por la vocal"))
          print(reemplazarVocales(palabra,caracter))

        #case "b" | "B":
            

        case "c"|"C":
             palabra=str(input("dime la cadena de caracteres"))
             print("la palabra mas larga es:",contadorPalabras(palabra))

        #case "e"|"E":
            

        case "d"|"D":
            filas=int(input("dime el número de filas"))
            columnas=int(input("dime el número de columnas"))
            print(rectangulo(filas,columnas))

        case "f"|"F":
            print("hasta pronto!")
            bandera = True
    
        case _:
            print("Letra errónea, elige otra opción")