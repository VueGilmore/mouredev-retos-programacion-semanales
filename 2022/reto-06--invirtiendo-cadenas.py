'''
Reto #6: INVIRTIENDO CADENAS

Dificultad: FÁCIL

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def invertir_cadena(cadena):
  cadena_nueva = ''
  cadena_len = len(cadena)
  cadena_tope = - cadena_len

  i = -1
  while i >= cadena_tope :
    cadena_nueva = ''.join([cadena_nueva, cadena[i]])
    i = i - 1
  print(cadena_nueva)

invertir_cadena('Hola mundo Python')

# Solución por ChatGTP
def reverse_string(s):
    # Convert the input string into a list of characters
    s = list(s)
    # Initialize two pointers, one at the start and one at the end
    i = 0
    j = len(s) - 1
    # While the two pointers have not met in the middle
    while i < j:
        # Swap the characters at the two pointers
        s[i], s[j] = s[j], s[i]
        # Increment the left pointer and decrement the right pointer
        i += 1
        j -= 1
    # Join the characters again to get a string as output
    return ''.join(s)

print(reverse_string("Hola mundo")) # Output: "odnum aloH"
