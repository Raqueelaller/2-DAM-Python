'''3. Escribe un programa lea un texto y determine si es un palíndromo. Procura
crear una función palindromo(s) -> Bool.'''

def palindromo(s :str) -> bool:
    bandera=False
    s = s.lower().replace(""," ")

    if s == s[::-1]:
        bandera = True
    
    return bandera

texto = str(input("dime el texto para saber si es palíndromo: "))

print(palindromo(texto))