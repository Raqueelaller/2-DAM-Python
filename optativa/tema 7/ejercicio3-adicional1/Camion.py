from Vehiculo import Vehiculo
class Camion(Vehiculo):
    def __init__(self, modelo, anyo):
        super().__init__(modelo, anyo)

    def calcular_consumo(self,km,peso:float,litros=20):
        
        if peso.__floor__() >=1:
            incremento=peso*0.1
            consumo=super().calcular_consumo(km,litros)*(incremento+1)
        else:
            consumo=super().calcular_consumo(km,litros)
        return consumo