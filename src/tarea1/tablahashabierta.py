from tarea1.diccionario import Diccionario
from tarea1.listaordenadadinamica import ListaOrdenadaDinámica

class TablaHashAbierta(Diccionario):
    def __init__(self, size=11):
        """
        inicializamos el array inicial de la tabla
        por default sería tamaño 12
        """
        self.original_size = size
        self.size = size
        self.lista = [ListaOrdenadaDinámica() for _ in range(size)] #Creamos N instancias de listas dinamicas 
        self.numElementos = 0
    
    def calculo_hash(self, key) -> int:
        """
        Funcion para calcular el indice de la llave
        """
        valor = 0
        for char in key:
            #Se usa un numero primo para mejor dispersion
            valor = (valor * 47 + ord(char)) % self.size
        return valor
    
    def __len__(self):
        return self.size
    
    def carga(self):
        c = self.numElementos / self.size
        if c > 0.7:
            self.rehash()

    def rehash(self):
        tabla_vieja = self.lista
        nuevo_size = self.size * 2

        self.lista = [ListaOrdenadaDinámica() for _ in range(nuevo_size)]
        self.size = nuevo_size
        self.numElementos = 0
        for lista in tabla_vieja:
            largo = len(lista)
            for i in range(largo):
                elemento = lista[i]
                self.inserte(elemento)


    
    #-------------
    # Adaptacion de las funciones abstractas
    #-------------
    def inserte(self, elemento):
        """
        Inserta un a la lista dinamica de la llave
        """
        self.numElementos += 1
        index = self.calculo_hash(elemento)
        self.lista[index].inserte(elemento)
        self.carga()

    def borre(self, elemento):
        index = self.calculo_hash(elemento)
        if(self.lista[index].borre(elemento)):
            self.numElementos -= 1
            return True
        else:
            return False

    def limpie(self):
        """
        Limpia cada lista dinamica
        """
        self.numElementos = 0
        for index in range(self.size):
            self.lista[index].limpie()
        #Volvemos a los valores inciales 
        self.lista = [ListaOrdenadaDinámica() for _ in range(self.original_size)]
        self.size = self.original_size

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
        