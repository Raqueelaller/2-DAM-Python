'''Ejercicio 1 — Par o impar con validación  
Escribe una función es_par(n: int) -> bool que devuelva True si n es par y False si es impar.  
A continuación, en un bucle, pide números al usuario hasta que introduzca 'fin'. Por cada  número,  
muestra si es par o impar. Valida que la entrada sea un entero (si no lo es, vuelve a pedirla).  
'''

def es_par(n:int) -> bool:
    if n%2==0:
        print("es par",True)
    else: 
        print("es impar",False)
    

def main():
    bandera = False 
    while bandera == False:
        n= input("dime un número ")
        if(n=="fin"):
            bandera=True
        else:
            try:
                n =int(n)
                es_par(n)
            except ValueError:
                print("dime un número") 

main()



