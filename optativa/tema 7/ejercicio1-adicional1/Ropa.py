from Producto import Producto
class Ropa(Producto):
    descuento= 20
    def __init__(self, nombre, precio) -> None:
        super().__init__(nombre, precio)
        self.descuento
    
    def precio_final(self):
        return super().precio_final()