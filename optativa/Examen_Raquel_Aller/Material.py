from abc import ABC, abstractmethod
#creo una clase abstracta para forzar que en el listado de materiales no haya un objeto "Material"
class Material(ABC):
    contadorId=0
    listaMateriales={

    }
    def __init__(self, titulo:str, autor:str, anyo:int) -> None:
        Material.contadorId=Material.contadorId+1
        self.titulo=titulo
        self.autor=autor
        self.anyo=anyo
        self.id=Material.contadorId
        Material.listaMateriales[self.contadorId]=self

    @abstractmethod
    def __str__(self) -> str:
        return f"id: {self.id},Título: {self.titulo},Autor: {self.autor}, Año: {self.anyo}"
