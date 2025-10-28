'''2. Repite el ejercicio anterior, pero ahora lo que se leen son textos. La condición
de finalización será la cadena vacía.'''

listaText = []

text = str(input("dime un texto para guardarlo, déjalo vacío para terminar"))

while(text != ""):
    listaText.append(text)
    text = str(input("dime un texto para guardarlo, déjalo vacío para terminar"))
    
    

print("a) orden introducido")
print(listaText)
print("b) orden creciente")
print(sorted(listaText))
print("c) orden Decreciente")
print(sorted(listaText, reverse=True))
