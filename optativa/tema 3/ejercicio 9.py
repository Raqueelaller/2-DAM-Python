'''9. Escribe un programa que recoja un número impar. Debe asegurarse de que  sea impar, 
en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez  tenga el número impar 
debe mostrar una pirámide de asteriscos cuya base es  igual al número introducido. 
Por ejemplo, si se introduce el valor 7 se debe  mostrar: '''

numero = 2

while numero%2 ==0:
    numero = int(input("dime un número: "))

    contador=1
    fila = (numero+1) //2
    for i in range (fila): 
        espacios= fila - i -1
        print(" " * espacios + "*" * contador)
        contador=contador+2
 