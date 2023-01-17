'''
Reto #7: CONTANDO PALABRAS

Dificultad: MEDIA

Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
  lo resuelvan automáticamente.
'''

def limpiar_cadena(cadena):
  palabras = cadena.split()

  for i in palabras:
    palabras[palabras.index(i)] = limpiar_palabra(i)

  return palabras


def limpiar_palabra(palabra):
  for i in [',',';', '.', ':' , '¡', '!', '¿', '?']:
    if i in palabra:
      palabra = palabra.replace(i, '')

  return palabra.lower()


def cuenta_palabras(cadena):
  nueva_cadena = limpiar_cadena(cadena)
  recuento = dict()

  for i in nueva_cadena:
    if not i in recuento:
      recuento[i] = nueva_cadena.count(i)

  return recuento

contar1 = cuenta_palabras('Hola mundo; Python. hola mundo!, mundo, ¡hello hello!, ¿Cómo estás?')
for i in contar1:
   print(f'{i}: {contar1[i]}')

print('---------------------')

contar2 = cuenta_palabras('Hola, hola, Python es un lenguaje de programación, programación, python')
for i in contar2:
   print(f'{i}: {contar2[i]}')


# ChatGPT
def count_words(text):
    # Crea un diccionario vacío para almacenar el recuento de palabras
    word_count = {}
    # Crea una variable temporal para construir las palabras a medida que se recorre la cadena de texto
    word = ""
    # Recorre cada carácter en la cadena de texto
    for char in text:
        # Verifica si el carácter es alfanumérico o un espacio
        if char.isalnum() or char.isspace():
            # Si el carácter es alfanumérico, agrégalo a la variable temporal
            if char.isalnum():
                word += char.lower()
            # Si el carácter es un espacio o el final de la cadena
            else:
                # Si la variable temporal no está vacía
                if word:
                    # Verifica si la palabra ya está en el diccionario
                    if word in word_count:
                        # Si está, aumenta el contador en 1
                        word_count[word] += 1
                    else:
                        # Si no, agrega la palabra al diccionario con un contador de 1
                        word_count[word] = 1
                    # Vacía la variable temporal
                    word = ""
    # Si queda alguna palabra en la variable temporal después de recorrer toda la cadena de texto
    if word:
        # Verifica si la palabra ya está en el diccionario
        if word in word_count:
            # Si está, aumenta el contador en 1
            word_count[word] += 1
        else:
            # Si no, agrega la palabra al diccionario con un contador de 1
            word_count[word] = 1
    # Recorre cada palabra en el diccionario
    for key in word_count:
        # Imprime la palabra y su contador
        print(key + ": " + str(word_count[key]))

#count_words('Hola mundo; Python. hola mundo!, mundo, ¡hello hello!, ¿Cómo estás?')
#count_words('Hola, hola, Python es un lenguaje de programación, programación, python')