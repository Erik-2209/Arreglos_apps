class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def esta_vacia(self):
        return self.inicio is None

    def insertar_inicio(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio
        else:
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo

    def insertar_fin(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio
        else:
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        eliminado = self.inicio.valor
        if self.inicio.siguiente == self.inicio:  # Solo un nodo
            self.inicio = None
        else:
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = self.inicio.siguiente
            self.inicio = self.inicio.siguiente
        return eliminado

    def eliminar_fin(self):
        if self.esta_vacia():
            return None
        actual = self.inicio
        if actual.siguiente == self.inicio:  # Solo un nodo
            eliminado = actual.valor
            self.inicio = None
            return eliminado
        while actual.siguiente.siguiente != self.inicio:
            actual = actual.siguiente
        eliminado = actual.siguiente.valor
        actual.siguiente = self.inicio
        return eliminado

    def buscar(self, valor):
        if self.esta_vacia():
            return False
        actual = self.inicio
        while True:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.inicio:
                break
        return False

    def imprimir(self):
        if self.esta_vacia():
            return []
        actual = self.inicio
        valores = []
        while True:
            valores.append(actual.valor)
            actual = actual.siguiente
            if actual == self.inicio:
                break
        return valores

# Menú interactivo para el usuario
def menu_interactivo():
    lista = ListaCircular()

    while True:
        print("\n--- Menú de Lista Circular ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar del inicio")
        print("4. Eliminar del final")
        print("5. Buscar un valor")
        print("6. Imprimir la lista")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese el valor a insertar al inicio: "))
            lista.insertar_inicio(valor)
            print(f"Valor {valor} insertado al inicio.")

        elif opcion == "2":
            valor = int(input("Ingrese el valor a insertar al final: "))
            lista.insertar_fin(valor)
            print(f"Valor {valor} insertado al final.")

        elif opcion == "3":
            eliminado = lista.eliminar_inicio()
            if eliminado is None:
                print("La lista está vacía.")
            else:
                print(f"Valor {eliminado} eliminado del inicio.")

        elif opcion == "4":
            eliminado = lista.eliminar_fin()
            if eliminado is None:
                print("La lista está vacía.")
            else:
                print(f"Valor {eliminado} eliminado del final.")

        elif opcion == "5":
            valor = int(input("Ingrese el valor a buscar: "))
            encontrado = lista.buscar(valor)
            if encontrado:
                print(f"El valor {valor} se encuentra en la lista.")
            else:
                print(f"El valor {valor} no se encuentra en la lista.")

        elif opcion == "6":
            print("Lista actual:", lista.imprimir())

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú interactivo
menu_interactivo()
