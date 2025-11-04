#!/usr/bin/env python3
"""
Ejercicios del Tema 1 al 5 - Resueltos y comentados
Archivo: Ejercicios_Temas_1_5_completos.py
Contenido:
 - Todos los enunciados (como comentarios) y soluciones del PDF "EJERCICIOS DEL TEMA 1 AL 5".
 - Menús interactivos para navegar por secciones y ejecutar cada ejercicio desde la consola.

Modo de uso:
 - Ejecuta: python3 Ejercicios_Temas_1_5_completos.py
 - Sigue los menús para escoger sección y ejercicio.

Nota: las funciones de lectura validan entradas para evitar fallos en el examen.
"""

# -----------------------------
# UTILIDADES COMUNES
# -----------------------------

def leer_entero(prompt: str, minimo=None, maximo=None, permitir_fin=False):
    """Lee un entero validando. Si permitir_fin=True, devuelve None al introducir 'fin'."""
    while True:
        s = input(prompt).strip()
        if permitir_fin and s.lower() == 'fin':
            return None
        try:
            n = int(s)
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")
            continue
        if minimo is not None and n < minimo:
            print(f"Introduce un número >= {minimo}.")
            continue
        if maximo is not None and n > maximo:
            print(f"Introduce un número <= {maximo}.")
            continue
        return n


def leer_float(prompt: str, permitir_fin=False):
    while True:
        s = input(prompt).strip()
        if permitir_fin and s.lower() == 'fin':
            return None
        try:
            return float(s)
        except ValueError:
            print("Entrada no válida. Introduce un número." )


def pausa():
    input("\nPulsa ENTER para continuar...")

# -----------------------------
# SECCION: CONCEPTOS BÁSICOS
# -----------------------------

# Ejercicio CB1
# Enunciado: Escriba un programa que recoja un valor por teclado y muestre de qué tipo es.
def cb1_tipo_valor():
    v = input('Introduce un valor: ')
    # intentamos convertir a int, float; si no, queda como string
    tipo = 'str'
    try:
        int(v)
        tipo = 'int'
    except ValueError:
        try:
            float(v)
            tipo = 'float'
        except ValueError:
            tipo = 'str'
    print(f"Has introducido '{v}' y su tipo detectado es: {tipo}")

# Ejercicio CB2
# Enunciado: Escribe un programa que recoja dos números enteros... suma, resta, multiplicación, división real, división entera, resto y potencia.
def cb2_operaciones_basicas():
    a = leer_entero('Introduce primer entero: ')
    b = leer_entero('Introduce segundo entero: ')
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División real: {a / b if b != 0 else 'Error: división por cero'}")
    print(f"División entera: {a // b if b != 0 else 'Error: división por cero'}")
    print(f"Resto: {a % b if b != 0 else 'Error: división por cero'}")
    print(f"Potencia a**b: {a ** b}")

# Ejercicio CB3
# Enunciado: Pide el nombre y saluda.
def cb3_saludo():
    nombre = input('Introduce tu nombre: ').strip()
    print(f"¡Hola, {nombre}!")

# Ejercicio CB4
# Enunciado: Recoja tres números y calcule su media aritmética.
def cb4_media():
    nums = []
    for i in range(3):
        n = leer_float(f'Introduce número {i+1}: ')
        nums.append(n)
    media = sum(nums) / 3
    print(f"La media es {media}")

# Ejercicio CB5
# Enunciado: Recoja un número y muestre su valor absoluto.
def cb5_valor_absoluto():
    n = leer_float('Introduce un número: ')
    print(f"Valor absoluto: {abs(n)}")

# Ejercicio CB6
# Enunciado: Recoja las notas de las tres evaluaciones... con pesos 20%,35%,45%.
def cb6_nota_final():
    n1 = leer_float('Nota 1 (0-10): ')
    n2 = leer_float('Nota 2 (0-10): ')
    n3 = leer_float('Nota 3 (0-10): ')
    final = n1 * 0.2 + n2 * 0.35 + n3 * 0.45
    print(f"Nota final: {final:.2f}")

# Ejercicio CB7
# Enunciado: Recoja un número y muestre su representación en código binario.
def cb7_binario():
    n = leer_entero('Introduce un entero: ')
    print(f"Binario: {bin(n)[2:]}")

# Ejercicio CB8
# Enunciado: Recoja un texto y lo muestre cinco veces consecutivas en la misma línea.
def cb8_repetir_linea():
    s = input('Introduce texto: ')
    print((s + ' ') * 5)

# Ejercicio CB9
# Enunciado: Recoja un texto y que muestre su longitud.
def cb9_longitud():
    s = input('Introduce texto: ')
    print(f"Longitud: {len(s)}")

