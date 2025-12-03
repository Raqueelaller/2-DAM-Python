###############################################################
#                       CLASE PERSONA
###############################################################

class Persona:
    def __init__(self, nombre, apellidos, dni, edad):
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_dni(dni)
        self.set_edad(edad)

    # GETTERS
    def get_nombre(self):
        return self._nombre

    def get_apellidos(self):
        return self._apellidos

    def get_dni(self):
        return self._dni

    def get_edad(self):
        return self._edad

    # SETTERS con validación
    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre.upper()

    def set_apellidos(self, apellidos):
        if not isinstance(apellidos, str) or apellidos.strip() == "":
            raise ValueError("Los apellidos no pueden estar vacíos.")
        self._apellidos = apellidos.upper()

    def set_dni(self, dni):
        if not isinstance(dni, str) or dni.strip() == "":
            raise ValueError("El DNI no puede estar vacío.")
        self._dni = dni.upper()

    def set_edad(self, edad):
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = edad

    # MÉTODOS
    def mostrar(self):
        print("\n---- DATOS DE LA PERSONA ----")
        print(f"Nombre: {self._nombre}")
        print(f"Apellidos: {self._apellidos}")
        print(f"DNI: {self._dni}")
        print(f"Edad: {self._edad}")

    def mayorDeEdad(self):
        return self._edad >= 18



###############################################################
#                       CLASE CUENTA
###############################################################

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



###############################################################
#                    CLASE CUENTA JOVEN
###############################################################

class CuentaJoven(Cuenta):
    def __init__(self, titular: Persona, cantidad=0.0, bonificacion=0):
        if not isinstance(titular, Persona):
            raise TypeError("El titular debe ser una Persona.")
        if titular.get_edad() >= 25:
            raise ValueError("El titular debe ser menor de 25 años para Cuenta Joven.")
        super().__init__(titular, cantidad)
        self.set_bonificacion(bonificacion)

    # GETTER / SETTER
    def get_bonificacion(self):
        return self._bonificacion

    def set_bonificacion(self, bonificacion):
        if 0 <= bonificacion <= 100:
            self._bonificacion = bonificacion
        else:
            raise ValueError("La bonificación debe estar entre 0 y 100.")

    # MOSTRAR
    def mostrar(self):
        print("\n----- CUENTA JOVEN -----")
        print("TITULAR:")
        self._titular.mostrar()
        print(f"Saldo actual: {self._cantidad:.2f}€")
        print(f"Bonificación: {self._bonificacion}%")
        print("(Titular válido para Cuenta Joven)")



###############################################################
#                       PROGRAMA PRINCIPAL
###############################################################

def main():
    try:
        # Crear persona adulta para cuenta normal
        p1 = Persona("Carlos", "García López", "12345678A", 30)
        cuenta1 = Cuenta(p1, 500)
        cuenta1.ingresar(200)
        cuenta1.retirar(50)
        cuenta1.mostrar()

        # Crear persona joven para cuenta joven
        p2 = Persona("Lucía", "Martínez Ruiz", "87654321B", 19)
        cuenta_joven = CuentaJoven(p2, 300, 15)
        cuenta_joven.ingresar(100)
        cuenta_joven.retirar(80)
        cuenta_joven.mostrar()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
