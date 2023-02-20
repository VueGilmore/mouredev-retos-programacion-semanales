'''
Reto #26: CUADRADO Y TRIÁNGULO 2D

Dificultad: FÁCIL   

Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
- Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
- EXTRA: ¿Eres capaz de dibujar más figuras?
'''

def dibujar_figurea(lado, figura):

    if figura == 'cuadrado':
        for i in range(0, lado):
            for j in range(0, lado):
                print('* ', end='')
            print()
        print()
    elif figura == 'triangulo':
        for i in range(0, lado):
            espacios = lado - i - 1
            asteriscos = 2*i + 1
            print(" " * espacios + "*" * asteriscos)



# Pruebas
dibujar_figurea(5, 'cuadrado')
dibujar_figurea(2, 'cuadrado')
dibujar_figurea(5, 'triangulo')
dibujar_figurea(8, 'triangulo')
