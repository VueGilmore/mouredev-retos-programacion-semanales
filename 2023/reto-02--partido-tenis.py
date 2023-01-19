'''
Reto #2: EL PARTIDO DE TENIS

Dificultad: MEDIA

Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Ventaja P1
  Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
'''

def procesar_juego(marcas):
    basic_game = ['Love', 15, 30, 40, 'Win']
    p1_game = 'Love'
    p2_game = 'Love'
    advantage_game = ''      # options: empty, P1 or P2
    game_status = 'regular'  # options: deuce, advantage, done

    for i in marcas:
      # Regular game
      if game_status == 'regular':
        if i == 'P1':
          p1_game = p1_game = basic_game[basic_game.index(p1_game) + 1]
        elif i == 'P2':
          p2_game = p2_game = basic_game[basic_game.index(p2_game) + 1]
        
        # Check if deuce
        if p1_game == 40 and p2_game == 40:
          game_status = 'deuce'
          print('Deuce')
        # check if done
        elif p1_game == 'Win' or p2_game == 'Win':
          game_status = 'done'
          
          if p1_game == 'Win':
            print('Ha ganado el P1')
          elif p2_game == 'Win':
            print('Ha ganado el P2')
        else:
          print( p1_game, ' - ', p2_game )
      # Deuce
      elif game_status == 'deuce':
        game_status = 'advantage'

        if i == 'P1':
          advantage_game = 'P1'
          print('Ventaja P1')
        elif i == 'P2':
          advantage_game = 'P2'
          print('Ventaja P2')
      # Advantage
      elif game_status == 'advantage':
        if i == 'P1' and advantage_game == 'P1':
          advantage_game = ''
          game_status = 'done'
          print('Ha ganado el P1')
        elif i == 'P1' and advantage_game == 'P2':
          advantage_game = ''
          game_status = 'deuce'
          print('Deuce')
        elif i == 'P2' and advantage_game == 'P2':
          advantage_game = ''
          game_status = 'done'
          print('Ha ganado el P2')  
        elif i == 'P2' and advantage_game == 'P1':
          advantage_game = ''
          game_status = 'deuce'
          print('Deuce')
    
    if not game_status == 'done':
      print('El juego no terminó')


procesar_juego(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])              # Ha ganado el P1
procesar_juego(['P1', 'P1', 'P2', 'P2', 'P2', 'P2'])                          # Ha ganado el P2
procesar_juego(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P2', 'P1'])  # Ha ganado el P1 (y sobran dos)
procesar_juego(['P1', 'P1', 'P1', 'P1', 'P1', 'P1'])                          # Ha ganado el P1 (y sobra uno)
procesar_juego(['P1', 'P1'])                                                  # 30 - Love (faltan datos)