'''
Reto #14: ¿ES UN NÚMERO DE ARMSTRONG?

Dificultad: FÁCIL

Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información 
al respecto.
'''
import math

def es_numero_armstrong(numero):
  numero_lista = list(str(numero))

  resultado = 0
  for i in numero_lista:
    resultado = resultado + math.pow(int(i), 3)

  if int(resultado) == numero:
    return True
  else:
    return False


print(es_numero_armstrong(0))
print(es_numero_armstrong(1))
print(es_numero_armstrong(153))
print(es_numero_armstrong(370))
print(es_numero_armstrong(371))
print(es_numero_armstrong(407))
print(es_numero_armstrong(188))
print(es_numero_armstrong(576))
