from tarea1.diccionario import Diccionario

class ABBVectorHeap(Diccionario):
    def __init__(self):
        self.vector = []
        
    def _padre(self, i):
        return (i - 1) // 2 if i > 0 else None

    def _izq(self, i):
        return 2 * i + 1

    def _der(self, i):
        return 2 * i + 2
    
    #Reacomoda hacia arriba (sube el elemento si es menor que su padre)
    def _heapify_up(self, i):
        padre = self._padre(i)
        if padre is not None and self.vector[i] < self.vector[padre]:
            self.vector[i], self.vector[padre] = self.vector[padre], self.vector[i]
            self._heapify_up(padre)

    #Reacomoda hacia abajo (baja el elemento si es mayor que sus hijos)
    def _heapify_down(self, i):
        n = len(self.vector)
        izq = self._izq(i)
        der = self._der(i)
        menor = i

        if izq < n and self.vector[izq] < self.vector[menor]:
            menor = izq
        if der < n and self.vector[der] < self.vector[menor]:
            menor = der

        if menor != i:
            self.vector[i], self.vector[menor] = self.vector[menor], self.vector[i]
            self._heapify_down(menor)

    def inserte(self, elemento):
        self.vector.append(elemento)
        self._heapify_up(len(self.vector) - 1)

    def borre(self, elemento):
        if elemento not in self.vector:
            return False
        
        i = self.vector.index(elemento)
        ultimo = self.vector.pop()  
        if i < len(self.vector):
            self.vector[i] = ultimo  
            self._heapify_down(i)
            self._heapify_up(i)
        
        return True

    def miembro(self, elemento):
        return elemento in self.vector

    def limpie(self):
        self.vector.clear()

    def imprima(self):
        print(self.__str__())

    def __str__(self) -> str:
        if not self.vector:
            return "Árbol vacío"
        resultado = []
        nivel = 0
        cantidad_nivel = 1
        i = 0
        n = len(self.vector)
        while i < n:
            elementos_nivel = self.vector[i:i + cantidad_nivel]
            resultado.append(f"Nivel {nivel}: " + " ".join(map(str, elementos_nivel)))
            i += cantidad_nivel
            cantidad_nivel *= 2
            nivel += 1
        return "\n".join(resultado)