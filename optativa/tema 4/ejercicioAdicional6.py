'''Implementa funciones c_a_f(c) y f_a_c(f) para convertir entre Celsius y Fahrenheit.
Pide al usuario el sentido de la conversión y el valor numérico, y muestra el resultado con 2
decimales.
Repite hasta que el usuario escriba 'fin'. Controla entradas inválidas.'''

def c_a_f(c:float):
    resultado = (c*(9/5))+32
    return round(resultado,2)
def f_a_c(f:float):
    resultado=(f-32)*(5/9)
    return round(resultado,2)


bandera = False
while bandera == False:
    print()
    print("a)pasar de celsius a farenheit")
    print("b)pasar de farenheit a celsius")
    print("c)fin")
    teclado=str(input("dime qué quieres hacer"))

    if teclado == "a":
        numero=float(input("dime un número"))
        conversion=c_a_f(numero)
        print("son:",conversion,"farenheit")
    elif teclado == "b":
        numero=float(input("dime un número"))
        conversion=f_a_c(numero)
        print("son:",conversion,"celsius")
    elif teclado == "c":
        bandera = True
