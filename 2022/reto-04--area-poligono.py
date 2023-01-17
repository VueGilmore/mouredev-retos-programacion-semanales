'''
Reto #4: ÁREA DE UN POLÍGONO

Dificultad: FÁCIL

Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
'''

def area_poligono(tipo: str, lados: list):
  if tipo == 'triangulo':
    area = lados[0] * lados[1] / 2
  elif tipo == 'cuadrado':
    area = lados[0] * lados[0]
  elif tipo == 'rectangulo':
    area = lados[0] * lados[1]
  else:
      area = 0
  return area

print(area_poligono('triangulo', [3, 4]))
print(area_poligono('cuadrado', [5]))
print(area_poligono('rectangulo', [3, 5]))