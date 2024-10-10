# Definir dos matrices 2x2
matriz_a = [
    [1, 2],
    [3, 4]
]

matriz_b = [
    [5, 6],
    [7, 8]
]

# Inicializar la matriz de resultado con ceros
resultado = [
    [0, 0],
    [0, 0]
]

# Sumar las dos matrices
for i in range(2):
    for j in range(2):
        resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

# Mostrar la matriz resultante
print("Suma de las matrices:")
for fila in resultado:
    print(fila)
