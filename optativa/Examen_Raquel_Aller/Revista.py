from Material import Material
class Revista(Material):
    contadorRevista=0
    meses = ["enero", "febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre", "diciembre"]
    def __init__(self, titulo: str, autor: str, anyo: int, numeroEdicion:int, mesPublicacion:str) -> None:
        super().__init__(titulo, autor, anyo)
        Revista.contadorRevista=Revista.contadorRevista+1
        if mesPublicacion not in Revista.meses:
            raise ValueError("el mes tiene que ser un mes correcto")
        self.mesPublicacion=mesPublicacion
        self.numeroEdicion=numeroEdicion

    def __str__(self) -> str:
        return f"Revista con id: {self.id},Título: {self.titulo},Autor: {self.autor}, Año: {self.anyo},Número de edición: {self.numeroEdicion},Mes de publicación: {self.mesPublicacion}"