from tarea1.diccionario import Diccionario

class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.izq = None
        self.der = None

class AbbPunteros(Diccionario):
    def __init__(self):
        self.raiz = None

    def inserte(self, elemento):
        self.raiz = self._insertar(self.raiz, elemento)

    def _insertar(self, nodo, elemento):
        if nodo is None:
            return Nodo(elemento)
        if elemento < nodo.elemento:
            nodo.izq = self._insertar(nodo.izq, elemento)
        else:
            nodo.der = self._insertar(nodo.der, elemento)
        return nodo

    def borre(self, elemento):
        encontrado, self.raiz = self._borrar(self.raiz, elemento)
        return encontrado

    def _borrar(self, nodo, elemento):
        if nodo is None:
            return False, None

        if elemento < nodo.elemento:
            encontrado, nodo.izq = self._borrar(nodo.izq, elemento)
            return encontrado, nodo
        elif elemento > nodo.elemento:
            encontrado, nodo.der = self._borrar(nodo.der, elemento)
            return encontrado, nodo
        else:
            # Nodo encontrado
            # Caso 1: sin hijos
            if nodo.izq is None and nodo.der is None:
                return True, None
            # Caso 2: un solo hijo
            elif nodo.izq is None:
                return True, nodo.der
            elif nodo.der is None:
                return True, nodo.izq
            # Caso 3: dos hijos
            else:
                sucesor = self._minimo(nodo.der)
                nodo.elemento = sucesor.elemento
                _, nodo.der = self._borrar(nodo.der, sucesor.elemento)
                return True, nodo

    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

    def miembro(self, elemento):
        return self._buscar(self.raiz, elemento)

    def _buscar(self, nodo, elemento):
        if nodo is None:
            return False
        if elemento == nodo.elemento:
            return True
        elif elemento < nodo.elemento:
            return self._buscar(nodo.izq, elemento)
        else:
            return self._buscar(nodo.der, elemento)

    def limpie(self):
        self.raiz = None

    def imprima(self):
        print(self.__str__())

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izq)
            print(nodo.elemento, end=" ")
            self._inorden(nodo.der)

    def __str__(self):
        if not self.raiz:
            return "Arbol vacio"
        elementos = []
        self._inorden_str(self.raiz, elementos)
        return " ".join(map(str, elementos))

    def _inorden_str(self, nodo, lista):
        if nodo:
            self._inorden_str(nodo.izq, lista)
            lista.append(nodo.elemento)
            self._inorden_str(nodo.der, lista)
