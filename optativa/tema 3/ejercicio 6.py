'''6. Escribe un programa que recoja un número de filas y columnas, y muestre una 
tabla con tantas filas y columnas como indicadas, numerando las celdas de  izquierda a derecha y de arriba abajo. 
Por ejemplo, si se introducen 2 filas y 3  columnas, se debe mostrar: '''

fila = int(input("Dime el número de filas: "))
columna = int(input("Dime el número de columnas: "))

contador = 1  

for i in range(fila):  # Bucle externo: recorre las filas
    for j in range(columna):  # Bucle interno: recorre las columnas
        print(f"{contador:4}", end=" ")  # Imprime el número con espacio fijo
        contador += 2  # Aumentamos el contador en 1
        if contador == 99:
            contador=1
    print()  # Hace un salto de línea después de cada fila