from Persona import Persona
class Cuenta:
    def __init__(self, titular: Persona, cantidad=0.0):
        if not isinstance(titular, Persona):
            raise TypeError("El titular debe ser un objeto de la clase Persona.")
        self._titular = titular
        self._cantidad = float(cantidad)

    # GETTERS
    def get_titular(self):
        return self._titular

    def get_cantidad(self):
        return self._cantidad

    # MÉTODOS DE OPERACIÓN
    def ingresar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a ingresar debe ser positiva.")
        self._cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        self._cantidad -= cantidad  # Puede quedar en negativo

    # MOSTRAR
    def mostrar(self):
        print("\n----- CUENTA BANCARIA -----")
        print("TITULAR:")
        self._titular.mostrar()
        print(f"Saldo actual: {self._cantidad:.2f}€")
