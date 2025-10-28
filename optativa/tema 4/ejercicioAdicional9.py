'''Ejercicio 9 — Validación de contraseña
Define una función es_contrasena_valida(s: str) -> bool que verifique:
- longitud mínima 8
- al menos una mayúscula, una minúscula, un dígito y un símbolo de: !@#$%^&*?
- no puede contener espacios
Pide contraseñas hasta que el usuario introduzca una válida y muestra un mensaje de éxito.
Pista: recorre carácter por carácter y usa .isupper(), .islower() y .isdigit().Ejercicio 9 — Validación de contraseña
Define una función es_contrasena_valida(s: str) -> bool que verifique:
- longitud mínima 8
- al menos una mayúscula, una minúscula, un dígito y un símbolo de: !@#$%^&*?
- no puede contener espacios
Pide contraseñas hasta que el usuario introduzca una válida y muestra un mensaje de éxito.
Pista: recorre carácter por carácter y usa .isupper(), .islower() y .isdigit().'''

def es_contraseña_valida(s: str) -> bool:
    banderaMayuscula = False
    banderaMinuscula = False
    banderaDigito = False
    banderaSimbolo=False
    banderaEspacio = True
    banderaLongitud = True
    banderaTotal = False
    contador = 0
    simbolo="!@#$%^&*?"
    for x in s:
        contador = contador +1
        if x.isupper():
            banderaMayuscula=True
        elif x.islower():
            banderaMinuscula=True
        elif x.isdigit():
            banderaDigito=True
        elif x == " ":
            banderaEspacio=False
        elif x in simbolo:
            banderaSimbolo=True

    
    if contador < 8:
        banderaLongitud=False

    if banderaDigito == True and banderaEspacio == True and banderaLongitud==True and banderaMayuscula==True and banderaMinuscula==True and banderaSimbolo==True:
        banderaTotal= True

    return banderaTotal



bandera = False
while bandera==False:
    texto = str(input("dime una contraseña que quieras crear"))
    bandera = es_contraseña_valida(texto)
    if bandera == True:
        print("contraseña creada con éxito")