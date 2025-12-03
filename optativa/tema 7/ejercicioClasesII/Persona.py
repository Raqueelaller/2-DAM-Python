class Persona:
    def __init__(self, nombre, apellidos, dni, edad):
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_dni(dni)
        self.set_edad(edad)

    def get_nombre(self):
        return self._nombre

    def get_apellidos(self):
        return self._apellidos

    def get_dni(self):
        return self._dni

    def get_edad(self):
        return self._edad


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


    def mostrar(self):
        print("\n---- DATOS DE LA PERSONA ----")
        print(f"Nombre: {self._nombre}")
        print(f"Apellidos: {self._apellidos}")
        print(f"DNI: {self._dni}")
        print(f"Edad: {self._edad}")

    def mayorDeEdad(self):
        return self._edad >= 18
