# 1. Escriba un programa que recoja un valor por teclado y muestre de qué tipo
#es.
valor1= input("valor:")
print( type(valor1))
#2. Escribe un programa que recoja dos números enteros por teclado y muestre
#los siguientes resultados: suma, resta, multiplicación, división real, división
#entera, resto de la división entera y potencia.
num1= int(input("numero 1:"))
num2= int(input("numero 2:"))
print("suma " , (num1+num2),1)
print("resta ", (num1-num2))
print("multiplicación ", (num1*num2))
print("division real ", (num1/num2))
print("división entera ", (num1//num2))
print("resto de división entera", (num1%num2))
print("potencia ", (num1**num2))

#3. Escribe un programa que pida el nombre del usuario y le responda con un
#saludo. En el saludo deberá utilizarse el nombre que introdujo el usuario.
nombre= input("dime tu nombre: ")
print("hola",nombre, "como estas?" )
#4. Escribe un programa que recoja tres números y calcule su media aritmética.
num3= int(input("dime el primer número:"))
num4= int(input("dime el segundo número:"))
num5=int(input("dime el tercer número"))
media=(num3+num4+num5)/3
print(media)
#5. Escribe un programa que recoja un número y muestre su valor absoluto.
numero1= int(input("dime un número"))
valor_absoluto=abs(numero1)
print(valor_absoluto)

#6. Escribe un programa que recoja las notas de las tres evaluaciones de un
#alumno. A continuación debe calcular y mostrar la nota final, teniendo en
#cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
#evaluación un 35% y la tercera evaluación un 45%.
nota1= float(input("dame la primera nota: "))
nota2= float(input("dame la segunda nota:"))
nota3= float(input("dame la tercera nota: "))
primera_evaluacion=nota1*0.2
segunda_evaluacion=nota2*0.35
tercera_evaluacion=nota3*0.45

print("la nota final es:",(primera_evaluacion+segunda_evaluacion+tercera_evaluacion))

#7. Escribe un programa que recoja un número y muestre su representación en
#código binario.
num6=int(input("dame un número:"))
print("el número binario es", bin(num6))

#8. Escribe un programa que recoja un texto y lo muestre cinco veces
#consecutivas en la misma línea.
texto1=input("dime lo que quieres repetir:")
print((texto1+" ")*5)

#9. Escribe un programa que recoja un texto y que muestre su longitud,
texto2=input("dime otro texto:")
print("la longitud del texto es:", len(texto2))


#10.Escribe un programa que recoja la edad del usuario y muestre la edad que
#tendrá dentro de 5, 10 y 15 años.
edad= int(input("dime tu edad:"))
print("tu edad dentro de 5 años es:",edad+5,"dentro de 10 años",edad+10,"dentro de 15 años",edad+15)
