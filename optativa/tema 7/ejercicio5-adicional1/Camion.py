from Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, matricula: str, modelo: str, estado: bool, capacidadCarga:int):
        super().__init__(matricula, modelo, estado)
        if(capacidadCarga<0):
            raise ZeroDivisionError("No puede tener una capacidad de carga menor a 0")
        else:
            self.capacidadCarga=capacidadCarga

    def __str__(self) -> str:
        return f"Matricula: {self.matricula},Modelo: {self.modelo},Estado: {"Disponible" if self.estado else "Servicio"},Capacidad Máxima de Carga: {self.capacidadCarga}"
    