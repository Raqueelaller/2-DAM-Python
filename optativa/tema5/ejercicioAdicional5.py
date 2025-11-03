'''5. Definir la función
# rango : (List[int]) -> List[int]
# tal que rango(xs) es la lista formada por el menor y mayor elemento
# de xs.
# rango([3, 2, 7, 5]) == [2, 7]'''

def rango (lista:list[int])->list[int]:
    numeroBajo=10000000000000000
    numeroAlto=0
    lista2=[int]
    for i in lista:
        if i > numeroAlto:
            numeroAlto=i
        if i < numeroBajo:
            numeroBajo=i
    lista2.append(numeroBajo)
    lista2.append(numeroAlto)
    return lista2

lista=[3,2,7,5]

print("lel número menor y mayor de la lista son:",rango(lista))