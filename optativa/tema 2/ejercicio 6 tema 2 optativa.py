'''6. Escribe un programa que muestre la nota final de un alumno a partir de su
calificación numérica (valor decimal), teniendo en cuenta que:
a. Nota menor de 5 es suspenso.
b. Nota entre 5 y 6 (sin llegar) es suficiente.
c. Nota entre 6 y 7 (sin llegar) es bien.
d. Nota entre 7 y 9 (sin llegar) es notable.
e. Nota entre 9 y 10 (sin llegar) es sobresaliente.
f. Nota igual a 10 es matrícula de honor.
g. Cualquier otro valor numérico fuera de este rango es un error.'''
nota=float(input("dime tu nota: "))

if nota<5:
    print("insuficiente")
if nota>=5 and nota<6:
    print("suficiente")
if nota>=6 and nota<7:
    print("bien")
if nota>=7 and nota<9:
    print("notable")
if nota>=9 and nota<10:
    print("sobresaliente")
if nota>=10:
    print("matrícula de honor") 




