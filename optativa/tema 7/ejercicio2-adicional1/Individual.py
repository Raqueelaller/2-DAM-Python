from Habitacion import Habitacion
class Individual(Habitacion):
    def __init__(self, noche):
        super().__init__(noche)
    
    def calcular_precio(self):
        precio = self.noche * 50
        return precio