'''Ejercicio 2 — Calculadora básica con funciones  
Implementa cuatro funciones: sumar(a, b), restar(a, b), multiplicar(a, b) y dividir(a, b).  
En un bucle, pide una operación (+, -, *, /) y dos números, muestra el resultado y sigue  
preguntando hasta que el usuario teclee 'salir'. Controla división por cero y entradas  inválidas.  
No uses eval().  
'''

def sumar(a,b):
    suma=a+b
    print("la suma es",suma)

def restar(a,b):
    resta=a-b
    print("La resta es",resta)

def multiplicar(a,b):
    multiplicacion=a*b
    print("La multiplicación es",multiplicacion)

def dividir(a,b):
    try:
        division=a/b
        print("La división es",division)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

def main():
    bandera = False
    while bandera==False:
        opcion = str(input("introduce una opción(+,-,*,/): "))
        match opcion:
            case "+":
                a= input("dime un número: ")
                b=input("dime otro número: ")
                try :
                    a=int(a)
                    b=int(b)
                    sumar(a,b)
                except ValueError:
                    print("ERROR")
            case "-":
                a= input("dime un número: ")
                b=input("dime otro número: ")
                try :
                    a=int(a)
                    b=int(b)
                    restar(a,b)
                except ValueError:
                    print("ERROR")
            case "*":
                a= input("dime un número: ")
                b=input("dime otro número: ")
                try :
                    a=int(a)
                    b=int(b)
                    multiplicar(a,b)
                except ValueError:
                    print("ERROR")
            case "/":
                a= input("dime un número: ")
                b=input("dime otro número: ")
                try :
                    a=int(a)
                    b=int(b)
                    dividir(a,b)
                except ValueError:
                    print("ERROR")
            case "salir":
                bandera= True
            case _:
                print("dime una de las opciones ")

main()


