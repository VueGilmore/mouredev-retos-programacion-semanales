'''
Reto #1: EL "LENGUAJE HACKER"

Dificultad: FÁCIL

Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
  con el alfabeto y los números en "leet".
  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

def codificar(texto):
  leet_code = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
              "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
              "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
              "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
  texto_codificado = ''

  for letra in texto:
    if letra.upper() in leet_code.keys():
      texto_codificado = texto_codificado + leet_code[letra.upper()]
    else:
      texto_codificado = texto_codificado + letra

  print(texto_codificado)
  

codificar('hola, este mensaje esta codificado')
codificar("Leet")
codificar("Aquí está un texto de prueba para ver si funciona el reto!")
