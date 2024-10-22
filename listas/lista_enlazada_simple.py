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

# Clase de prueba para validar los métodos de la lista enlazada simple
if __name__ == "__main__":
    # Creación de una lista enlazada simple
    lista = ListaEnlazadaSimple()

    # Insertar elementos al inicio de la lista
    lista.insertar_inicio(10)
    lista.insertar_inicio(20)

    # Insertar elemento al final de la lista
    lista.insertar_final(30)

    # Imprimir la lista después de las inserciones
    print("Lista después de las inserciones:")
    lista.imprimir_lista()  # Debería imprimir: 20 -> 10 -> 30 -> None

    # Buscar elementos en la lista
    print("¿Está 10 en la lista?", lista.buscar(10))  # Debería ser True
    print("¿Está 40 en la lista?", lista.buscar(40))  # Debería ser False

    # Eliminar un nodo de la lista
    lista.eliminar(10)
    print("Lista después de eliminar el nodo 10:")
    lista.imprimir_lista()  # Debería imprimir: 20 -> 30 -> None

    # Verificar si la lista está vacía
    print("¿La lista está vacía?", lista.esta_vacia())  # Debería ser False
