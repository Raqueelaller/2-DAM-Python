'''3. Escribe un programa que recoja números por teclado hasta que se introduzca  el valor cero. 
A continuación, debe mostrar el número de valores introducidos,  el valor mínimo introducido, el máximo, 
la suma de todos ellos y su media  aritmética (todos los cálculos sin contar el cero) '''
num=int(input("dime un número"))
numMax=num
numMin=num
contador=0
suma=num
media=0
while num != 0:
    num=int(input("dime un número: "))
    if num !=0:
        contador=contador+1
        if num<numMin: 
            numMin=num
        if num>numMax:
            numMax=num
        suma=num+suma
        media=suma/(contador+1)
    
print("número mínimo:",numMin, "número Máximo:", numMax,"suma:", suma, "media:",media)
