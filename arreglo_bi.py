# Arreglo bidimensional para almacenar la cantidad de 3 productos en 4 sucursales
inventario = [
    [10, 20, 15, 30],  # Producto 1 en 4 sucursales
    [5, 15, 10, 25],   # Producto 2 en 4 sucursales
    [8, 12, 20, 18]    # Producto 3 en 4 sucursales
]

# Calcular la cantidad total de cada producto
for i in range(len(inventario)):
    cantidad_total = sum(inventario[i])
    print(f"La cantidad total del producto {i + 1} es: {cantidad_total}")