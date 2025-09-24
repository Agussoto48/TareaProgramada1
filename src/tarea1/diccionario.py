from abc import ABC, abstractmethod

class Diccionario(ABC):
    """
    Clase abstracta Diccionario. Dicta los métodos que deben tener los diccionarios.
    
    """
    @abstractmethod
    def inserte(self, elemento):
        """
        Inserta un elemento. Puede ser repetido.
        """
        pass

    @abstractmethod
    def borre(self, elemento):
        pass

    @abstractmethod
    def limpie(self):
        pass

    @abstractmethod
    def miembro(self, elemento):
        pass

    @abstractmethod
    def imprima(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
