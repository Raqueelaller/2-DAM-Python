'''4. Escribe un programa que lea dos textos y compruebe si una es palíndromo de
la otra. El programa debe preguntar si se desea comprobar teniendo en cuenta
mayúsculas/minúsculas o no.'''

texto1 = str(input("dime  el primer texto"))
texto2 = str(input("dime el segundo texto"))

pregunta = str(input("quieres comprobar los palindromos teniendo en cuenta las mayúsculas?"))

if pregunta == "si":
    texto1 = texto1.replace("", " ")
    texto2 = texto2.replace("", " ")
    if texto1[::-1] == texto2:
        print("son palíndromo")
    else:
        print("no son palíndromo")
else:
    texto1 = texto1.replace("", " ").lower()
    texto2 = texto2.replace("", " ").lower()
    if texto1[::-1] == texto2:
        print("son palíndromo")
    else:
        print("no son palíndromo")