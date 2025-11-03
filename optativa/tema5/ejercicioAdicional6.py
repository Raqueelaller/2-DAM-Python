'''6. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]'''

def interior(lista:list[int])->list[int]:
    return lista[1:-1]

lista=[2,5,3,7,3]

print(interior(lista))