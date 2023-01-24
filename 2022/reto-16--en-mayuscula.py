'''
Reto #16: EN MAYÚSCULA

Dificultad: FÁCIL 

Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
'''

def capitalize(cadena):
  nueva_cadena = ''
  next_upper = True

  for i in cadena:
    if next_upper and i not in ('¡', '!', '¿', '?', ',', ';', '.', ':', '[', ']', '{', '}', '(', ')', '&', '%', '/', '$'):
        nueva_cadena = nueva_cadena + i.upper()
        next_upper = False
    else:
       nueva_cadena = nueva_cadena + i
    if i == ' ':
        next_upper = True
        
  return nueva_cadena

print(capitalize('hola esta es una frase para probar si la función funciona bien'))
print(capitalize('esta también ¡funciona?'))