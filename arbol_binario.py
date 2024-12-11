class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        """Insertar un nuevo valor en el árbol"""
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
    
    def buscar(self, valor):
        """Buscar un valor en el árbol"""
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo_actual, valor):
        # Si el nodo es None o encontramos el valor
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        
        # Si el valor es menor, busca en el subárbol izquierdo
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        
        # Si el valor es mayor, busca en el subárbol derecho
        return self._buscar_recursivo(nodo_actual.derecho, valor)
    
    def recorrido_inorden(self):
        """Recorrido inorden del árbol"""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            # Primero recorre el subárbol izquierdo
            self._inorden_recursivo(nodo.izquierdo, resultado)
            # Agrega el valor actual
            resultado.append(nodo.valor)
            # Luego recorre el subárbol derecho
            self._inorden_recursivo(nodo.derecho, resultado)
    
    def altura(self):
        """Calcular la altura del árbol"""
        return self._calcular_altura(self.raiz)
    
    def _calcular_altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(
            self._calcular_altura(nodo.izquierdo), 
            self._calcular_altura(nodo.derecho)
        )

# Función para probar el árbol binario
def probar_arbol_binario():
    # Crear una instancia del árbol
    arbol = ArbolBinario()
    
    # Insertar valores
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)
    
    # Pruebas de funcionalidad
    print("1. Recorrido Inorden:")
    print(arbol.recorrido_inorden())
    
    # Prueba de búsqueda
    valor_buscar = 40
    nodo = arbol.buscar(valor_buscar)
    if nodo:
        print(f"\n2. Valor {valor_buscar} encontrado en el árbol")
    else:
        print(f"\n2. Valor {valor_buscar} NO encontrado en el árbol")
    
    # Prueba de altura
    print(f"\n3. Altura del árbol: {arbol.altura()}")
    
    # Prueba de búsqueda de valor no existente
    valor_no_existente = 100
    nodo = arbol.buscar(valor_no_existente)
    if nodo:
        print(f"\n4. Valor {valor_no_existente} encontrado en el árbol")
    else:
        print(f"\n4. Valor {valor_no_existente} NO encontrado en el árbol")

# Ejecutar las pruebas
if __name__ == "__main__":
    probar_arbol_binario()