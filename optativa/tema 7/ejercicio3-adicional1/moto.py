from Vehiculo import Vehiculo
class Moto(Vehiculo):
    def __init__(self, modelo, anyo):
        super().__init__(modelo, anyo)
    
    def calcular_consumo(self,km, litros=3):
        
        return super().calcular_consumo(km,litros)