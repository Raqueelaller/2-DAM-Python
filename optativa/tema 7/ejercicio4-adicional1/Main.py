from Asalariado import Asalariado
from Comisionista import Comisionista
from PorHora import PorHora
from Empleado import Empleado

def main():

    empleados = [
        Asalariado("Raquel",1050).__str__(),
        PorHora("Gabi",100,10).__str__(),
        Comisionista("Jorge",1200,0.12).__str__()
    ]

    for emp in empleados:
        print(emp)

main()
