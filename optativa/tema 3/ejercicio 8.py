numero=int(input("dime un número: "))

if numero == 2 or numero == 3:
    print("es primo")
elif numero%2 ==0 or numero%3 ==0:   
    print("no es primo")
else:
    print("es primo")