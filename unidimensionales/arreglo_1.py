# Función para rellenar el arreglo con múltiplos
def rellenar_arreglo(tamaño, multiplo):
    arreglo = []  # Creamos un arreglo vacío
    for i in range(1, tamaño + 1):
        arreglo.append(i * multiplo)  # Añadimos los múltiplos
    return arreglo

# Función para mostrar el contenido del arreglo
def mostrar_arreglo(arreglo):
    print("El arreglo contiene los siguientes múltiplos:")
    for numero in arreglo:
        print(numero)

# Función principal para gestionar la entrada del usuario y llamar a las otras funciones
def main():
    # Pedimos el tamaño del arreglo y el número múltiplo al usuario
    tamaño = int(input("Introduce el tamaño del arreglo: "))
    multiplo = int(input("Introduce el número para los múltiplos: "))
    
    # Llamamos a la función que rellena el arreglo
    arreglo = rellenar_arreglo(tamaño, multiplo)
    
    # Llamamos a la función que muestra el arreglo
    mostrar_arreglo(arreglo)

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
