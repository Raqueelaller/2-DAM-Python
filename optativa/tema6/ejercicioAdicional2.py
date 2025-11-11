''' 2. Modificar el programa anterior para que pueda manejar varios nombres.'''

def crearUsuario(nombre:str, edad:int,direccion:str,telefono:int) -> dict():
    usuario={
        "nombre":nombre,
        "edad":edad,
        "dirección": direccion,
        "teléfono": telefono
    }

    return usuario

bandera = False
lista = []
while bandera == False:
    print("a) mostrar listado")
    print("b) añadir usuario")
    print("c) salir")
    respuesta = str(input("dime la opción: "))
    respuesta=respuesta.lower()
    match respuesta:
        case "a":
            print(lista)
        case "b":
            nombre=str(input("Dime tu nombre: "))
            edad=int(input("Dime tu edad: "))
            direccion= str(input("Cual es tu dirección? "))
            telefono = int(input("¿cual es tu número de teléfono? "))
            usuario=crearUsuario(nombre,edad,direccion,telefono)
            lista.append(usuario)
        case "c":
            bandera=True
            