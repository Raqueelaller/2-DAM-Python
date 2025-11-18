from ejecicio1 import Persona
def main():
    persona1=Persona("Raquel","Malaga",673721140)
    persona2=Persona("Jorge","Malaga",666666666)
    persona3=Persona("Andrea","Cártama",888888888)

    bandera =False

    agenda ={
        persona1.nombre:persona1,
        persona2.nombre: persona2,
        persona3.nombre:persona3
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
                for clave, persona in agenda.items():
                    print(f"Nombre:{clave}")
                    print(f"direccion: {persona.direccion}")
                    print(f"teléfono: {persona.telefono}")
                    print("-----------------------")

            case "b":
                agenda_ordenada = dict(sorted(agenda.items()))
                for clave, persona in agenda_ordenada.items():
                    print(f"Nombre: {clave}")
                    print(f"Dirección: {persona.direccion}")
                    print(f"Telefono: {persona.telefono}")
                    print("--------------------------")

            case "c":
                nombre = str(input("dime el nombre de la persona que quieres introducir: "))
                direccion = str(input("dime la dirección de la persona que quieres introducir: "))
                try :
                    numero = int(input("dime su número de teléfono: "))
                except ValueError:
                    print("Error: No has introducido un número válido")

                if nombre in agenda:
                    print("¡Esa persona ya existe!")
                else:
                    agenda[nombre]= Persona(nombre,direccion,numero)

            case "d":
                nombre = str(input("dime el nombre de la persona que quieres modificar: "))
                bandera1 = False
                for clave, persona in agenda.items():
                    if nombre == clave:
                        bandera1= True
                if bandera1 == True :
                    for clave, persona in agenda.items():
                        if nombre == clave:
                            persona.direccion = str(input("dime la dirección de la persona que quieres introducir: "))
                            try :
                                persona.telefono = int(input("dime su número de teléfono: "))
                            except ValueError:
                                print("Error: No has introducido un número válido")
                    
                    print("modificado correctamente!")
                else:
                    pregunta=str(input("¿quieres añadirlo? si o no: "))
                    pregunta = pregunta.lower()
                    if pregunta == "si":
                        nombre = str(input("dime el nombre de la persona que quieres introducir: "))
                        direccion = str(input("dime la dirección de la persona que quieres introducir: "))
                        try :
                            numero = int(input("dime su número de teléfono: "))
                        except ValueError:
                            print("Error: No has introducido un número válido")
                        agenda[nombre]= Persona(nombre,direccion,numero)
                        print("Contacto añadido correctamente")
                    else:
                        ("OK!")
            case "e":
                    try :
                        numero = int(input("dime el número de teléfono del contacto a buscar: "))
                    except ValueError:
                        print("Error: No has introducido un número válido")
                    bandera2 = False
                    for clave, persona in agenda.items():
                        if persona.telefono == numero:
                            bandera2=True
                            print(f"nombre: {persona.nombre}")
                            print(f"dirección : {persona.direccion}")
                    if bandera2 == False:
                        print("Contacto no encontrado :(")
            case "f":
                nombre = str(input("dime el nombre de la persona que quieres eliminar: "))
                bandera3 = False
                for clave, persona in agenda.items():
                    if nombre == clave:
                        bandera3= True
                if bandera3 == True :
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

main()