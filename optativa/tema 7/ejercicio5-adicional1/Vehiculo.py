class Vehiculo:
    idVehiculo=0
    def __init__(self,modelo:str, estado:bool):
        Vehiculo.idVehiculo=Vehiculo.idVehiculo+1
        self.modelo=modelo
        self.estado=estado
    
    