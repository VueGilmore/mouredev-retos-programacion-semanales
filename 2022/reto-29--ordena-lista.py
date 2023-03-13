'''
Reto #29: ORDENA LA LISTA

Dificultad: FÁCIL   

Crea una función que ordene y retorne una matriz de números.
- La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
  adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
  o de mayor a menor.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan
  automáticamente.
'''

def ordenar_matriz(matrix, order):
  i = 1
  while i < len(matrix):
    if ( matrix[i] < matrix[i-1] and order == 'Asc' ) or ( matrix[i] > matrix[i-1] and order == 'Desc' ) :
      temp = matrix[i-1]

      matrix[i-1] = matrix[i]
      matrix[i] = temp
      i = 1
    else:
      i += 1

  return matrix


# Pruebas
print( ordenar_matriz( [4, 2, 8, 6, 9], 'Asc' ) )           # [2, 4, 6, 8, 9]
print( ordenar_matriz( [99, 4, 11, 2, 7, 32, 1], 'Asc' ) )  # [1, 2, 4, 7, 11, 32, 99]
print( ordenar_matriz( [2, 4, 6, 8, 9], 'Desc' ) )          # [9, 8, 6, 4, 2]
print( ordenar_matriz( [12, 4, 3, 2, 9], 'Desc' ) )         # [12, 9, 4, 3, 2]



# ChatGPT
def ordenar_matriz_chatgpt(lista, orden):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if orden == "Asc":
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            elif orden == "Desc":
                if lista[j] < lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                return "Orden inválida. Debe ser 'Asc' o 'Desc'."
    return lista

lista = [2, 4, 6, 8, 9]
orden = "Asc"

lista_ordenada = ordenar_matriz_chatgpt(lista, orden)

print(lista_ordenada)  # Resultado esperado: [2, 4, 6, 8, 9]
