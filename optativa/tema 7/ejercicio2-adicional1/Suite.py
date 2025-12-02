from Habitacion import Habitacion

class Suite(Habitacion):

    def __init__(self, noche):
        super().__init__(noche)
    
    def calcular_precio(self):
        precio=self.noche*150

        if self.noche>3:
            precio=precio*0.9

        return precio