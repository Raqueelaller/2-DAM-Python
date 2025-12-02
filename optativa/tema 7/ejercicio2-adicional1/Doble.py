from Habitacion import Habitacion

class Doble(Habitacion):

    def __init__(self, noche):
        super().__init__(noche)
    
    def calcular_precio(self,respuesta:str):
        respuesta = respuesta.lower()
        precio = self.noche * 75

        if respuesta == "si":
            precio = precio +10
        
        return precio