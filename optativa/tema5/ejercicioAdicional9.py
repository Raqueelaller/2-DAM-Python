'''9. Definir la función
# extremos : (int, list[A]) -> list[A]
# tal que extremos(n, xs) es la lista formada por los n primeros
# elementos de xs y los n finales elementos de xs. Por ejemplo,
# extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]'''

def extremos(numero:int,lista:list[int])->list[int]:
    listita = []
    valor=len(lista)
    listita.extend(lista[0:numero])
    listita.extend(lista[(valor-numero):valor])
    return listita

lista=[2,6,7,1,2,4,5,8,9,2,3]

print(extremos(3,lista))