'''7. Escribe un programa que recoja una cadena de texto por teclado y una letra a  
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar  
el número de veces que se repite la letra en el texto.'''

texto = str(input("Dime una cadena de texto: "))
letra= str(input("dime la letra que quieras buscar: "))
letras=[]
contador =0
for i in texto:
    letras.append(i)
    if letra == i:
        contador= contador +1

print("hay",contador,letra)
