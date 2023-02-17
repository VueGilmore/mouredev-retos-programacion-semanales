'''
Reto #24: ITERATION MASTER

Dificultad: FÁCIL   

Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.
'''

# For loop
def count_to_100_1():
    for i in range(0, 100):
        print(i + 1)


# While loop
def count_to_100_2():
    i = 1
    cont = True

    while cont:
        print(i)

        if i >= 100:
            cont = False
        i += 1


# Recursive
def count_to_100_3(start = 1):
    print(start)
    if start < 100:
        count_to_100_3( start + 1 )



# Pruebas
count_to_100_1() # For loop
count_to_100_2() # While loop
count_to_100_3() # Recursive
