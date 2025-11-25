from Producto import Producto
class Electronico(Producto):
    descuento= 10
    def __init__(self, nombre, precio) -> None:
        super().__init__(nombre, precio)
        self.descuento
    
    def precio_final(self):
        return super().precio_final()