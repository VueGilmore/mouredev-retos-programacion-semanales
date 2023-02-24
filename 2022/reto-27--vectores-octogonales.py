'''
Reto #27: VECTORES ORTOGONALES

Dificultad: FÁCIL   

Crea un programa que determine si dos vectores son ortogonales.
- Los dos array deben tener la misma longitud.
- Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''

def es_octogonal(vectores):
    if not len(vectores[0]) == len(vectores[1]):
        return False
    else: 
        results = []
        
        for i in range(0, len(vectores)):
            results.append(0)
            
            # Calcula el producto
            for j in range(0, len(vectores[i])):
                if results[i] == 0:
                    results[i] = vectores[i][j]
                else:
                    results[i] = results[i] * vectores[i][j]

        # Si la diferencia es 0 es ortogonal
        total = 0
        for i in results:
            total += i

        if total == 0:
            return True
        else:
            return False
            

print(es_octogonal([[2, 1], [-1, 2]]))        # True
print(es_octogonal([[2, 3], [3, -2]]))        # True
print(es_octogonal([[1, -2], [1, -2]]))       # False
print(es_octogonal([[2, 4, 5], [-2, 3, 7] ])) # False



# ChatGPT
""" def son_ortogonales(v1, v2):
    if len(v1) != len(v2):
        return False
    else:
        # Calculamos el producto punto de los vectores
        prod_punto = sum([v1[i]*v2[i] for i in range(len(v1))])
        if prod_punto == 0:
            return True
        else:
            return False

# Ejemplo de uso
v1 = [1, -2]
v2 = [2, 1]
if son_ortogonales(v1, v2):
    print("Los vectores son ortogonales")
else:
    print("Los vectores no son ortogonales") """
