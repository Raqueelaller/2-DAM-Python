'''10. Las dimensiones de los rectángulos puede representarse
# por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y
# altura 3.
#
# Definir la función
# mayorRectangulo : (tuple[float, float], tuple[float, float])
# -> tuple[float, float]
# tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre
# r1 y r2. Por ejemplo,
# mayorRectangulo((4, 6), (3, 7)) == (4, 6)
# mayorRectangulo((4, 6), (3, 8)) == (4, 6)
# mayorRectangulo((4, 6), (3, 9)) == (3, 9)'''

def mayorRectangulo(primer:tuple[float,float], segundo:tuple[float,float])->tuple[float,float]:
    resultado = []
    if (primer[0]*primer[1]) > (segundo[0]*segundo[1]):
        resultado=primer
    else:
        resultado=segundo
    return resultado

primero=[4,6]
segundo=[3,9]

print(mayorRectangulo(primero,segundo))