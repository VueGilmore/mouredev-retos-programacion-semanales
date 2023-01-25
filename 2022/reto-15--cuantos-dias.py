'''
Reto #15: ¿CUÁNTOS DÍAS?

Dificultad: DIFÍCIL 

Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
  lanzará una excepción.
'''
import datetime

def calcular_dias(cadena1, cadena2):
  diferencia = 0

  try:
    fecha1 = datetime.datetime.strptime(cadena1, "%d/%m/%Y").date()
    fecha2 = datetime.datetime.strptime(cadena2, "%d/%m/%Y").date()

    diferencia = fecha2 - fecha1
    diferencia = diferencia.days
  except:
    return 'Las fechas proporcionadas no están en el formato correcto.'
  
  return abs(diferencia)


# Pruebas
print(calcular_dias('01/01/2023', '05/01/2023'))
print(calcular_dias('01/01/2023', '05/01/2022'))
print(calcular_dias('21/11/2023', '21/11/2024'))
## Pruebas con Errores
print(calcular_dias('01/01/2023', '05/01/202'))
print(calcular_dias('0101/2023', '05/01/2024'))
print(calcular_dias('2023/00/00', '05/01/2024'))