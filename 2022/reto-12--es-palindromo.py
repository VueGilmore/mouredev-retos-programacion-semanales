'''
Reto #12: ¿ES UN PALÍNDROMO?

Dificultad: MEDIA

Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
'''

def es_palindromo(cadena):
  not_wanted = ['á', 'é', 'í', 'ó', 'ú', '?', '¿', '¡', '!', ' ', ',', '.', ';', ':' ] # These characters are not allowed
  cadena = cadena.replace(' ', '').lower() # no empty spaces, all lowercase

  for i in not_wanted:
    cadena = cadena.replace(i, '')

  i, j = 0, len(cadena) - 1
  es_palindromo = True

  while i <= j / 2 and es_palindromo:
      if cadena[i] != cadena[j]:
        es_palindromo = False
      i = i + 1
      j = j - 1
      
  return es_palindromo

print(es_palindromo('ana'))
print(es_palindromo('roma'))
print(es_palindromo('Ana lleva al oso la avellana'))