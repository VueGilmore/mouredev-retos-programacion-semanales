'''
Reto #9: CÓDIGO MORSE

Dificultad: MEDIA

Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
  la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
  o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
  https://es.wikipedia.org/wiki/Código_morse.

  
A	· —	 	    N	— ·	 	    0	— — — — —
B	— · · ·	 	Ñ	— — · — —	1	· — — — —
C	— · — ·	 	O	— — —	 	2	· · — — —
CH	— — — —	 	P	· — — ·	 	3	· · · — —
D	— · ·	 	Q	— — · —	 	4	· · · · —
E	·	 	    R	· — ·	 	5	· · · · ·
F	· · — ·	 	S	· · ·	 	6	— · · · ·
G	— — ·	 	T	—	 	    7	— — · · ·
H	· · · ·	 	U	· · —	 	8	— — — · ·
I	· ·	 	    V	· · · —	 	9	— — — — ·
J	· — — —	 	W	· — —	 	.	· — · — · —
K	— · —	 	X	— · · —	 	,	— — · · — —
L	· — · ·	 	Y	— · — —	 	?	· · — — · ·
M	— —	 	    Z	— — · ·	 	"	· — · · — ·  
'''

dictionary = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'ch': '----',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'ñ': '--.--',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '"': '.-..-.',
}




def is_morse_code(text):
    if text.count('.') + text.count('-') + text.count(' ') == len(text):
        return True
    else:
        return False
    

def remove_accents(texto):
    for i in texto:
        if i == 'á':
            texto = texto.replace(i, 'a')
        elif i == 'é':
            texto = texto.replace(i, 'e')
        elif i =='í':
            texto = texto.replace(i, 'i')
        elif i =='ó':
            texto = texto.replace(i, 'o')
        elif i =='ú':
            texto = texto.replace(i, 'u')
    return texto

def convert_to_natural(texto):
    in_natural = ''

    for i in texto.split():
        letter_found = list(dictionary.keys())[list(dictionary.values()).index(i)]
        if letter_found:
            in_natural = in_natural + letter_found
        else:
            in_natural = in_natural + ' '

    return in_natural
    

def convert_to_morse(texto):
    in_morse = ''

    for i in texto:
        if not i == ' ':
            in_morse = in_morse + dictionary[i.lower()] + ' '
        else:
            in_morse = in_morse + ' '

    return in_morse


def convert_text(texto):
    if is_morse_code(texto):
        return convert_to_natural(texto)
    else:
        texto = remove_accents(texto)
        return convert_to_morse(texto)


print( convert_text( 'Hola' ) )
print( convert_text( 'Hola, ahora esto es código morse' ) )
print( convert_text( '.... --- .-.. .-' ) )
print( convert_text( '.... --- .-.. .- --..--  .- .... --- .-. .-  . ... - ---  -. ---  . ...  -.-. --- -.. .. --. ---  -- --- .-. ... . ' ) )




# ChatGPT
# Diccionario con las correspondencias entre caracteres y código morse
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    """
    Función para codificar un mensaje en código morse
    """
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Agrega el código morse del caracter y un espacio
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            # Agrega dos espacios para separar palabras
            cipher += ' '

    return cipher

def decrypt(message):
    """
    Función para decodificar un mensaje en código morse
    """
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

def convert(message):
    """
    Función para detectar automáticamente si el texto de entrada es en texto natural o en código morse, y realizar la conversión correspondiente
    """
    if all(c in MORSE_CODE_DICT.values() for c in message.split()):
        # El texto de entrada es en código morse
        return decrypt(message)
    else:
        # El texto de entrada es en texto natural
        return encrypt(message)


#print( convert( 'Hola' ) )
#print( convert( '.... --- .-.. .-' ) )