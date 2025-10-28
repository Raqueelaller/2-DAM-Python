'''5. Escribe un programa que calcule el precio de entrada a un museo a partir de
la edad del visitante, teniendo en cuenta que:
a. Menores de 5 años entran gratis.
b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
d. Jubilados entran gratis.'''
edad=int(input("dime tu edad para que sepas el precio de tu entrada: "))
precio=0
if edad<5:
    precio=0
elif edad>=5 and edad<18:
    precio=3
elif edad>=18 and edad<65:
    precio=6
elif edad>=65:
    precio=0

print("te cuesta la entrada:",precio)