# Ejercicio CB10
# Enunciado: Recoja la edad del usuario y muestre la edad que tendrá dentro de 5, 10 y 15 años.
def cb10_edad_futuro():
    edad = leer_entero('Introduce tu edad: ', minimo=0)
    print(f"En 5 años tendrás {edad + 5} años")
    print(f"En 10 años tendrás {edad + 10} años")
    print(f"En 15 años tendrás {edad + 15} años")

# -----------------------------
# SECCION: SENTENCIAS DE SELECCIÓN
# -----------------------------

# Selección 1: Par o impar
# Enunciado: Recoja un número e indique si se trata de un número par o impar.
def s1_par_impar():
    n = leer_entero('Introduce un entero: ')
    print('Par' if n % 2 == 0 else 'Impar')

# Selección 2: Día de la semana
# Enunciado: Recoja un número y muestre el día de la semana (1=Lunes...)
def s2_dia_semana():
    dias = {1:'Lunes',2:'Martes',3:'Miércoles',4:'Jueves',5:'Viernes',6:'Sábado',7:'Domingo'}
    n = leer_entero('Introduce número (1-7): ')
    print(dias.get(n,'Día de la semana incorrecto'))

# Selección 3: Mayor y menor de tres
# Enunciado: Lea tres números y muestre los mayor y menor.
def s3_mayor_menor():
    nums = [leer_float(f'Número {i+1}: ') for i in range(3)]
    print(f"Mayor: {max(nums)}; Menor: {min(nums)}")

# Selección 4: División con comprobación de divisor
# Enunciado: Recoja dividendo y divisor, y realice su división si divisor != 0.
def s4_division():
    a = leer_float('Dividendo: ')
    b = leer_float('Divisor: ')
    if b == 0:
        print('Error: divisor 0')
    else:
        print(f"Resultado: {a / b}")

# Selección 5: Precio de entrada según edad
# Enunciado: Calcular precio según edad y jubilación.
def s5_precio_museo():
    edad = leer_entero('Edad: ', minimo=0)
    jubilado = input('¿Es jubilado? (s/n): ').strip().lower() == 's'
    if edad < 5 or jubilado or edad >= 65:
        precio = 0.0
    elif 5 <= edad < 18:
        precio = 3.0
    else:
        precio = 6.0
    print(f"Precio entrada: {precio} €")

# Selección 6: Calificación literal
# Enunciado: Mostrar nota final como texto según intervalos.
def s6_nota_literal():
    n = leer_float('Introduce nota (0-10): ')
    if n < 0 or n > 10:
        print('Error: nota fuera de rango')
    elif n < 5:
        print('Suspenso')
    elif n < 6:
        print('Suficiente')
    elif n < 7:
        print('Bien')
    elif n < 9:
        print('Notable')
    elif n < 10:
        print('Sobresaliente')
    else:
        print('Matrícula de honor')

# Selección 7: Saludo según hora
# Enunciado: Recoja la hora y devuelva saludo según intervalos.
def s7_saludo_hora():
    h = leer_entero('Introduce hora (0-23): ', minimo=0, maximo=23)
    if 7 <= h < 12:
        print('Buenos días')
    elif 12 <= h < 20:
        print('Buenas tardes')
    else:
        print('Buenas noches')

# Selección 8: Días del mes
# Enunciado: Recoja mes en número y devuelva número de días del mes.
def s8_dias_mes():
    m = leer_entero('Introduce mes (1-12): ', minimo=1, maximo=12)
    if m in (1,3,5,7,8,10,12):
        dias = 31
    elif m == 2:
        dias = 28
    else:
        dias = 30
    print(f"El mes {m} tiene {dias} días (sin contar bisiestos)")

# Selección 9: Año bisiesto
# Enunciado: Indique si un año es bisiesto.
def s9_bisiesto():
    a = leer_entero('Introduce año: ')
    es = (a % 4 == 0) and (a % 100 != 0 or a % 400 == 0)
    print('Es bisiesto' if es else 'No es bisiesto')

# Selección 10: Donante de sangre (validación completa simplificada)
# Enunciado: A partir de varios parámetros indicar si puede donar.
def s10_puede_donar():
    ayunas = input('¿Va en ayunas? (s/n): ').strip().lower() == 's'
    if ayunas:
        print('No puede donar en ayunas')
        return
    edad = leer_entero('Edad: ')
    if not (18 <= edad <= 65):
        print('Edad fuera de rango')
        return
    peso = leer_float('Peso (kg): ')
    if peso <= 50:
        print('Peso insuficiente')
        return
    td = leer_entero('Tensión diastólica (mm Hg): ')
    ts = leer_entero('Tensión sistólica (mm Hg): ')
    if not (50 <= td <= 100 and 90 <= ts <= 180):
        print('Tensión fuera de rango')
        return
    pulso = leer_entero('Pulso (ppm): ')
    if not (50 <= pulso <= 110):
        print('Pulso fuera de rango')
        return
    sexo = input('Sexo (hombre/mujer): ').strip().lower()
    hb = leer_float('Hemoglobina (g/L): ')
    if (sexo.startswith('h') and hb <= 13.5) or (sexo.startswith('m') and hb <= 12.5):
        print('Hemoglobina insuficiente')
        return
    plaquetas = leer_entero('Plaquetas (x1000): ')
    if plaquetas <= 150:
        print('Plaquetas insuficientes')
        return
    proteinas = leer_float('Proteínas totales (g/dl): ')
    if proteinas <= 6:
        print('Proteínas insuficientes')
        return
    print('Puede donar')

