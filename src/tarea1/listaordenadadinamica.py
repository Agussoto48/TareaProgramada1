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
        pass

    def inserte(self, elemento):
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
        pass

    def limpie(self):
        pass

    def miembro(self, elemento):
        pass

    def imprima(self):
        print(self)

    def __str__(self) -> str:
        pass
    
    def __del__(self):
        pass