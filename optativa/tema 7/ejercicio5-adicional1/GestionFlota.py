from Vehiculo import Vehiculo

class GestionFlota:
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def mostrarDatos(cls, vehiculito:Vehiculo):

        if vehiculito.matricula in Vehiculo.sistema:
            vehiculo = Vehiculo.sistema[vehiculito.matricula]
            print(vehiculo)

    
    @classmethod
    def listarDisponibles(cls) -> list:
        lista: list=[]
        for vehiculo in Vehiculo.sistema.values():
            if(vehiculo.estado==True):
                lista.append(vehiculo)
        return lista

    @classmethod
    def cambiarEstado(cls, vehiculito:Vehiculo):
        if(vehiculito.estado==True):
            vehiculito.estado=False
        else:
            vehiculito.estado=True
    @classmethod
    def eliminarVehiculo(cls, matricula:str):
        if matricula in Vehiculo.sistema:
            del Vehiculo.sistema[matricula]
            

                