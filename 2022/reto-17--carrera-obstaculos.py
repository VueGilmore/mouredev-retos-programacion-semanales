'''
Reto #17: LA CARRERA DE OBSTÁCULOS

Dificultad: MEDIA 

Crea una función que evalúe si un/a atleta ha superado correctamente una
carrera de obstáculos.
- La función recibirá dos parámetros:
     - Un array que sólo puede contener String con las palabras
       "run" o "jump"
     - Un String que represente la pista y sólo puede contener "_" (suelo)
       o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
     - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
       será correcto y no variará el símbolo de esa parte de la pista.
     - Si hace "jump" en "_" (suelo), se variará la pista por "x".
     - Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
'''

def es_carrera_correcta(acciones, pista):
  es_correcta = True

  for i in range(0, len(pista)):
    if pista[i] == '_':
      if not acciones[i] == 'run':
        pista[i] = 'x'
        es_correcta = False
    if pista[i] == '|':
      if not acciones[i] == 'jump':
        pista[i] = '/'
        es_correcta = False

  return es_correcta


# Pruebas
print(es_carrera_correcta(
  ['run', 'run', 'jump', 'run', 'run', 'jump', 'run', 'jump', 'run', 'run'],
  ['_', '_', '|', '_', '_', '|', '_', '|', '_', '_']
))

print(es_carrera_correcta(
  ['run', 'run', 'jump', 'run', 'run', 'jump', 'run', 'jump', 'run', 'run'],
  ['_', '|', '_', '_', '|', '_', '_', '|', '_', '_']
))