from Vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, matricula: str, modelo: str, estado: bool, numeroAsientos:int):
        super().__init__(matricula, modelo, estado)
        if(numeroAsientos<1):
            raise ZeroDivisionError("No puede ser un número de asientos menor que 1")
        else:
            self.numeroAsientos=numeroAsientos

        
    def __str__(self) -> str:
        return f"Matricula: {self.matricula},Modelo: {self.modelo},Estado: {"Disponible" if self.estado else "Servicio"},Numero de asientos: {self.numeroAsientos} "
    
