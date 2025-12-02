from Empleado import Empleado
class Comisionista(Empleado):
    def __init__(self, nombre,base:float, porcentaje:float ):
        super().__init__(nombre)
        self.base=base
        self.porcentaje=porcentaje
    
    def calcular_salario(self):
        porcentaje=1+self.porcentaje
        salario=self.base*porcentaje
        salario=salario.__round__(2)
        return salario
    
    def __str__(self):
        return f"id: {self.idEmpleado} nombre: {self.nombre} salario: {self.calcular_salario()}" 