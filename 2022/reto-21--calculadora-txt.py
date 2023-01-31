'''
Reto #21: CALCULADORA .TXT

Dificultad: MEDIA  

Lee el fichero "reto-21--calculadora-txt.txt" incluido en el proyecto, calcula su
resultado e imprímelo.
- El .txt se corresponde con las entradas de una calculadora.
- Cada línea tendrá un número o una operación representada por un
  símbolo (alternando ambos).
- Soporta números enteros y decimales.
- Soporta las operaciones suma "+", resta "-", multiplicación "*"
  y división "/".
- El resultado se muestra al finalizar la lectura de la última
  línea (si el .txt es correcto).
- Si el formato del .txt no es correcto, se indicará que no se han
  podido resolver las operaciones.
'''

with open('./2022/reto-21--calculadora-txt.txt', 'r') as file:
  content = file.read().replace('\n', '')
  
  operation_ok = True
  operations_allowed = ('+', '-', '*', '/')
  num1 = 0
  num2 = 0
  operation = ''

  for index in range(0, len(content)):
    # Asignar
    if content[index] in operations_allowed:
      operation = content[index]
    elif num1 == 0:
      num1 = int(content[index])
    else:
      num2 = int(str(num2) + content[index])

    if not num2 == 0 and ( (index + 1 < len(content) and content[index + 1] in operations_allowed ) or (index + 1 >= len(content))):
      # Calcular 
      if operation == '+':
        num1 = num1 + num2
      elif operation == '-':
        num1 = num1 - num2
      elif operation == '*':
        num1 = num1 * num2
      elif operation == '/':
        num1 = num1 / num2
      else:
        operation_ok = False
      # Reset
      operation = ''
      num2 = 0

  if operation_ok:
    print(num1) # 18,5
  else:
    print('No se han podido resolver las operaciones')

      

