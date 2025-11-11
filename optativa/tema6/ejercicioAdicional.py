'''1. Escribir un programa que pregunte al usuario su nombre, edad,  dirección y teléfono 
y lo guarde en un diccionario. Después debe  mostrar por pantalla el mensaje'''

nombre=str(input("Dime tu nombre: "))
edad=int(input("Dime tu edad: "))
direccion= str(input("Cual es tu dirección? "))
telefono = int(input("¿cual es tu número de teléfono? "))

usuario= {
"Nombre":nombre,
"Edad":edad,
"dirección":direccion,
"teléfono":telefono
}

print(usuario)