# -----------------------------
# SECCION: SENTENCIAS DE REPETICIÓN
# -----------------------------

# Repetición 1: Cada letra en línea distinta
# Enunciado: Recoja un texto y escriba cada letra en una línea distinta.
def r1_letras_linea():
    s = input('Introduce texto: ')
    for ch in s:
        print(ch)

# Repetición 2: Factorial
# Enunciado: Recoja un número y calcule su factorial.
def r2_factorial():
    n = leer_entero('Introduce entero >= 0: ', minimo=0)
    res = 1
    for i in range(2, n+1):
        res *= i
    print(f"{n}! = {res}")

# Repetición 3: Leer números hasta 0 y mostrar estadísticos
# Enunciado: Leer números hasta que se introduzca 0. Mostrar número de valores, min, max, suma y media.
def r3_estadisticas_hasta_cero():
    nums = []
    while True:
        n = leer_entero('Introduce entero (0 para terminar): ')
        if n == 0:
            break
        nums.append(n)
    if not nums:
        print('No se introdujeron valores')
    else:
        print(f"Cantidad: {len(nums)}; Min: {min(nums)}; Max: {max(nums)}; Suma: {sum(nums)}; Media: {sum(nums)/len(nums):.2f}")

# Repetición 4: Triángulo de asteriscos
# Enunciado: Mostrar triángulo con base igual al número.
def r4_triangulo():
    n = leer_entero('Introduce altura (entero positivo): ', minimo=1)
    for i in range(1, n+1):
        print('*' * i)

# Repetición 5: Primeros cuadrados hasta n
# Enunciado: Mostrar los primeros cuadrados hasta el número introducido.
def r5_cuadrados():
    n = leer_entero('Introduce entero >=1: ', minimo=1)
    print(' '.join(str(i*i) for i in range(1, n+1)))

# Repetición 6: Tabla filas x columnas
# Enunciado: Recoja filas y columnas y muestre tabla numerada.
def r6_tabla_nc():
    filas = leer_entero('Filas: ', minimo=1)
    cols = leer_entero('Columnas: ', minimo=1)
    num = 1
    for r in range(filas):
        row = []
        for c in range(cols):
            row.append(str(num))
            num += 1
        print(' '.join(row))

# Repetición 7: Contar ocurrencias de letra
# Enunciado: Recoja cadena y letra, contar cuántas veces aparece.
def r7_contar_letra():
    s = input('Introduce texto: ')
    letra = input('Introduce letra a buscar: ')
    if len(letra) != 1:
        print('Introduce una sola letra')
        return
    print(f"La letra '{letra}' aparece {s.count(letra)} veces")

# Repetición 8: Es primo
# Enunciado: Recoja un número y calcule si es primo.
def r8_es_primo():
    n = leer_entero('Introduce entero >=2: ', minimo=2)
    if n <= 3:
        print('Primo' if n in (2,3) else 'No primo')
        return
    if n % 2 == 0:
        print('No primo')
        return
    i = 3
    import math
    limite = int(math.sqrt(n))
    while i <= limite:
        if n % i == 0:
            print('No primo')
            return
        i += 2
    print('Primo')

