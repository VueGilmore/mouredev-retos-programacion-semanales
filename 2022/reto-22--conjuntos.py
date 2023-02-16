'''
Reto #22: CONJUNTOS

Dificultad: FÁCIL  

Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes
  de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes
  de los dos array.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
'''

def conjuntos(conjunto1, conjunto2, booleano):
    conjuntoRetorno = []

    if booleano:
        for i in conjunto1:
            if i in conjunto2:
                conjuntoRetorno.append(i)
    else:
        for i in conjunto1:
            if i not in conjunto2:
                conjuntoRetorno.append(i)

    return conjuntoRetorno


# Pruebas
print(conjuntos([1, 3, 5, 8], [12, 34, 6, 2, 4, 5, 3], True))
print(conjuntos([1, 3, 5, 8], [1, 6, 2, 4, 5, 3], True))
print(conjuntos([1, 3, 5, 8], [1, 6, 2, 4, 5, 3], False))
print(conjuntos(['a', 'b', 'c', 'd', 'e'], ['a', 'e'], True))
print(conjuntos(['a', 'b', 'c', 'd', 'e'], ['a', 'e'],False))
