from tarea1.diccionario import Diccionario
from tarea1.listaordenadadinamica import ListaOrdenadaDinámica

class TablaHashAbierta(Diccionario):
    def __init__(self, size=12):
        """
        inicializamos el array inicial de la tabla
        por default sería tamaño 12
        """
        self.size = size
        self.lista = [ListaOrdenadaDinámica() for _ in range(size)] #Creamos N instancias de listas dinamicas 
    
    def calculo_hash(self, key) -> int:
        """
        Funcion para calcular el indice de la llave
        """
        suma = 0
        for char in key:
            suma += ord(char)
        index_hash = suma % self.size
        return index_hash
    def __len__(self):
        return self.size
    #-------------
    # Adaptacion de las funciones abstractas
    #-------------
    def inserte(self, elemento):
        """
        Inserta un a la lista dinamica de la llave
        """
        index = self.calculo_hash(elemento)
        self.lista[index].inserte(elemento)

    def borre(self, elemento):
        index = self.calculo_hash(elemento)
        return self.lista[index].borre(elemento)

    def limpie(self):
        """
        Limpia cada lista dinamica
        """
        for index in range(self.size):
            self.lista[index].limpie()

    def miembro(self, elemento):
        index = self.calculo_hash(elemento)
        return self.lista[index].miembro(elemento)
        

    def imprima(self):
        print(self)

    def __str__(self) -> str:
        listas_strings: list[str] = []
        for i in range(self.size):
            lista = self.lista[i]
            if lista.__len__ == 0:         # evita imprimir vacíos
                continue
            listas_strings.append(f"{i + 1}: {lista}")
        return "\n".join(listas_strings) if listas_strings else "(tabla vacía)"
    #------------
    # Fin de adaptacinoes
    #------------
    def __del__(self):
        self.limpie()
        