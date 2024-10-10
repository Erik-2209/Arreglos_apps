import random

# Ingresar el tamaño de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Inicializar la matriz con valores aleatorios entre 1 y 100
matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]

# Mostrar la matriz generada
print("\nMatriz generada:")
for fila in matriz:
    print(fila)

# Encontrar el mayor valor en la matriz
mayor = matriz[0][0]
for fila in matriz:
    for valor in fila:
        if valor > mayor:
            mayor = valor

print(f"\nEl valor más grande en la matriz es: {mayor}")
