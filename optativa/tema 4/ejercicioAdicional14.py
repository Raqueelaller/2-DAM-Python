'''Ejercicio 14 — Conversión de segundos a formato h:m:s
Crea una función convertir_tiempo(segundos: int) -> str que convierta una cantidad de
segundos
en formato horas:minutos:segundos.
Ejemplo: 3665 → '1:01:05'.
Pista: usa división entera // y módulo %.'''

def convertir_tiempo(segundos: int) -> str:
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_rest = segundos % 60
    return f"{horas}:{minutos:02}:{segundos_rest:02}"

tiempo = int(input("dime los segundos"))

print(convertir_tiempo(tiempo))