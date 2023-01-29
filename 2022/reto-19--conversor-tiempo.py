'''
Reto #19: CONVERSOR TIEMPO

Dificultad: FÁCIL 

Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
'''

def convertir_tiempo(dias, horas, minutos, segundos):
  return (dias * 86400000) + (horas * 3600000) + (minutos * 60000) + (segundos * 1000)


print(convertir_tiempo(2, 2, 2, 2))