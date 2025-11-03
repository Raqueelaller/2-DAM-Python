'''11. Definir la función
# intercambia : (tuple[A, B]) -> tuple[B, A]
# tal que intercambia(p) es el punto obtenido intercambiando las
# coordenadas del punto p. Por ejemplo,
# intercambia((2,5)) == (5,2)
# intercambia((5,2)) == (2,5)'''

def intercambia(primera:tuple[int,int])->tuple[int,int]:
    invertida = primera[::-1]
    return invertida

primera = [2,5]
segunda=[5,2]

print(intercambia(primera))
print(intercambia(segunda))