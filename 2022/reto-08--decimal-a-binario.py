'''
Reto #8: DECIMAL A BINARIO

Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def convertir_a_binario(numero):
    record = list()

    while numero >= 1:
        record.append(numero % 2)
        numero = numero // 2

    record.reverse()
    
    for i in record:
        print(i, end='')
    print('')


convertir_a_binario(5)  # 101
convertir_a_binario(28) # 11100
convertir_a_binario(79) # 1001111