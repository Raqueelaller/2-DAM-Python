from abc import ABC, abstractmethod
class Empleado(ABC):
    idEmpleado=0

    def __init__(self,nombre:str):
        Empleado.idEmpleado= Empleado.idEmpleado +1
        self.nombre=nombre
    
    @abstractmethod
    def calcular_salario(self):
        return
    @abstractmethod
    def __str__(self)->str:
        return f"id:{self.idEmpleado} nombre{self.nombre}"