'''8. Definir la función
# segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []'''

def segmento(numero1:int,numero2:int,lista:list[int])->list[int]:
    numero1=numero1-1
    return lista[numero1:numero2]

lista=[3,4,1,2,7,9,0]

print("prueba 1",segmento(3,4,lista))
print("prueba 2",segmento(3,5,lista))
print("prueba 3",segmento(5,3,lista))