from Empleado import Empleado

class PorHora(Empleado):

    def __init__(self, nombre:str,horas:float, tarifa:float ):
        super().__init__(nombre)
        self.horas=horas
        self.tarifa=tarifa
    
    def calcular_salario(self):
        if self.horas<160:
            salario=self.horas*self.tarifa
        else:
            salario=160*self.tarifa

        salario=salario.__round__(2)
        return salario
    
    def __str__(self):
        return f"id: {self.idEmpleado} nombre: {self.nombre} salario: {self.calcular_salario()}"
    

