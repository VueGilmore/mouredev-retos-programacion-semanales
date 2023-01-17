'''
Reto #10: EXPRESIONES EQUILIBRADAS

Dificultad: MEDIA

Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran
  en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios.
  No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
'''
def es_equilibrada(expresion):
    expresion = expresion.replace(' ', '')
    delimitadores_abrir = ('[', '(', '{')
    delimitadores_cerrar = (']', ')', '}')
    temp = list()

    for c in expresion:
        if c in delimitadores_abrir:
            temp.append(c)
        elif c in delimitadores_cerrar:
            if c == ']' and temp[-1] == '[':
                temp.pop()
            elif c == ')' and temp[-1] == '(':
                temp.pop()
            elif c == '}' and temp[-1] == '{':
                temp.pop()
            else:
                temp.append(c)

    if len(temp) == 0:
        return True
    else:
        return False

print(es_equilibrada('{ [ a * ( c + d ) ] - 5 }')) # True
print(es_equilibrada('{ a * ( c + d ) ] - 5 }'))   # False
print(es_equilibrada('{ [ a * ( c + d ] ) - 5 }')) # False