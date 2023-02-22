'''
Reto #25: PIEDRA, PAPEL, TIJERA

Dificultad: MEDIA   

Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel)
  o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''

def ganador(ronda):
    order = ['R', 'P', 'S', 'R']

    index1 = order.index(ronda[0])

    if ronda[0] == ronda[1]:
        return 'Tie'
    elif ronda[1] == order[index1 + 1]:
        return 'player2'
    else:
        return 'player1'



def quien_gana(rondas):
    won_player_1 = 0
    won_player_2 = 0

    for i in rondas:
        if ganador(i) == 'player1':
            won_player_1 += 1
        elif ganador(i) == 'player2':
            won_player_2 += 1

    if won_player_1 > won_player_2:
        return 'Player 1'
    elif won_player_1 < won_player_2:
        return 'Player 2'
    elif won_player_1 == won_player_2:
        return 'Tie'
    else:
        return 'Invalid'



# Pruebas
print(quien_gana([("S","P"), ("R","R"), ("S","P")])) # Player 1 
print(quien_gana([("P","R"), ("R","S"), ("S","P")])) # Player 1
print(quien_gana([("R","S"), ("S","R"), ("P","S")])) # Player 2
print(quien_gana([("S","R"), ("S","R"), ("P","S")])) # Player 2
print(quien_gana([("R","R"), ("R","S"), ("P","S")])) # Tie
