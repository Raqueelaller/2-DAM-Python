from Producto import Producto
class Comida(Producto):
    descuento= 0
    def __init__(self, nombre, precio) -> None:
        super().__init__(nombre, precio)
        self.descuento
    
    def precio_final(self):
        return self.precio