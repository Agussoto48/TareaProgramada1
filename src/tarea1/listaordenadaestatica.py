from tarea1.diccionario import Diccionario

class Array:
    def __init__(self, valor_inicial=None, tamaño = None):
        if not isinstance(tamaño, int) or tamaño < 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        if not isinstance(valor_inicial, list):
            self.__lista = [valor_inicial] * tamaño
            self.__tamaño = tamaño
        else:
            self.__lista = valor_inicial
            self.__tamaño = len(valor_inicial)        

    def __getitem__(self, índice):
        if not (0 <= índice < self.__tamaño):
            raise IndexError("Índice de arreglo fuera de los límites.")
        return self.__lista[índice]

    def __setitem__(self, índice, value):
        if not (0 <= índice < self.__tamaño):
            raise IndexError("Índice de arreglo fuera de los límites")
        self.__lista[índice] = value

    def __len__(self):
        return self.__tamaño

    def __repr__(self):
        return f"Array({self.__lista})"
    
    def __str__(self) -> str:
        return str(self.__lista)

class ListaOrdenadaEstática(Diccionario):
    def __init__(self, tamaño):
        self.__arreglo: Array = Array(valor_inicial=0, tamaño=tamaño)
        self.__último: int | None = None

    def __len__(self):
        if self.__último is None:
            return 0
        else:
            return self.__último + 1
    
    def __getitem__(self, índice):
        pass

    def inserte(self, elemento):
        pass

    def borre(self, elemento):
        pass

    def limpie(self):
        pass

    def miembro(self, elemento):
        pass

    def imprima(self):
        print(self)

    def __str__(self) -> str:
        return str(self.__arreglo)
    
    def __del__(self):
        pass