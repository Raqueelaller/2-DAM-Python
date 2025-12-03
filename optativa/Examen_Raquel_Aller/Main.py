from Material import Material
from Libro import Libro
from Revista import Revista

def estadisticas():
    print(f"Total de materiales registrados: {Material.contadorId}")
    print(f"Número de libros: {Libro.contadorLibro} y revistas: {Revista.contadorRevista} ")
    print(f"Promedio de Páginas para los libros: {Libro.mediaPaginasLibros()}")

def anyadirLibro()->Libro:
    titulo=str(input("dime el título del libro: "))
    autor=str(input("dime el autor: "))
    anyo= int(input("dime el año: "))
    genero= str(input("dime el género"))
    genero=genero.lower()
    numPaginas= int(input("dime el número de páginas: "))
    lire = Libro(titulo,autor,anyo,genero,numPaginas)
    print("libro creado correctamente")
    return lire

def anyadirRevista()->Revista:
    titulo1=str(input("dime el título de la revista: "))
    autor1=str(input("dime el autor: "))
    anyo1= int(input("dime el año: "))
    mes= str(input("dime el mes de publicación: "))
    mes=mes.lower()
    numEdicion= int(input("dime el número de edición: "))
    revista = Revista(titulo1,autor1,anyo1,numEdicion,mes)
    print("revista creada correctamente")
    return revista



def main():
    bandera =False

    while bandera == False:
        print("BIENVENIDX AL MENÚ")
        print("a) Agregar Material ")
        print("b) Listar Materiales")
        print("c) Buscar Material por ID")
        print("d) Eliminar Material")
        print("e) Generar Estadísticas")
        print("f) Salir")
        opcion = str(input("dime que opción deseas escoger: "))
        opcion = opcion.lower()

        match opcion:
            case "a":
                pregunta=str(input("Quieres agregar un libro o una revista? "))
                pregunta=pregunta.lower()
                if pregunta=="libro":
                    titulo=str(input("dime el título del libro: "))
                    autor=str(input("dime el autor: "))
                    try:
                        anyo= int(input("dime el año: "))
                        genero= str(input("dime el género"))
                    except ValueError as e:
                        print(e)
                    genero=genero.lower()
                    numPaginas= int(input("dime el número de páginas: "))
                    try:
                        Libro(titulo,autor,anyo,genero,numPaginas)
                        print("libro creado correctamente")
                    except ValueError as e:
                        print(e)
                elif pregunta == "revista":
                    titulo1=str(input("dime el título de la revista: "))
                    autor1=str(input("dime el autor: "))
                    try:
                        anyo1= int(input("dime el año: "))
                    except ValueError as e:
                        print(e)
                    mes= str(input("dime el mes de publicación: "))
                    mes=mes.lower()
                    numEdicion= int(input("dime el número de edición: "))
                    try:
                        Revista(titulo1,autor1,anyo1,numEdicion,mes)
                    except ValueError as e:
                        print(e)
                    print("revista creada correctamente")
                else:
                    print("No existe esa opción")
            case "b":
                print("Lista de materiales:")
                try:
                    for materiales in Material.listaMateriales.values():
                        print(materiales).__str__
                except ValueError as e:
                    print(e)
            case "c":
                id=int(input("dime la id del material que quieres buscar"))
                if id in Material.listaMateriales.keys():
                    print(Material.listaMateriales[id])
                else:
                    print("No existe un material con esa ID")
            case "d":
                id2=int(input("dime la id del material que quieres eliminar"))
                if id in Material.listaMateriales.keys():
                    print(f"Se ha borrado el material: {Material.listaMateriales[id2]}")
                    del Material.listaMateriales[id]
                else:
                    print("No existe un material con esa ID")
            case "e":
                estadisticas()
            case "f":
                print("Hasta luego!")
                bandera=True
            case _:
                print("Letra errónea, elige otra opción")



main()