'''
Reto #3: ¿ES UN NÚMERO PRIMO?

Dificultad: MEDIA

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

def es_numero_primo(numero):
    if numero < 2:
       return False

    for i in range(2, numero):
      if numero % i == 0:
        return False
    
    return True
       
          

def lista_numeros_primos(cantidad):
    for i in range(1, cantidad + 1):
      if es_numero_primo(i):
         print(i)

lista_numeros_primos(100)