class Vehiculo:
    def __init__(self,modelo,anyo):
        self.modelo=modelo
        self.anyo=anyo
        
    
    def calcular_consumo(self,km,litros):
        coste=(litros/100)*km
        return coste