###############################################################
#                   DEFINICIÓN DE UNA CLASE
###############################################################

# Una clase es un molde para crear objetos (instancias).
# Se define con "class Nombre:".

class Persona:

    ###########################################################
    #                ATRIBUTOS DE CLASE (COMUNES)
    ###########################################################
    # Se comparten entre todos los objetos de la clase.
    especie = "Humano"

    ###########################################################
    #                    MÉTODO CONSTRUCTOR
    ###########################################################
    # __init__ se ejecuta al crear un objeto.
    # "self" representa al propio objeto.
    def __init__(self, nombre, edad):
        #######################################################
        #               ATRIBUTOS DE INSTANCIA
        #######################################################
        # Cada objeto tiene sus propios valores.
        self.nombre = nombre      # público
        self._edad = edad         # protegido (convención)
        self.__dni = "12345678A"  # privado (name mangling)


    ###########################################################
    #                    MÉTODOS DE INSTANCIA
    ###########################################################
    # Acceden a atributos de la instancia mediante self.
    def saludar(self):
        print(f"Hola, soy {self.nombre}")


    ###########################################################
    #                       GETTERS Y SETTERS
    ###########################################################
    # Sirven para acceder y modificar atributos "privados".

    def get_dni(self):
        return self.__dni

    def set_dni(self, nuevo_dni):
        # Validación sencilla para el ejemplo
        if len(nuevo_dni) == 9:
            self.__dni = nuevo_dni
        else:
            print("DNI no válido")


    ###########################################################
    #                       MÉTODO DE CLASE
    ###########################################################
    # Se usa @classmethod y CLS en lugar de SELF.
    # Afecta a la clase, no a un objeto concreto.
    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie


    ###########################################################
    #                       MÉTODO ESTÁTICO
    ###########################################################
    # No recibe ni self ni cls.
    # Es como una función normal dentro de la clase.
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18


    ###########################################################
    #                       MÉTODOS ESPECIALES
    ###########################################################

    def __str__(self):
        # Representación "bonita"
        return f"Persona(nombre={self.nombre}, edad={self._edad})"

    def __repr__(self):
        # Representación técnica (para depuración)
        return f"Persona('{self.nombre}', {self._edad})"



###############################################################
#                   HERENCIA BÁSICA
###############################################################

# Una subclase hereda atributos y métodos de la clase padre.

class Estudiante(Persona):

    def __init__(self, nombre, edad, curso):
        # Se llama al constructor de la superclase:
        super().__init__(nombre, edad)
        self.curso = curso

    def saludar(self):
        # Sobrescritura (override)
        print(f"Hola, soy {self.nombre} y estudio {self.curso}")



###############################################################
#               HERENCIA MÚLTIPLE (MUY IMPORTANTE)
###############################################################

class Trabajador:
    def trabajar(self):
        print("Estoy trabajando.")

class EstudianteTrabajador(Estudiante, Trabajador):
    pass


###############################################################
#                POLIMORFISMO
###############################################################

# Diversos objetos pueden usar el mismo método,
# aunque hagan cosas diferentes.

def presentar(persona):
    persona.saludar()  # Cada clase ejecuta su propia versión



###############################################################
#                CLASES ABSTRACTAS
###############################################################

# Se usan para crear "interfaces".
# No se pueden instanciar directamente.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sonido(self):
        pass  # Obliga a las clases hijas a implementar el método


class Perro(Animal):
    def sonido(self):
        print("Guau!")


class Gato(Animal):
    def sonido(self):
        print("Miau!")


###############################################################
#         COMPOSICIÓN Y AGREGACIÓN (RELACIONES ENTRE OBJETOS)
###############################################################

# COMPOSICIÓN → Un objeto contiene a otro y depende de él.

class Motor:
    def arrancar(self):
        print("Motor arrancado.")

class Coche:
    def __init__(self):
        self.motor = Motor()  # El coche "crea" su motor

    def conducir(self):
        self.motor.arrancar()
        print("El coche está en movimiento.")


# AGREGACIÓN → Un objeto recibe otro ya creado (no depende de él)

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Asignatura:
    def __init__(self, profesor):
        self.profesor = profesor  # El profe ya existía antes



###############################################################
#                 DEMOSTRACIÓN FINAL DE TODO
###############################################################

# Crear objetos:
p = Persona("Carlos", 20)
e = Estudiante("Ana", 18, "Python")
dog = Perro()

