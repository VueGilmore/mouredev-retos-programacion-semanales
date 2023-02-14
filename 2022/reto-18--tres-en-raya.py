'''
Reto #18: TRES EN RAYA

Dificultad: DIFÍCIL  

Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
  O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
'''

'''
Checks if the "player" wins
@matrix: matriz
@player: X o O
'''
def check_win(matrix, player):
  winner = False

  # Horizontal
  for i in matrix:
    if i.count(player) == 3:
      winner = True
  
  # Vertical
  if not winner:
    for index1 in range(0, len(matrix)):
      counter = 0
      for index2 in range(0, len(matrix[index1])):
        if matrix[index2][index1] == player:
          counter = counter + 1
      if counter == 3:
        winner = True

  # Diagonal
  if not winner:
    if matrix[0][0] == player and matrix[1][1] == player and matrix[2][2] == player:
      winner = True
    elif matrix[0][2] == player and matrix[1][1] == player and matrix[2][0] == player:
      winner = True

  return winner

'''
Para ser posible tiene que:
- Tener un mínimo de 3 Xs o Os
- Tener el mismo número de Xs y Os o por diferencia de uno (si el primero en jugar gana)
- No pueden ganar los dos
'''
def check_possible_matrix(matrix):
  numberOfXs = 0
  numberOfOs = 0

  for i in range(0, len(matrix)):
    numberOfXs = numberOfXs + matrix[i].count('X')
    numberOfOs = numberOfOs + matrix[i].count('O')

  if numberOfXs < 3 and numberOfOs < 3:
    #print('Movimientos insuficientes. La partida aún no ha terminado.')
    return False
  elif not numberOfXs == numberOfOs and abs(numberOfXs - numberOfOs) > 1:
    #print('Número de Xs o Os no válido')
    #print(f'X: {numberOfXs}')
    #print(f'O: {numberOfOs}')
    return False
  elif check_win(matrix, 'X') and check_win(matrix, 'O'):
    #print('Ambos ganaron...')
    return False
  else:
    return True


def get_result_game(matrix):
  if check_possible_matrix(matrix):
    if check_win(matrix, 'X'):
      print('Gana X')
    elif check_win(matrix, 'O'):
      print('Gana O')
    else:
      print('No gana nadie. Empate.')
  else:
    print('Matriz no válida.')
    return None



# Pruebas
get_result_game((('X', 'X', 'X'), ('', 'O', ''), ('O', 'O', '')))    # Gana X
get_result_game((('X', '', ''), ('X', 'O', ''), ('X', 'O', 'O')))    # Gana X
get_result_game((('X', '', 'O'), ('O', 'X', ''), ('O', '', 'X')))    # Gana X
get_result_game((('', 'O', 'X'), ('', 'X', 'O'), ('X', 'O', '')))    # Gana X

get_result_game((('', 'X', 'O'), ('X', 'X', 'O'), ('X', 'O', 'O')))  # Gana O
get_result_game((('O', 'X', ''), ('X', 'O', ''), ('X', '', 'O')))    # Gana O
get_result_game((('O', '', ''), ('X', 'O', ''), ('X', 'X', 'O')))    # Gana O
get_result_game((('O', '', 'X'), ('X', 'O', 'X'), ('', '', 'O')))    # Gana O

get_result_game((('X', 'O', 'X'), ('X', 'O', 'O'), ('O', 'X', 'X'))) # Empate
get_result_game((('X', 'X', 'O'), ('O', 'X', 'X'), ('X', 'O', 'O'))) # Empate
get_result_game((('O', 'X', 'O'), ('X', 'O', 'X'), ('X', 'O', 'X'))) # Empate
get_result_game((('O', 'X', 'O'), ('O', 'X', 'X'), ('X', 'O', 'X'))) # Empate

get_result_game((('O', 'X', 'X'), ('X', 'X', 'X'), ('X', 'O', 'X'))) # No valido - Mas Xs que Os
get_result_game((('O', 'O', 'X'), ('O', 'O', 'O'), ('X', 'O', 'X'))) # No valido - Mas Os que Xs
get_result_game((('X', 'X', 'X'), ('O', 'O', 'O'), ('', '', '')))    # No valido - Ambos ganan
get_result_game((('X', '', 'X'), ('', '', 'O'), ('', 'O', '')))      # No valido - No suficiente