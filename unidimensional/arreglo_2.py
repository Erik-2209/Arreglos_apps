def rellenar_arreglo_personas(tamaño):
    arreglo = []
    for i in range(tamaño):
        nombre = input(f"Introduce el nombre de la persona {i + 1}: ")
        edad = int(input(f"Introduce la edad de la persona {i + 1}: "))
        arreglo.append({"nombre": nombre, "edad": edad})  # Diccionario como objeto
    return arreglo

def mostrar_arreglo(arreglo):
    print("El arreglo contiene los siguientes datos sobre las personas:")
    for obj in arreglo:
        print(f"Nombre: {obj['nombre']}, Edad: {obj['edad']}")

# Ejemplo de uso
tamaño = int(input("Introduce el tamaño del arreglo de personas: "))
arreglo = rellenar_arreglo_personas(tamaño)
mostrar_arreglo(arreglo)
