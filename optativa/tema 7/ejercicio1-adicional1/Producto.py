class Producto:
    descuento=0
    def __init__(self,nombre,precio) -> None:
        self.nombre= nombre
        self.precio=precio
        self.descuento

    
    def precio_final(self):
        procentaje=1 -(self.descuento/100) 
        return self.precio*procentaje