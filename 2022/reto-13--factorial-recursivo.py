'''
Reto #13: FACTORIAL RECURSIVO

Dificultad: FÁCIL

Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
'''

def factorial(numero):
  if numero == 0:
    return 1
  else:
    return numero * factorial(numero - 1)

    
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(5))
print(factorial(7))
print(factorial(10))
