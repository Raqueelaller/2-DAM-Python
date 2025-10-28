'''4. Escribe un programa que recoja un número y muestre un triángulo. Por  ejemplo, si se ha introducido el valor 5, se debe mostrar: 
* 
** 
*** 
**** 
***** 
Ayuda: La función print introduce por defecto un salto de línea al final del texto.  Para modificar este comportamiento 
por defecto se puede utilizar el parámetro  end para indicar otro valor. Por ejemplo, print(texto, end=””) 
escribe el texto  indicado y como final de línea pone la cadena vacía (es decir, nada). Por tanto,  
el siguiente texto que se escriba se muestra en la misma línea.'''
num=int(input("dime un número"))

for i in range(1,num+1):
    print("*"*i)

