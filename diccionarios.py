###############################################################
#                      DICCIONARIOS EN PYTHON
###############################################################

# Un diccionario es una estructura de datos que almacena pares
# CLAVE : VALOR. Las claves NO se pueden repetir.

# Ejemplo básico:
persona = {
    "nombre": "Ana",
    "edad": 23,
    "ciudad": "Madrid"
}

# Acceder a un valor:
print(persona["nombre"])  # → Ana

# Añadir un nuevo par:
persona["profesion"] = "Ingeniera"

# Modificar un valor existente:
persona["edad"] = 24

# Eliminar un elemento:
del persona["ciudad"]

# Métodos importantes de diccionarios:

# .get(clave) → Devuelve valor o None si no existe
print(persona.get("nombre"))

# .keys() → Devuelve lista de claves
print(persona.keys())

# .values() → Devuelve lista de valores
print(persona.values())

# .items() → Devuelve lista de tuplas (clave, valor)
print(persona.items())

# .pop(clave) → Elimina una clave y devuelve su valor
persona.pop("edad")

# .update(otro_diccionario) → Fusionar diccionarios
persona.update({"edad": 30, "ciudad": "Toledo"})

###############################################################
#                    CREACIÓN DE DICCIONARIOS
###############################################################

# Diccionario vacío:
dic = {}

# Diccionario con elementos:
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Madrid"
}

# También se puede crear así:
persona2 = dict(nombre="Ana", edad=30)



###############################################################
#                       ACCEDER A DATOS
###############################################################

# Acceder por clave:
print(persona["nombre"])   # Carlos

# Evitar error si la clave no existe → usar .get()
print(persona.get("altura"))      # None
print(persona.get("altura", 0))   # Puedes dar un valor por defecto


###############################################################
#                  AÑADIR O MODIFICAR VALORES
###############################################################

# Añadir nueva clave:
persona["profesion"] = "Ingeniero"

# Modificar valor:
persona["edad"] = 26

# Añadir varios a la vez con update():
persona.update({
    "ciudad": "Sevilla",
    "altura": 175
})



###############################################################
#                        ELIMINAR DATOS
###############################################################

# Eliminar una clave:
del persona["altura"]

# Eliminar y obtener el valor eliminado:
valor = persona.pop("edad")   # elimina "edad"

# Eliminar último elemento insertado (Python 3.7+):
persona.popitem()

# Vaciar diccionario
persona.clear()



###############################################################
#                   COMPROBAR EXISTENCIA (IF)
###############################################################

# Comprobar si existe una clave:
if "nombre" in persona:
    print("La clave 'nombre' existe")

# Comprobar si NO existe:
if "altura" not in persona:
    print("No tiene altura")

# Comprobar si un valor está en los valores:
if "Sevilla" in persona.values():
    print("La persona vive en Sevilla")



###############################################################
#                       RECORRER DICCIONARIOS
###############################################################

persona = {"nombre": "Ana", "edad": 20, "curso": "Python"}

# Recorrer solo claves:
for clave in persona:
    print(clave)

# Recorrer claves (forma explícita):
for clave in persona.keys():
    print(clave)

# Recorrer valores:
for valor in persona.values():
    print(valor)

# Recorrer clave y valor:
for clave, valor in persona.items():
    print(clave, "→", valor)



###############################################################
#               BUSCAR POR VALOR (DICCIONARIO)
###############################################################

