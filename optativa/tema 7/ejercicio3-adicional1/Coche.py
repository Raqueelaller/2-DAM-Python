from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, modelo, anyo):
        super().__init__(modelo, anyo)
    
    def calcular_consumo(self,km, litros=5):
        
        return super().calcular_consumo(km,litros)