from tarea1.diccionario import Diccionario

class ABBVectorHeap(Diccionario):
    def __init__(self):
        self.vector = []

    def inserte(self, elemento):
        self.vector.append(elemento)
        self.vector.sort()

    def borre(self, elemento):
        if elemento in self.vector:
            self.vector.remove(elemento)
            return True
        return False

    def miembro(self, elemento):
        return elemento in self.vector

    def limpie(self):
        self.vector.clear()

    def imprima(self):
        print(self.__str__())

    def __str__(self)  -> str :
        if not self.vector:
            return "Arbol vacío"
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