# Encontrar clave a partir de un valor concreto:
def buscar_clave_por_valor(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    return None  # si no existe

print(buscar_clave_por_valor(persona, "Ana"))  # nombre



###############################################################
#          BUSCAR POR CONDICIONES / FILTRAR (IMPORTANTE)
###############################################################

# Crear un nuevo diccionario con claves que cumplan una condición

edades = {
    "Juan": 15,
    "Ana": 22,
    "Luis": 17,
    "Marta": 30
}

# Encontrar mayores de edad
mayores = {nombre: edad for nombre, edad in edades.items() if edad >= 18}

print(mayores)  # {'Ana': 22, 'Marta': 30}



###############################################################
#        ENCONTRAR POSICIÓN (LOS DICCIONARIOS NO TIENEN)
###############################################################

# No existe "posición" en diccionarios porque NO están ordenados como una lista.
# PERO puedes simular una posición usando enumerate:

for i, (clave, valor) in enumerate(persona.items()):
    print("Posición", i, "→", clave, valor)



###############################################################
#                    COPIAR DICCIONARIOS
###############################################################

# Copia superficial (shallow copy):
copia = persona.copy()

# Copia fiable:
copia2 = dict(persona)



###############################################################
#                     DICCIONARIOS ANIDADOS
###############################################################

alumnos = {
    "A1": {"nombre": "Ana", "nota": 9},
    "A2": {"nombre": "Luis", "nota": 7}
}

# Acceder a un valor dentro de otro diccionario:
print(alumnos["A1"]["nota"])  # 9



###############################################################
#             ORDENAR DICCIONARIOS (MUY IMPORTANTE)
###############################################################

# Ordenar por clave:
ordenado_claves = dict(sorted(edades.items()))
print(ordenado_claves)

# Ordenar por valor:
ordenado_valores = dict(sorted(edades.items(), key=lambda x: x[1]))
print(ordenado_valores)



###############################################################
#          CONVERTIR DICCIONARIOS A LISTAS (IMPORTANTE)
###############################################################

# Lista de claves:
lista_claves = list(persona.keys())

# Lista de valores:
lista_valores = list(persona.values())

# Lista de pares (clave, valor):
lista_items = list(persona.items())



###############################################################
#           CREAR DICCIONARIO A PARTIR DE LISTAS
###############################################################

claves = ["nombre", "edad", "curso"]
valores = ["Carlos", 20, "Python"]

nuevo_dic = dict(zip(claves, valores))
print(nuevo_dic)



###############################################################
#              CONTAR FRECUENCIAS CON DICCIONARIO
###############################################################

texto = "python es genial y python es potente"
frecuencias = {}

for palabra in texto.split():
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print(frecuencias)



###############################################################
#            USO AVANZADO: setdefault() Y fromkeys()
###############################################################

# setdefault() → Si la clave no existe, la crea
d = {}
d.setdefault("nombre", "Desconocido")
print(d)

# fromkeys() → Crear diccionario con claves dadas y mismo valor:
claves = ["a", "b", "c"]
dicc = dict.fromkeys(claves, 0)
print(dicc)



###############################################################
#            VALIDACIÓN DE DATOS (DNI, TELÉFONO, ETC.)
###############################################################

import re  # Módulo para expresiones regulares, muy útil para validar.

################# VALIDAR DNI ESPAÑOL #########################

# Un DNI válido tiene 8 números + 1 letra
# Ejemplo correcto: 12345678Z

def validar_dni(dni):
    # Expresión regular: 8 dígitos + una letra mayúscula
    patron = r"^[0-9]{8}[A-Z]$"
    if re.match(patron, dni):
        return True
    else:
        return False


################ VALIDAR MATRÍCULA ESPAÑOLA ###################

# Formato nuevo: 1234 ABC
# 4 números + espacio + 3 letras

def validar_matricula(m):
    patron = r"^[0-9]{4}\s?[A-Z]{3}$" 
    # \s? = espacio opcional
    return bool(re.match(patron, m))


################ VALIDAR TELÉFONO ESPAÑOL ####################

# Un teléfono español tiene 9 dígitos y empieza por 6, 7, 8 o 9.

def validar_telefono(t):
    patron = r"^[6789][0-9]{8}$"
    return bool(re.match(patron, t))


################ VALIDAR CÓDIGO POSTAL ########################

# Código postal válido: 5 números

def validar_cp(cp):
    patron = r"^[0-9]{5}$"
    return bool(re.match(patron, cp))


# Ejemplos de uso:
print(validar_dni("12345678Z"))       # True
print(validar_matricula("1234 ABC"))  # True
print(validar_telefono("612345678"))  # True
print(validar_cp("28080"))            # True


###############################################################
#                  BUCLES FOR EN PYTHON
###############################################################

# El bucle for sirve para recorrer iterables: listas, tuplas,
# diccionarios, cadenas de texto, rangos, etc.

############# FOR con listas #############
frutas = ["manzana", "pera", "uva"]

for f in frutas:
    print(f)  # Recorre cada elemento


############# FOR con diccionarios ########
persona = {"nombre": "Luis", "edad": 20}

# Recorrer claves:
for clave in persona:
    print(clave, "→", persona[clave])

# Recorrer claves y valores con items():
for clave, valor in persona.items():
    print(clave, valor)


############# FOR con range() #############
# range(inicio, fin, paso)

for i in range(1, 6):
    print(i)  # Imprime 1,2,3,4,5

# Con paso:
for i in range(0, 10, 2):
    print(i)  # 0,2,4,6,8


############# FOR en cadenas ################
for letra in "Python":
    print(letra)


###############################################################
#                     EJEMPLO FINAL
###############################################################

# Pedimos un DNI y verificamos si es válido

dni = input("Introduce tu DNI: ")

if validar_dni(dni):
    print("DNI correcto ✔️")
else:
    print("DNI incorrecto ❌")
