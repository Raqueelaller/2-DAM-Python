#4. Escribe un programa que recoja dividendo y divisor, y realice su división
#siempre que el divisor sea distinto de cero.
dividendo=int(input("dime el dividendo: "))
divisor=int(input("dime el divisor"))

if divisor==0:
    print("no puede ser el divisor igual a 0")
else:
    division=dividendo/divisor
    print("división:",division)

