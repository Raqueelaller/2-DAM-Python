from Material import Material
class Libro(Material):
    contadorLibro=0
    ListaGenero= ["ficcion", "no ficcion", "terror", "ciencia"]
    contadorPaginas=0
    def __init__(self, titulo: str, autor: str, anyo: int, genero:str, numeroPaginas:int) -> None:
        super().__init__(titulo, autor, anyo)
        Libro.contadorLibro=Libro.contadorLibro+1
        if genero not in Libro.ListaGenero:
            raise ValueError(f"El género tiene que estar dentro de la lista {Libro.ListaGenero}")
        
        self.genero=genero
        if numeroPaginas<0:
            raise ValueError("el número de páginas tiene que ser mayor que 0")
        self.numeroPaginas = numeroPaginas
        Libro.contadorPaginas= Libro.contadorPaginas + numeroPaginas


    def __str__(self) -> str:
        return f"Libro con id: {self.id},Título: {self.titulo},Autor: {self.autor}, Año: {self.anyo},Género: {self.genero},Número de páginas: {self.numeroPaginas}"
    
    @staticmethod
    def mediaPaginasLibros()->int: #m´ñetodo estático en el que se calcula la media de número de páginas
        media= Libro.contadorPaginas/Libro.contadorLibro
        media = media.__floor__()
        return media