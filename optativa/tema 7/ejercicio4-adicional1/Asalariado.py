from Empleado import Empleado

class Asalariado(Empleado):
    def __init__(self, nombre:str, salario:float):
        super().__init__(nombre)
        self.salario=salario

    def calcular_salario(self):
        return self.salario
    
    def __str__(self):
        return f"id: {self.idEmpleado} nombre: {self.nombre} salario: {self.calcular_salario()}"
