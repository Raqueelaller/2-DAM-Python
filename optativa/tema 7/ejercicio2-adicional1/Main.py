from Individual import Individual
from Doble import Doble
from Suite import Suite

def main():
        
    noches=int(input("Cuantas noches quiere pasar en nuestro hotel?"))
    tipo=str(input("quiere individual, doble o suite?"))
    tipo=tipo.lower()
    if tipo=="individual":
        individual1=Individual(noches)
        precio=individual1.calcular_precio()
        print(f"El precio por {noches} en este tipo de habitación es de {precio}")
    elif tipo=="doble":
        doble1=Doble(noches)
        desayuno=str(input("Quiere desayuno? si/no"))
        print(f"El precio por {noches} en este tipo de habitación es de {doble1.calcular_precio(desayuno)}")
    elif tipo=="suite":
        suite1=Suite(noches)
        print(f"El precio por {noches} en este tipo de habitación es de {suite1.calcular_precio()}")
    else:
        print("Opción no válida")


main()