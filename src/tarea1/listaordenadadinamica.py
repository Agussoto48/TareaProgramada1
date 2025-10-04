from tarea1.diccionario import Diccionario

class Nodo:
    def __init__(self, elemento:str=''):
        self.elemento = elemento
        self.siguiente: Nodo | None = None

class ListaOrdenadaDinámica(Diccionario):
    def __init__(self):
        self.__cabeza = Nodo()
        self.__tamaño = 0

    def __len__(self):
        return self.__tamaño
    
    def __getitem__(self, indice):
        if indice < 0 or indice >= self.__tamaño:
            raise IndexError("Índice fuera de rango")
        actual = self.__cabeza.siguiente
        for _ in range(indice):
            actual = actual.siguiente
        return actual.elemento

    def inserte(self, elemento):
        self.__tamaño += 1
        referencia: Nodo = self.__cabeza
        nodo = Nodo(elemento)
        if referencia.siguiente is None:
            referencia.siguiente = nodo
        else:
            while referencia.siguiente.siguiente is not None and elemento > referencia.siguiente.elemento:
                referencia = referencia.siguiente
            nodo.siguiente = referencia.siguiente
            referencia.siguiente = nodo

    def borre(self, elemento):
        """Elimina la primera ocurrencia"""
        referencia = self.__cabeza
        while referencia.siguiente is not None and referencia.siguiente.elemento != elemento:
            referencia = referencia.siguiente

        if referencia.siguiente is None:
            return False  # No encontrado

        referencia.siguiente = referencia.siguiente.siguiente
        self.__tamaño -= 1
        return True
    
    def limpie(self):
        """Vacía la lista"""
        self.__cabeza.siguiente = None
        self.__tamaño = 0

    def miembro(self, elemento):
        """Verifica si el elemento está en la lista"""
        actual = self.__cabeza.siguiente
        while actual is not None:
            if actual.elemento == elemento:
                return True
            actual = actual.siguiente
        return False

    def imprima(self):
        print(self)

    def __str__(self) -> str:
        elementos = []
        actual = self.__cabeza.siguiente
        while actual is not None:
            elementos.append(actual.elemento)
            actual = actual.siguiente
        return str(elementos)
    
    def __del__(self):
        self.limpie()