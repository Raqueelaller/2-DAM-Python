'''7. # Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]'''

def finales(numero:int, lista:list[int]) -> list[int]:
    longitudLista=len(lista)
    return lista[-numero:longitudLista]

lista=[2,5,4,7,9,6]

print(finales(3,lista))