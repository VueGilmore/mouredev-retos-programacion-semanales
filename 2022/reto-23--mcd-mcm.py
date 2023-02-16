'''
Reto #23: MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO

Dificultad: MEDIA  

Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
que calcule el mínimo común múltiplo (mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que 
  lo resuelvan directamente.
'''

def calcular_maximo_comun_divisor(numero1, numero2):
    min_num = min(numero1, numero2)
    mcd = 1

    while min_num > 1:
        if numero1 % min_num == 0 and numero2 % min_num == 0:
            mcd = min_num
        min_num -= 1
    return mcd


def calcular_minimo_comun_multiplo(numero1, numero2):
    max_num = max(numero1, numero2)

    while True:
        if max_num % numero1 == 0 and max_num % numero2 == 0:
            return max_num
        max_num += 1


# Pruebas
print(f'MCD(2, 4):   {calcular_maximo_comun_divisor(2, 4)}')
print(f'MCD(3, 8):   {calcular_maximo_comun_divisor(3, 8)}')
print(f'MCD(12, 34): {calcular_maximo_comun_divisor(12, 34)}')
print(f'MCD(3, 33):  {calcular_maximo_comun_divisor(3, 33)}')

print(f'MCM(2, 4)   {calcular_minimo_comun_multiplo(2, 4)}')
print(f'MCM(3, 7)   {calcular_minimo_comun_multiplo(3, 7)}')
print(f'MCM(23, 46) {calcular_minimo_comun_multiplo(23, 46)}')
print(f'MCM(54, 98) {calcular_minimo_comun_multiplo(54, 98)}')
