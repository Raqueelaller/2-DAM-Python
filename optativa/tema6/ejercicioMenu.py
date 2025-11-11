''' Crea un programa que utilice un diccionario para crear un listín telefónico. El
diccionario estará formado por pares (nombre, teléfono).'''


bandera =False

agenda ={
    "Jorge":66666666,
    "Raquel": 66666668,
    "Andrea prima":7787878
}

while bandera == False:
    print("Menú de opciones")
    print("a) Listado de teléfonos, por orden por defecto")
    print("b) Listado de teléfonos, por orden alfabético")
    print("c) Añadir un nuevo contacto")
    print("d) modifica el teléfono de un contacto")
    print("e) Busca un número de teléfono")
    print("f) eliminar un contacto")
    print("g) borrar el listín telefónico")
    print("h) salir")
    print(" ")
    opcion = str(input("dime que opción deseas escoger: "))
    opcion = opcion.lower()

    match opcion:
        case "a":
            print(agenda)

        case "b":
            agenda_ordenada = dict(sorted(agenda.items()))
            print(agenda_ordenada)

        case "c":
            nombre = str(input("dime el nombre de la persona que quieres introducir: "))
            numero = int(input("dime su número de teléfono: "))
            if nombre in agenda:
                print("¡Esa persona ya existe!")
            else:
                agenda[nombre]= numero

        case "d":
            nombre = str(input("dime el nombre de la persona que quieres modificar: "))
            
            if nombre in agenda:
                numero = int(input("dime su nuevo número de teléfono: "))
                agenda [nombre]=numero
                print("modificado correctamente!")
            else:
                pregunta=str(input("¿quieres añadirlo? si o no: "))
                pregunta = pregunta.lower()
                if pregunta == "si":
                    nombre = str(input("dime el nombre de la persona que quieres introducir: "))
                    numero = int(input("dime su número de teléfono: "))
                    agenda[nombre]= numero
                    print("Contacto añadido correctamente!")
                else:
                    print("ok!")
        
        case "e":
                numero = int(input("dime el numero de teléfono de la persona que quieres buscar: "))
                clave = next((k for k, v in agenda.items() if v == numero), None)
                print("El nombre de este contacto es:",clave)
        
        case "f":
            nombre = str(input("dime el nombre de la persona que quieres eliminar: "))
            if nombre in agenda:
                del agenda[nombre]
                print("borrado correctamente")
            else:
                print("no se ha encontrado esta persona")

        case "g":
            pregunta=str(input("¿Estás segur@ que quieres borrar todo el listado? si o no: "))
            pregunta = pregunta.lower()
            if pregunta == "si":
                agenda.clear()
        
        case "h":
            print("Hasta luego!")
            bandera = True