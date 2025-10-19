from tarea1.diccionario import Diccionario

class NodoTriePunteros:
    def __init__(self):
        self.hijos = {}      # diccionario: caracter → NodoTriePunteros
        self.es_fin = False  # True si representa fin de palabra

class TriePunteros(Diccionario):
    def __init__(self):
        self.raiz = NodoTriePunteros()
        self._tamaño = 0

    def inserte(self, elemento: str):
        """Inserta una palabra en el trie (versión con punteros)."""
        nodo = self.raiz
        for char in elemento:
            if not char.isalpha():
                continue  # ignorar caracteres no alfabéticos
            char = char.lower()
            if char not in nodo.hijos:
                nodo.hijos[char] = NodoTriePunteros()
            nodo = nodo.hijos[char]
        if not nodo.es_fin:
            nodo.es_fin = True
            self._tamaño += 1

    def borre(self, elemento: str):
        """Elimina una palabra si existe."""
        def _borre(nodo, elemento, profundidad):
            if nodo is None:
                return False

            if profundidad == len(elemento):
                if nodo.es_fin:
                    nodo.es_fin = False
                    self._tamaño -= 1
                    # Si no tiene hijos, se puede borrar este nodo
                    return len(nodo.hijos) == 0
                return False

            char = elemento[profundidad].lower()
            if char not in nodo.hijos:
                return False

            puede_borrar = _borre(nodo.hijos[char], elemento, profundidad + 1)

            if puede_borrar:
                del nodo.hijos[char]
                return not nodo.es_fin and len(nodo.hijos) == 0
            return False

        _borre(self.raiz, elemento, 0)

    def limpie(self):
        """Elimina todas las palabras del trie."""
        self.raiz = NodoTriePunteros()
        self._tamaño = 0

    def miembro(self, elemento: str) -> bool:
        """Verifica si una palabra está en el trie."""
        nodo = self.raiz
        for char in elemento:
            if not char.isalpha():
                continue
            char = char.lower()
            if char not in nodo.hijos:
                return False
            nodo = nodo.hijos[char]
        return nodo.es_fin

    def imprima(self):
        """Imprime todas las palabras almacenadas."""
        palabras = self._listar_palabras()
        for palabra in palabras:
            print(palabra)

    def __str__(self):
        """Devuelve una cadena con todas las palabras."""
        return ", ".join(self._listar_palabras())

    # ----------------------------------------------------------
    # Métodos auxiliares
    # ----------------------------------------------------------

    def _listar_palabras(self):
        """Devuelve todas las palabras almacenadas."""
        resultado = []

        def _dfs(nodo, prefijo):
            if nodo.es_fin:
                resultado.append(prefijo)
            for char, hijo in nodo.hijos.items():
                _dfs(hijo, prefijo + char)

        _dfs(self.raiz, "")
        return resultado

    def __len__(self):
        return self._tamaño