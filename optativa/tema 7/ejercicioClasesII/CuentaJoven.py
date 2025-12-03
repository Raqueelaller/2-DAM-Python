from Cuenta import Cuenta
from Persona import Persona
class CuentaJoven(Cuenta):
    def __init__(self, titular: Persona, cantidad=0.0, bonificacion=0):
        if not isinstance(titular, Persona):
            raise TypeError("El titular debe ser una Persona.")
        if titular.get_edad() >= 25:
            raise ValueError("El titular debe ser menor de 25 años para Cuenta Joven.")
        super().__init__(titular, cantidad)
        self.set_bonificacion(bonificacion)

    def get_bonificacion(self):
        return self._bonificacion

    def set_bonificacion(self, bonificacion):
        if 0 <= bonificacion <= 100:
            self._bonificacion = bonificacion
        else:
            raise ValueError("La bonificación debe estar entre 0 y 100.")

    def mostrar(self):
        print("\n----- CUENTA JOVEN -----")
        print("TITULAR:")
        self._titular.mostrar()
        print(f"Saldo actual: {self._cantidad:.2f}€")
        print(f"Bonificación: {self._bonificacion}%")
        print("(Titular válido para Cuenta Joven)")
