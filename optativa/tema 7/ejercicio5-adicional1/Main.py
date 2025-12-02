from Auto import Auto
from Vehiculo import Vehiculo
from Camion import Camion
from GestionFlota import GestionFlota

def main():

    tipo=str(input("Quieres hacer un camion o un auto?"))
    if(tipo=="auto"):
        auto1 = Auto("0028LYB","Ibiza",False,5)
    elif(tipo=="camion"):
        camion=Camion("0000xxx","mercedes",True,500)
    else:
        print("opción incorrecta")


    
    auto2 = Auto("0055BBB","ateca",True,5)
    print("Mostrando datos del primer vehiculo")
    GestionFlota.mostrarDatos(auto1)
    print("")
    print("Lista de vehículos disponibles")
    for vehiculo in GestionFlota.listarDisponibles():
        print(vehiculo)
    
    print("")

    GestionFlota.cambiarEstado(auto1)
    print("Cambiando el estado del primer coche")
    GestionFlota.mostrarDatos(auto1)
    GestionFlota.eliminarVehiculo("0000xxx")
    print("Lista de vehículos")
    for vehiculito in Vehiculo.sistema.values():
        print(vehiculito)

main()