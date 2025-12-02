from Camion import Camion
from Coche import Coche
from moto import Moto

def main():
    coche= Coche("seat",2000)
    moto= Moto("Honda",2000)
    camion=Camion("Mercedes",2000)

    print(f"El coche consume {coche.calcular_consumo(200,10)} en 200km")
    print(f"La moto consume {moto.calcular_consumo(200)} en 200km")
    print(f"El camión consume {camion.calcular_consumo(200,2) }en 200km")


main()