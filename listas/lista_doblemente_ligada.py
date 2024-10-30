class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def esta_vacia(self):
        return self.inicio is None

    def insertar_inicio(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo

    def insertar_fin(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.fin
            self.fin = nuevo_nodo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        eliminado = self.inicio.valor
        if self.inicio == self.fin:
            self.inicio = self.fin = None
        else:
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = None
        return eliminado

    def eliminar_fin(self):
        if self.esta_vacia():
            return None
        eliminado = self.fin.valor
        if self.inicio == self.fin:
            self.inicio = self.fin = None
        else:
            self.fin = self.fin.anterior
            self.fin.siguiente = None
        return eliminado

    def buscar(self, valor):
        actual = self.inicio
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        actual = self.inicio
        valores = []
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores

# Función de menú para interactuar con la lista desde la terminal
def menu_interactivo():
    lista = ListaDobleEnlazada()

    while True:
        print("\n--- Menú de Lista Doble Enlazada ---")
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
