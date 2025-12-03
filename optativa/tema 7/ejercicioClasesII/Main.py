from Persona import Persona
from Cuenta import Cuenta
from CuentaJoven import CuentaJoven
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

main()