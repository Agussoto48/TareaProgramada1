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
        if self.__último is None or índice < 0 or índice > self.__último:
            raise IndexError("Índice fuera de rango")
        return self.__arreglo[índice]

    def inserte(self, elemento):
        """Inserta en orden creciente"""
        # Caso: lista vacía
        if self.__último is None:
            self.__arreglo[0] = elemento
            self.__último = 0
            return
        
        # Verificar que haya espacio
        if self.__último + 1 >= len(self.__arreglo):
            raise OverflowError("Lista llena, no se puede insertar")

        # Encontrar la posición de inserción (ordenada)
        i = 0
        while i <= self.__último and self.__arreglo[i] < elemento:
            i += 1

        # Desplazar elementos a la derecha
        for j in range(self.__último, i - 1, -1):
            self.__arreglo[j + 1] = self.__arreglo[j]

        # Insertar nuevo elemento
        self.__arreglo[i] = elemento
        self.__último += 1

    def borre(self, elemento):
        """Elimina la primera ocurrencia"""
        if self.__último is None:
            return False

        # Buscar elemento
        i = 0
        while i <= self.__último and self.__arreglo[i] != elemento:
            i += 1

        if i > self.__último:
            return False  # No encontrado

        # Desplazar elementos a la izquierda
        for j in range(i, self.__último):
            self.__arreglo[j] = self.__arreglo[j + 1]

        self.__último -= 1
        if self.__último < 0:
            self.__último = None
        return True

    def limpie(self):
        """Vacía la lista"""
        self.__último = None

    def miembro(self, elemento):
        """Verifica si el elemento está en la lista"""
        if self.__último is None:
            return False
        for i in range(self.__último + 1):
            if self.__arreglo[i] == elemento:
                return True
        return False

    def imprima(self):
        if self.__último is None:
            print("[]")
        else:
            print([self.__arreglo[i] for i in range(self.__último + 1)])

    def __str__(self) -> str:
        if self.__último is None:
            return "[]"
        return str([self.__arreglo[i] for i in range(self.__último + 1)])
    
    def __del__(self):
        self.__último = None