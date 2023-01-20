'''
Reto #11: ELIMINANDO CARACTERES

Dificultad: FÁCIL

Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
  estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
  estén presentes en str1.
'''

def eliminando_caracteres(str1, str2):
    out1 = '' # str1 menos str2
    out2 = '' # str1 menos str1

    for i in str1:
        if not i.lower() in str2.lower():
            out1 = out1 + i

    for i in str2:
        if not i.lower() in str1.lower():
            out2 = out2 + i

    return (out1, out2)

print(eliminando_caracteres('Esta es la cadena numero 1', 'Esta es la cadena numero 2'))
print(eliminando_caracteres( 'VueGilmore', 'Hola que tal' ))

print(eliminando_caracteres("brais","moure"))
print(eliminando_caracteres("Me gusta Java","Me gusta Python"))