from Electronico import Electronico
from Comida import Comida
from Ropa import Ropa
from Producto import Producto

def main():
    lechuga = Comida("lechuga",3.8)
    auricular = Electronico("HP",78)
    pantalon=Ropa("pantalon",30)

    print(f"lechuga {lechuga.precio_final()}")
    print(f"auricular {auricular.precio_final()}")
    print(f"pantalon {pantalon.precio_final()}")


main()