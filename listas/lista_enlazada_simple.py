# Clase Nodo: Representa cada nodo de la lista enlazada
class Nodo:
    def __init__(self, dato):
        """Constructor del nodo."""
        self.dato = dato  # Almacena el valor del nodo
        self.siguiente = None  # Referencia al siguiente nodo, inicializada en None

# Clase ListaEnlazadaSimple: Representa la lista enlazada simple
class ListaEnlazadaSimple:
    def __init__(self):
        """Constructor de la lista enlazada simple."""
        self.cabeza = None  # La cabeza de la lista inicialmente es None (lista vacía)

    # Método para insertar al inicio de la lista
    def insertar_inicio(self, dato):
        """Inserta un nuevo nodo al inicio de la lista."""
        nuevo_nodo = Nodo(dato)  # Crear un nuevo nodo con el dato proporcionado
        nuevo_nodo.siguiente = self.cabeza  # El siguiente del nuevo nodo apunta a la antigua cabeza
        self.cabeza = nuevo_nodo  # Actualizamos la cabeza para que apunte al nuevo nodo

    # Método para insertar al final de la lista
    def insertar_final(self, dato):
        """Inserta un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)  # Crear un nuevo nodo con el dato proporcionado
        if self.cabeza is None:  # Si la lista está vacía, el nuevo nodo será la cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:  # Recorremos hasta el final de la lista
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # El último nodo ahora apunta al nuevo nodo

    # Método para eliminar un nodo por su dato
    def eliminar(self, dato):
        """Elimina el primer nodo que contenga el dato proporcionado."""
        actual = self.cabeza
        anterior = None
        while actual is not None:  # Recorremos la lista
            if actual.dato == dato:  # Si encontramos el nodo con el dato buscado
                if anterior is None:  # Si el nodo a eliminar es la cabeza
                    self.cabeza = actual.siguiente  # Actualizamos la cabeza
                else:
                    anterior.siguiente = actual.siguiente  # Saltamos el nodo a eliminar
                return  # Terminamos la operación después de eliminar el nodo
            anterior = actual
            actual = actual.siguiente

    # Método para buscar un nodo por su dato
    def buscar(self, dato):
        """Busca un nodo que contenga el dato especificado."""
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True  # Si encontramos el nodo, devolvemos True
            actual = actual.siguiente
        return False  # Si no encontramos el nodo, devolvemos False

    # Método para imprimir la lista
    def imprimir_lista(self):
        """Imprime todos los nodos de la lista enlazada."""
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")  # Imprimimos el dato de cada nodo
            actual = actual.siguiente  # Avanzamos al siguiente nodo
        print("None")  # Indicar el final de la lista con None

    # Método para verificar si la lista está vacía
    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None  # Si la cabeza es None, la lista está vacía

# Función para validar nombres y apellidos
def validar_nombre_apellido(mensaje):
    while True:
        valor = input(mensaje)
        if valor.replace(" ", "").isalpha() and len(valor.split()) >= 2:
            return valor  # Solo acepta si el valor contiene solo letras y al menos nombre y apellido
        else:
            print("Por favor, ingresa un nombre válido con apellido (solo letras).")

# Clase de prueba para validar los métodos de la lista enlazada simple
if __name__ == "__main__":
    lista = ListaEnlazadaSimple()

    while True:
        print("\nOpciones:")
        print("1. Insertar al inicio (Nombre y Apellido)")
        print("2. Insertar al final (Nombre y Apellido)")
        print("3. Eliminar un nodo (Nombre y Apellido)")
        print("4. Buscar un nodo (Nombre y Apellido)")
        print("5. Imprimir la lista")
        print("6. Verificar si la lista está vacía")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

        if opcion == '1':
            valor = validar_nombre_apellido("Ingresa tu nombre y apellido para insertar al inicio: ")
            lista.insertar_inicio(valor)
            print(f"Nombre {valor} insertado al inicio.")
        elif opcion == '2':
            valor = validar_nombre_apellido("Ingresa tu nombre y apellido para insertar al final: ")
            lista.insertar_final(valor)
            print(f"Nombre {valor} insertado al final.")
        elif opcion == '3':
            valor = validar_nombre_apellido("Ingresa el nombre y apellido que deseas eliminar: ")
            lista.eliminar(valor)
            print(f"Nombre {valor} eliminado.")
        elif opcion == '4':
            valor = validar_nombre_apellido("Ingresa el nombre y apellido que deseas buscar: ")
            encontrado = lista.buscar(valor)
            if encontrado:
                print(f"Nombre {valor} encontrado en la lista.")
            else:
                print(f"Nombre {valor} no encontrado en la lista.")
        elif opcion == '5':
            print("Contenido de la lista:")
            lista.imprimir_lista()
        elif opcion == '6':
            if lista.esta_vacia():
                print("La lista está vacía.")
            else:
                print("La lista no está vacía.")
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 7.")
