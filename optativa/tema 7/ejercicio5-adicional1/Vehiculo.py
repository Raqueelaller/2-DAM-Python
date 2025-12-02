class Vehiculo:
    
    sistema :dict={
        
     }
          

    def __init__(self,matricula:str,modelo:str, estado:bool):
        # if (sistemas.containsKey(matricula))
        # -> throw new Exception("Matricula ya existe")
            self.matricula=matricula
            self.modelo=modelo
            self.estado=estado
            Vehiculo.sistema[self.matricula]=self


    
    def __str__(self) -> str:
        return f"Matricula: {self.matricula},Modelo: {self.modelo},Estado: {"Disponible" if self.estado else "Servicio"}"
    

