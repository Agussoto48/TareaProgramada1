from tarea1.diccionario import Diccionario

class NodoTrieArray:
    def __init__(self):
        self.hijos = [None] * 26   # hijos[a-z]
        self.es_fin = False        # fin de palabra

class TrieArreglos(Diccionario):
    def __init__(self):
        self.raiz = NodoTrieArray()
        self._tamaño = 0           # cantidad de palabras almacenadas

    def _indice(self, char):
        """Convierte un carácter en índice 0–25."""
        return ord(char.lower()) - ord('a')

    def inserte(self, elemento: str):
        """Inserta una palabra en el trie."""
        nodo = self.raiz
        for char in elemento:
            if not char.isalpha():
                continue  # ignorar caracteres no alfabéticos
            i = self._indice(char)
            if nodo.hijos[i] is None:
                nodo.hijos[i] = NodoTrieArray()
            nodo = nodo.hijos[i]
        if not nodo.es_fin:
            nodo.es_fin = True
            self._tamaño += 1

    def borre(self, elemento: str):
        """Elimina una palabra del trie si existe."""
        def _borre(nodo, elemento, profundidad):
            if nodo is None:
                return False

            if profundidad == len(elemento):
                if nodo.es_fin:
                    nodo.es_fin = False
                    self._tamaño -= 1
                    # Si no tiene hijos, se puede borrar este nodo
                    return not any(nodo.hijos)
                return False

            i = self._indice(elemento[profundidad])
            puede_borrar = _borre(nodo.hijos[i], elemento, profundidad + 1)

            if puede_borrar:
                nodo.hijos[i] = None
                return not nodo.es_fin and not any(nodo.hijos)
            return False

        _borre(self.raiz, elemento, 0)

    def limpie(self):
        """Elimina todas las palabras del trie."""
        self.raiz = NodoTrieArray()
        self._tamaño = 0

    def miembro(self, elemento: str) -> bool:
        """Verifica si una palabra pertenece al trie."""
        nodo = self.raiz
        for char in elemento:
            if not char.isalpha():
                continue
            i = self._indice(char)
            if nodo.hijos[i] is None:
                return False
            nodo = nodo.hijos[i]
        return nodo.es_fin

    def imprima(self):
        """Imprime todas las palabras almacenadas."""
        palabras = self._listar_palabras()
        for palabra in palabras:
            print(palabra)

    def __str__(self):
        """Devuelve una representación en cadena del contenido."""
        return ", ".join(self._listar_palabras())

    # ----------------------------------------------------------
    # Métodos auxiliares
    # ----------------------------------------------------------

    def _listar_palabras(self):
        """Devuelve todas las palabras almacenadas en una lista."""
        resultado = []

        def _dfs(nodo, prefijo):
            if nodo is None:
                return
            if nodo.es_fin:
                resultado.append(prefijo)
            for i in range(26):
                if nodo.hijos[i] is not None:
                    _dfs(nodo.hijos[i], prefijo + chr(ord('a') + i))

        _dfs(self.raiz, "")
        return resultado

    def __len__(self):
        return self._tamaño