# Repetición 9: Número impar y pirámide
# Enunciado: Recoja número impar (volver a pedir si es par) y mostrar pirámide de asteriscos con base igual al número.
def r9_piramide_impar():
    while True:
        n = leer_entero('Introduce número impar: ')
        if n % 2 == 1:
            break
        print('No es impar, vuelve a intentarlo')
    # pirámide centrada
    altura = (n // 2) + 1
    for i in range(altura):
        estrellas = 1 + 2*i
        print('*' * estrellas)

# Repetición 10: Triángulo de impares decrecientes
# Enunciado: Recoja un número y muestre triángulo con secuencias decrecientes de números impares.
def r10_triangulo_impares():
    n = leer_entero('Introduce n (número de líneas): ', minimo=1)
    for i in range(1, n+1):
        linea = ' '.join(str(2*j-1) for j in range(i, 0, -1))
        print(linea)

# -----------------------------
# SECCION: FUNCIONES (MENÚ DEL EXAMEN)
# -----------------------------
# Items indicados en el PDF: rombo, adivinar número, ecuación 2º grado, tabla de números aleatorios,
# factorial (recursivo), fibonacci, tabla de multiplicar y salir.

import random
import math

# Función: mostrar rombo
# Enunciado: Pedir un número impar y mostrar rombo de asteriscos.
def f_rombo():
    while True:
        n = leer_entero('Introduce número impar para el rombo: ', minimo=1)
        if n % 2 == 1:
            break
        print('Debe ser impar')
    mitad = n // 2
    for i in range(mitad + 1):
        espacios = ' ' * (mitad - i)
        estrellas = '*' * (1 + 2*i)
        print(espacios + estrellas)
    for i in range(mitad-1, -1, -1):
        espacios = ' ' * (mitad - i)
        estrellas = '*' * (1 + 2*i)
        print(espacios + estrellas)

# Función: adivinar un número (1-100)
def f_adivina():
    secreto = random.randint(1, 100)
    intento = None
    while intento != secreto:
        intento = leer_entero('Adivina el número (1-100): ', minimo=1, maximo=100)
        if intento < secreto:
            print('Es mayor')
        elif intento > secreto:
            print('Es menor')
        else:
            print('¡Acertaste!')

# Función: resolver ecuación de segundo grado
# Enunciado: Leer coeficientes a,b,c y encontrar soluciones (puede no tener reales).
def f_resolver_cuadratica():
    a = leer_float('a: ')
    b = leer_float('b: ')
    c = leer_float('c: ')
    if a == 0:
        if b == 0:
            print('No es ecuación')
        else:
            print(f"Solución lineal: {-c/b}")
        return
    disc = b*b - 4*a*c
    if disc < 0:
        print('No tiene soluciones reales')
    elif disc == 0:
        x = -b / (2*a)
        print(f"Una única solución: {x}")
    else:
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        print(f"Soluciones: {x1} y {x2}")

# Función: tabla de números aleatorios
# Enunciado: Pedir filas y columnas y mostrar tabla con números aleatorios.
def f_tabla_numeros_aleatorios():
    filas = leer_entero('Filas: ', minimo=1)
    cols = leer_entero('Columnas: ', minimo=1)
    for r in range(filas):
        row = [str(random.randint(0, 99)) for _ in range(cols)]
        print('\t'.join(row))

# Función: factorial recursivo
# Enunciado: Calcular factorial (solución recursiva sugerida)
def f_factorial_rec(n: int) -> int:
    return 1 if n <= 1 else n * f_factorial_rec(n-1)

def f_factorial_menu():
    n = leer_entero('Introduce entero >=0: ', minimo=0)
    print(f"{n}! = {f_factorial_rec(n)}")

# Función: fibonacci (iterativa para evitar recursión costosa)
def f_fibonacci_menu():
    pos = leer_entero('Introduce posición (>=1): ', minimo=1)
    a, b = 1, 1
    if pos <= 2:
        print(1)
        return
    for _ in range(3, pos+1):
        a, b = b, a + b
    print(b)

# Función: tabla de multiplicar
def f_tabla_multiplicar():
    n = leer_entero('Introduce número: ')
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Menú principal del bloque FUNCIONES (tal como en el enunciado del PDF)
def menu_funciones():
    opciones = {
        'a': ('Mostrar un rombo', f_rombo),
        'b': ('Adivinar un número', f_adivina),
        'c': ('Resolver una ecuación de segundo grado', f_resolver_cuadratica),
        'd': ('Tabla de números', f_tabla_numeros_aleatorios),
        'e': ('Cálculo del número factorial de un número', f_factorial_menu),
        'f': ('Cálculo de un número de la sucesión de Fibonacci', f_fibonacci_menu),
        'g': ('Tabla de multiplicar', f_tabla_multiplicar),
        'h': ('Salir', None)
    }
    while True:
        print('\nMENÚ DE OPCIONES')
        for k, (desc, _) in opciones.items():
            print(f"{k}) {desc}")
        opcion = input('Elige opción: ').strip().lower()
        if opcion not in opciones:
            print('Opción incorrecta')
            continue
        if opcion == 'h':
            break
        func = opciones[opcion][1]
        func()
        pausa()

# -----------------------------
# BLOQUE: RELACIÓN DE EJERCICIOS (NUMEROS, CADENAS, CONDICIONALES, BUCLES Y FUNCIONES)
# Implementación de los 19 ejercicios listados en ese bloque.
# -----------------------------

# Ejercicio 1 — Par o impar con validación
# ... (implementación siguiendo las indicaciones del PDF)

def ex1_es_par(n: int) -> bool:
    return n % 2 == 0

def ex1_main():
    print("Introduce números y escribe si son par o impar. Escribe 'fin' para terminar.")
    while True:
        s = input('Número o fin: ').strip().lower()
        if s == 'fin':
            break
        try:
            n = int(s)
        except ValueError:
            print('Entrada no válida')
            continue
        print('Par' if ex1_es_par(n) else 'Impar')

# Ejercicio 2 — Calculadora básica con funciones

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError('División por cero')
    return a / b

def ex2_calculadora():
    print("Calculadora. Escribe 'salir' como operación para terminar.")
    while True:
        op = input('Operación (+ - * /) o salir: ').strip().lower()
        if op == 'salir':
            break
        if op not in ['+','-','*','/']:
            print('Operación no válida')
            continue
        try:
            a = float(input('a: '))
            b = float(input('b: '))
        except ValueError:
            print('Entrada numérica inválida')
            continue
        try:
            res = {'+': sumar, '-': restar, '*': multiplicar, '/': dividir}[op](a, b)
            print(f'Resultado: {res}')
        except ZeroDivisionError:
            print('Error: división por cero')

# Ejercicio 3 — Contador de vocales

def contar_vocales(cadena: str) -> dict:
    conteo = {v:0 for v in 'aeiou'}
    for ch in cadena.lower():
        if ch in conteo:
            conteo[ch] += 1
    return conteo

def ex3_main():
    s = input('Introduce una frase: ')
    c = contar_vocales(s)
    # ordenar por frecuencia descendente
    orden = sorted(c.items(), key=lambda x: x[1], reverse=True)
    for v, n in orden:
        print(f"{v}: {n}")

# Ejercicio 4 — Máximo hasta 'fin'

def leer_enteros_hasta_fin() -> list:
    res = []
    while True:
        s = input("Introduce entero o 'fin': ").strip().lower()
        if s == 'fin':
            break
        try:
            res.append(int(s))
        except ValueError:
            print('No es entero')
    return res

def calcular_extremos(numeros):
    if not numeros:
        return None
    return (min(numeros), max(numeros))

def ex4_main():
    nums = leer_enteros_hasta_fin()
    if not nums:
        print('No hay datos')
    else:
        minimo, maximo = calcular_extremos(nums)
        print(f"Mínimo: {minimo}; Máximo: {maximo}")

# Ejercicio 5 — Números primos hasta N

def ex5_es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    i = 3
    while i <= r:
        if n % i == 0:
            return False
        i += 2
    return True

def ex5_main():
    N = leer_entero('Introduce N (>1): ', minimo=2)
    primos = [str(i) for i in range(2, N+1) if ex5_es_primo(i)]
    print(' '.join(primos))

# Ejercicio 6 — Conversor de temperaturas

def c_a_f(c):
    return c * 9/5 + 32

def f_a_c(f):
    return (f - 32) * 5/9

def ex6_main():
    print("Conversor: escribe 'fin' para terminar")
    while True:
        sentido = input("¿c->f o f->c? (c/f): ").strip().lower()
        if sentido == 'fin':
            break
        if sentido not in ('c','f'):
            print('Opción no válida')
            continue
        try:
            val = float(input('Valor: '))
        except ValueError:
            print('Valor no válido')
            continue
        if sentido == 'c':
            print(f"{c_a_f(val):.2f} F")
        else:
            print(f"{f_a_c(val):.2f} C")

# Ejercicio 7 — Figuras con asteriscos (triángulo, escalera, rectángulo)

def dibujar_triangulo(h):
    for i in range(1, h+1): print('*' * i)

def dibujar_escalera(h):
    for i in range(1, h+1): print('*' * i)

def dibujar_rectangulo(w, h):
    for _ in range(h): print('*' * w)

def ex7_main():
    print('1 triángulo, 2 escalera, 3 rectángulo')
    op = leer_entero('Opción: ', minimo=1, maximo=3)
    if op in (1,2):
        h = leer_entero('Altura: ', minimo=1)
        if op == 1: dibujar_triangulo(h)
        else: dibujar_escalera(h)
    else:
        w = leer_entero('Ancho: ', minimo=1)
        h = leer_entero('Altura: ', minimo=1)
        dibujar_rectangulo(w,h)

# Ejercicio 8 — Tablas de multiplicar desde a hasta b

def imprimir_tablas(a, b):
    for n in range(a, b+1):
        print(f"Tabla del {n}:")
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
        print()

def ex8_main():
    a = leer_entero('a: ')
    b = leer_entero('b (>=a): ')
    if b < a:
        print('b debe ser >= a')
        return
    imprimir_tablas(a, b)

# Ejercicio 9 — Validación de contraseña

def es_contrasena_valida(s: str) -> bool:
    if len(s) < 8 or ' ' in s:
        return False
    has_upper = has_lower = has_digit = has_symbol = False
    for ch in s:
        if ch.isupper(): has_upper = True
        elif ch.islower(): has_lower = True
        elif ch.isdigit(): has_digit = True
        elif ch in '!@#$%^&*?': has_symbol = True
    return has_upper and has_lower and has_digit and has_symbol

def ex9_main():
    while True:
        s = input('Introduce contraseña: ')
        if es_contrasena_valida(s):
            print('Contraseña válida')
            break
        else:
            print('No válida, inténtalo de nuevo')

# Ejercicio 10 — Normaliza nombres

def normaliza_nombre(s: str) -> str:
    partes = [p for p in s.strip().split(' ') if p]
    partes = [p[0].upper() + p[1:].lower() if len(p)>0 else '' for p in partes]
    return ' '.join(partes)

def ex10_main():
    s = input('Introduce nombre: ')
    print(normaliza_nombre(s))

# Ejercicio 11 — Contar dígitos pares e impares

def contar_pares_impares(n: int):
    n = abs(n)
    pares = impares = 0
    if n == 0:
        pares = 1
    while n > 0:
        d = n % 10
        if d % 2 == 0: pares += 1
        else: impares += 1
        n //= 10
    return pares, impares

def ex11_main():
    n = leer_entero('Introduce entero: ')
    pares, imp = contar_pares_impares(n)
    print(f"Pares: {pares}; Impares: {imp}")

# Ejercicio 12 — Repetir palabra con guiones

def repetir_palabra(palabra: str, n: int) -> str:
    if n <= 0:
        return ''
    return '-'.join([palabra]*n)

def ex12_main():
    p = input('Palabra: ')
    n = leer_entero('Veces: ', minimo=0)
    print(repetir_palabra(p, n))

# Ejercicio 13 — Contar vocales y consonantes (sin listas)

def contar_vocales_consonantes(s: str):
    vocales = 'aeiouAEIOU'
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vocales: v += 1
            else: c += 1
    return v, c

def ex13_main():
    s = input('Introduce texto: ')
    v, c = contar_vocales_consonantes(s)
    print(f"Vocales: {v}; Consonantes: {c}")

# Ejercicio 14 — Conversión segundos a h:m:s

def convertir_tiempo(segundos: int) -> str:
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return f"{h}:{m:02d}:{s:02d}"

def ex14_main():
    s = leer_entero('Segundos: ', minimo=0)
    print(convertir_tiempo(s))

# Ejercicio 15 — Calculadora de potencias con menú

def calcular_potencia(base, exp):
    return base ** exp

def ex15_main():
    while True:
        print('a) Cuadrado b) Cubo c) Potencia n d) Salir')
        op = input('Opción: ').strip().lower()
        if op == 'd': break
        if op not in ('a','b','c'):
            print('Opción no válida')
            continue
        base = float(input('Base: '))
        if op == 'a': print(calcular_potencia(base, 2))
        elif op == 'b': print(calcular_potencia(base, 3))
        else:
            exp = int(input('Exponente: '))
            print(calcular_potencia(base, exp))

# Ejercicio 16 — Inversión de cadena (sin slicing)

def invertir_cadena(s: str) -> str:
    res = ''
    for ch in s:
        res = ch + res
    return res

def ex16_main():
    s = input('Cadena: ')
    print(invertir_cadena(s))

# Ejercicio 17 — Contador de caracteres específicos

def contar_caracter(s: str, c: str) -> int:
    cnt = 0
    for ch in s:
        if ch == c: cnt += 1
    return cnt

def ex17_main():
    s = input('Cadena: ')
    c = input('Carácter: ')
    print(contar_caracter(s, c))

# Ejercicio 18 — Número capicúa

def es_capicua(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def ex18_main():
    n = leer_entero('Número: ')
    print('Capicúa' if es_capicua(n) else 'No capicúa')

# Ejercicio 19 — Convertidor mayúsculas/minúsculas/capitalizar

def ex19_main():
    s = input('Frase: ')
    print('a) Mayúsculas b) Minúsculas c) Capitalizar')
    op = input('Opción: ').strip().lower()
    if op == 'a': print(s.upper())
    elif op == 'b': print(s.lower())
    elif op == 'c': print(s.capitalize())
    else: print('Opción no válida')

# -----------------------------
# SECCION: SECUENCIAS (ejercicios finales)
# -----------------------------

# Secuencia 1: Leer números hasta 0 y mostrar en 3 modos
def seq1():
    nums = []
    while True:
        n = leer_entero('Número (0 para terminar): ')
        if n == 0: break
        nums.append(n)
    print('Orden introducido:', ' '.join(map(str, nums)))
    print('Orden creciente:', ' '.join(map(str, sorted(nums))))
    print('Orden decreciente:', ' '.join(map(str, sorted(nums, reverse=True))))

# Secuencia 2: Repetir pero con textos hasta cadena vacía
def seq2():
    textos = []
    while True:
        s = input('Texto (vacío para terminar): ')
        if s == '': break
        textos.append(s)
    print('Orden introducido:', textos)
    print('Orden creciente:', sorted(textos))
    print('Orden decreciente:', sorted(textos, reverse=True))

# Secuencia 3: Palíndromo
def palindromo(s):
    t = ''.join(ch.lower() for ch in s if ch.isalnum())
    return t == t[::-1]

def seq3():
    s = input('Texto: ')
    print('Es palíndromo' if palindromo(s) else 'No es palíndromo')

# Secuencia 4: Comprobar si un texto es palíndromo de otro
def seq4():
    a = input('Texto A: ')
    b = input('Texto B: ')
    ign = input('Ignorar mayúsculas/minúsculas? (s/n): ').strip().lower() == 's'
    if ign:
        a2 = ''.join(ch.lower() for ch in a if ch.isalnum())
        b2 = ''.join(ch.lower() for ch in b if ch.isalnum())
    else:
        a2 = ''.join(ch for ch in a if ch.isalnum())
        b2 = ''.join(ch for ch in b if ch.isalnum())
    print('Sí' if a2 == b2[::-1] else 'No')

# -----------------------------
# MENÚ GENERAL PARA NAVEGAR TODO EL ARCHIVO
# -----------------------------

SECCIONES = {
    '1': ('Conceptos básicos', [
        ('CB1 Tipo valor', cb1_tipo_valor),
        ('CB2 Operaciones básicas', cb2_operaciones_basicas),
        ('CB3 Saludo', cb3_saludo),
        ('CB4 Media de 3', cb4_media),
        ('CB5 Valor absoluto', cb5_valor_absoluto),
        ('CB6 Nota final ponderada', cb6_nota_final),
        ('CB7 Binario', cb7_binario),
        ('CB8 Repetir texto 5 veces', cb8_repetir_linea),
        ('CB9 Longitud texto', cb9_longitud),
        ('CB10 Edad futura', cb10_edad_futuro),
    ]),
    '2': ('Sentencias de selección', [
        ('S1 Par o impar', s1_par_impar),
        ('S2 Día de la semana', s2_dia_semana),
        ('S3 Mayor y menor', s3_mayor_menor),
        ('S4 División con comprobación', s4_division),
        ('S5 Precio museo', s5_precio_museo),
        ('S6 Nota literal', s6_nota_literal),
        ('S7 Saludo por hora', s7_saludo_hora),
        ('S8 Días del mes', s8_dias_mes),
        ('S9 Año bisiesto', s9_bisiesto),
        ('S10 Donación de sangre', s10_puede_donar),
    ]),
    '3': ('Sentencias de repetición', [
        ('R1 Letras en líneas', r1_letras_linea),
        ('R2 Factorial', r2_factorial),
        ('R3 Estadísticas hasta 0', r3_estadisticas_hasta_cero),
        ('R4 Triángulo', r4_triangulo),
        ('R5 Cuadrados', r5_cuadrados),
        ('R6 Tabla filas x cols', r6_tabla_nc),
        ('R7 Contar letra', r7_contar_letra),
        ('R8 Es primo', r8_es_primo),
        ('R9 Pirámide impar', r9_piramide_impar),
        ('R10 Triángulo impares', r10_triangulo_impares),
    ]),
    '4': ('Funciones (menú examen)', [
        ('Funciones - menú interactivo (rombo, adivina, etc.)', menu_funciones),
    ]),
    '5': ('Relación de ejercicios (varios)', [
        ('Ex1 Par o impar con validación', ex1_main),
        ('Ex2 Calculadora básica', ex2_calculadora),
        ('Ex3 Contador de vocales', ex3_main),
        ('Ex4 Máximo hasta fin', ex4_main),
        ('Ex5 Primos hasta N', ex5_main),
        ('Ex6 Conversor temperaturas', ex6_main),
        ('Ex7 Figuras asteriscos', ex7_main),
        ('Ex8 Tablas multiplicar a..b', ex8_main),
        ('Ex9 Validación contraseña', ex9_main),
        ('Ex10 Normaliza nombre', ex10_main),
        ('Ex11 Contar pares/impares dígitos', ex11_main),
        ('Ex12 Repetir palabra', ex12_main),
        ('Ex13 Vocales/Consonantes', ex13_main),
        ('Ex14 Segundos a h:m:s', ex14_main),
        ('Ex15 Calculadora de potencias', ex15_main),
        ('Ex16 Invertir cadena', ex16_main),
        ('Ex17 Contar carácter', ex17_main),
        ('Ex18 Capicúa', ex18_main),
        ('Ex19 Convertir mayus/minus/cap', ex19_main),
    ]),
    '6': ('Secuencias finales', [
        ('Seq1 Números modos', seq1),
        ('Seq2 Textos modos', seq2),
        ('Seq3 Palíndromo', seq3),
        ('Seq4 Palíndromo comparado', seq4),
    ])
}


def menu_general():
    while True:
        print('\n--- MENÚ GENERAL - EJERCICIOS TEMA 1 AL 5 ---')
        for k, (titulo, _) in SECCIONES.items():
            print(f"{k}) {titulo}")
        print('0) Salir')
        sec = input('Elige sección: ').strip()
        if sec == '0':
            print('Fin. ¡Suerte en el examen!')
            break
        if sec not in SECCIONES:
            print('Sección no válida')
            continue
        titulo, lista = SECCIONES[sec]
        print(f"\n-- {titulo} --")
        for i, (nom, _) in enumerate(lista, start=1):
            print(f"{i}) {nom}")
        print('0) Volver')
        while True:
            sel = input('Selecciona ejercicio: ').strip()
            if sel == '0':
                break
            try:
                idx = int(sel)
                if not (1 <= idx <= len(lista)):
                    print('Índice fuera de rango')
                    continue
            except ValueError:
                print('Entrada no válida')
                continue
            func = lista[idx-1][1]
            func()
            pausa()
            break

# Ejecutar menú_general si el archivo se ejecuta directamente
if __name__ == '__main__':
    menu_general()

# ==========================================================
# EXPLICACIÓN DEL TRY - EXCEPT EN PYTHON (equivalente a TRY - CATCH en Java)
# ==========================================================
#
# En Python, el manejo de errores se realiza con las palabras clave:
#   try      -> código que puede fallar
#   except   -> bloque que se ejecuta si ocurre un error
#   else     -> (opcional) se ejecuta si NO ocurre ningún error
#   finally  -> (opcional) se ejecuta SIEMPRE, ocurra o no error
#
# ----------------------------------------------------------
# EJEMPLO 1: ESTRUCTURA BÁSICA
# ----------------------------------------------------------

try:
    # Aquí colocamos el código que puede generar un error
    numero = int(input("Introduce un número entero: "))

    # Si todo va bien, se ejecutan las líneas siguientes
    print("Número introducido correctamente:", numero)

except ValueError:
    # Este bloque se ejecuta si ocurre un error de tipo ValueError
    # (por ejemplo, si el usuario escribe letras en lugar de números)
    print("Error: No has introducido un número válido")

# ----------------------------------------------------------
# EJEMPLO 2: AÑADIR BLOQUES ELSE Y FINALLY
# ----------------------------------------------------------
#
# - El bloque else se ejecuta solo si NO ocurre ningún error.
# - El bloque finally se ejecuta SIEMPRE, pase lo que pase.

try:
    a = int(input("Introduce el numerador: "))
    b = int(input("Introduce el denominador: "))
    resultado = a / b  # Esto puede lanzar ZeroDivisionError

except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

except ValueError:
    print("Error: Debes introducir números válidos")

else:
    print("Resultado correcto:", resultado)

finally:
    print("Este mensaje aparece SIEMPRE, haya error o no")

# ----------------------------------------------------------
# EJEMPLO 3: CAPTURAR VARIOS TIPOS DE EXCEPCIONES A LA VEZ
# ----------------------------------------------------------

try:
    texto = input("Introduce algo: ")
    numero = int(texto)
    print("Has introducido el número", numero)

except (ValueError, TypeError):
    # Captura ambos tipos de error en el mismo bloque
    print("Error: Valor o tipo incorrecto")

# ----------------------------------------------------------
# EJEMPLO 4: CAPTURAR CUALQUIER ERROR (GENERAL)
# ----------------------------------------------------------

try:
    x = 10 / 0  # Esto genera ZeroDivisionError
except Exception as e:
    # Captura cualquier excepción que herede de Exception
    print("Ha ocurrido un error:", e)

# ----------------------------------------------------------
# EJEMPLO 5: LANZAR EXCEPCIONES MANUALMENTE
# ----------------------------------------------------------

def dividir(a, b):
    # Podemos lanzar una excepción usando 'raise'
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero (lanzado manualmente)")
    return a / b

try:
    print(dividir(5, 0))
except ZeroDivisionError as e:
    print("Error capturado:", e)

# ----------------------------------------------------------
# DIFERENCIAS RESPECTO A JAVA (RESUMEN RÁPIDO)
# ----------------------------------------------------------
#
# - En Java se usa try { ... } catch(Exception e) { ... }
# - En Python se usa try: ... except Exception as e: ...
# - Python no obliga a declarar excepciones en la firma del método (no hay checked exceptions)
# - No existe finally{} sino finally:
# - Para lanzar excepciones se usa 'raise', no 'throw new'
#
# EJEMPLO COMPARATIVO:
#
#  Java ->   try { int x = Integer.parseInt("abc"); }
#             catch (NumberFormatException e) { System.out.println("Error"); }
#
#  Python -> try:
#                x = int("abc")
#            except ValueError:
#                print("Error")
#
# ==========================================================
# FIN DE LA EXPLICACIÓN
# ==========================================================
