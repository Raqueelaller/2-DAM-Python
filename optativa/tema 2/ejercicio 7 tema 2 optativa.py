''' 7. Escribe un programa que recoja la hora del día y devuelva un saludo, según
las siguientes reglas:
INTERVALO DE HORAS SALUDO
[7,12) Buenos días
[12, 20) Buenas tardes
En otro caso Buenas noches'''

hora=int(input("dime qué hora es: "))

match hora:
    case n if n>=7 and n<12:
        print("buenos días")
    case n if n>=12 and n<20:
        print("buenas tarde")
    case _:
        print("buenas noches") 