# Usar métodos:
p.saludar()
e.saludar()
dog.sonido()

# Polimorfismo:
presentar(p)
presentar(e)

# Métodos estáticos y de clase:
print(Persona.es_mayor_de_edad(17))   # False
Persona.cambiar_especie("Mutante")

# Composición:
c = Coche()
c.conducir()

# Acceso a atributos privados mediante getter:
print(p.get_dni())

###############################################################
#                 HERENCIA MÚLTIPLE EN PYTHON
###############################################################

# Una clase puede heredar de MÁS DE UNA clase.
# Python usa el MRO (Method Resolution Order) para decidir
# qué método se ejecuta cuando varias superclases lo tienen.


###############################################################
#               EJEMPLO 1: HERENCIA MÚLTIPLE BÁSICA
###############################################################

class A:
    def accion(self):
        print("Acción desde A")

class B:
    def accion(self):
        print("Acción desde B")

# Hereda de A y B → el orden importa (primero busca en A)
class C(A, B):
    pass

c = C()
c.accion()       # SALIDA: "Acción desde A"
print(C.mro())   # MRO: [C, A, B, object]


###############################################################
#      DIAMOND PROBLEM (PROBLEMA DEL ROMBO) + super()
###############################################################
#     A
#    / \
#   B   C
#    \ /
#     D
# Esto demuestra cómo Python resuelve conflictos entre métodos.


class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")
        super().saludar()   # IMPORTANTE

class C(A):
    def saludar(self):
        print("Hola desde C")
        super().saludar()   # IMPORTANTE

class D(B, C):
    def saludar(self):
        print("Hola desde D")
        super().saludar()   # super() sigue el MRO

d = D()
d.saludar()

# SALIDA:
# Hola desde D
# Hola desde B
# Hola desde C
# Hola desde A
#
# IMPORTANTE ● super() NO VA a la clase padre directa,
# sino al siguiente elemento según el MRO.


###############################################################
#                 CONSULTAR EL ORDEN MRO
###############################################################

print(D.mro())
# SALIDA:
# [D, B, C, A, object]


###############################################################
#                  MIXINS (MUY IMPORTANTE)
###############################################################
# Un Mixin es una clase que aporta funcionalidad EXTRA,
# pero no debe instanciarse por sí sola.
# Se usa para “mezclar” comportamientos.


class LoggerMixin:
    def log(self, mensaje):
        print(f"[LOG]: {mensaje}")


class GuardarMixin:
    def guardar(self, dato):
        print(f"Guardando '{dato}' en la base de datos.")


# Clase principal que usa mixins:
class Usuario(LoggerMixin, GuardarMixin):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar(self):
        self.log(f"Mostrando usuario {self.nombre}")  # Método del Mixin


u = Usuario("Ana")
u.mostrar()
u.guardar("registro")


###############################################################
#           CONTROL FINO DE LA HERENCIA MÚLTIPLE
###############################################################

# Ejemplo donde cada clase añade algo con super()

class X:
    def proceso(self):
        print("Proceso en X")
        super().proceso()

class Y:
    def proceso(self):
        print("Proceso en Y")
        super().proceso()

class Z:
    def proceso(self):
        print("Proceso final en Z")  # No llama super() → final


class M(X, Y, Z):
    pass

m = M()
m.proceso()

# SALIDA:
# Proceso en X
# Proceso en Y
# Proceso en Z


###############################################################
#     EJEMPLO REAL: Herencia múltiple con validaciones
###############################################################

class ValidarNombreMixin:
    def validar_nombre(self, nombre):
        return nombre.isalpha()

class ValidarEdadMixin:
    def validar_edad(self, edad):
        return 0 < edad < 120


class Persona(ValidarNombreMixin, ValidarEdadMixin):
    def __init__(self, nombre, edad):
        if not self.validar_nombre(nombre):
            raise ValueError("Nombre inválido")
        if not self.validar_edad(edad):
            raise ValueError("Edad inválida")

        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 20)   # Correcto


###############################################################
#          EJEMPLO FINAL PARA ENTENDER BIEN EL ORDEN
###############################################################

class A:
    def msg(self):
        print("Soy A")

class B(A):
    def msg(self):
        print("Soy B")
        super().msg()

class C(A):
    def msg(self):
        print("Soy C")
        super().msg()

class D(B, C):
    pass

d = D()
d.msg()

# Orden MRO en D:
# D → B → C → A → object
