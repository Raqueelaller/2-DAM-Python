#2. Escribe un programa que recoja un número por teclado y muestre el día de la
#semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número
#incorrecto, mostrará el mensaje “Día de la semana incorrecto”.
diasem=int(input("dime un número para decirte el día de la semana del 1 al 7: "))

match diasem:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miércoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sábado")
    case 7:
        print("domingo")
    case _:
        print("Día de la semana incorrecto")