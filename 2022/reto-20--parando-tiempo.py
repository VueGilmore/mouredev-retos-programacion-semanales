'''
Reto #20: PARANDO EL TIEMPO

Dificultad: MEDIA  

Crea una función que sume 2 números y retorne su resultado pasados
unos segundos.
- Recibirá por parámetros los 2 números a sumar y los segundos que
  debe tardar en finalizar su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma
  asíncrona, es decir, sin detener la ejecución del programa principal.
  Se podría ejecutar varias veces al mismo tiempo.
'''
from threading import Timer

def mostrar_suma(num1, num2):
  print( num1 + num2 )

def parando_tiempo(num1, num2, timer):
  timing = Timer(timer, mostrar_suma, (num1, num2))
  timing.start()

parando_tiempo(7, 3, 5)
parando_tiempo(7, 5, 5)
