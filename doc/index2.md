# Tarea Programada 1 / Avance 2

**Autores:**

- Andres Salas Acuña — C37104
- Agustín Soto Chaves — C4K199

## Introducción

En esta ampliación del proyecto se incorporan dos nuevas familias de estructuras de datos basadas en el modelo Diccionario: **Tries (Arboles de prefijos)**, que permiten almacenar cadenas de caracteres de forma estructurada por niveles y **Árboles Binarios de Búsqueda (ABB)**, que organizan los elementos según su valor relativo, facilitando la búsqueda ordenada.

Cada estructura presenta una implementación por **arreglos (basada en índices y vectores)** y otra **por punteros (basada en nodos enlazados)**.
Ambas respetan la interfaz común definida por la clase abstracta Diccionario, garantizando la compatibilidad con el resto del proyecto.

El objetivo principal es analizar las diferencias en complejidad temporal, uso de memoria y flexibilidad, observando cómo la representación interna (arreglo vs punteros) afecta el comportamiento de las operaciones fundamentales.
------------------------
## Trie
Un ***Trie (del inglés retrieval tree)*** es una estructura de datos en forma de árbol que se utiliza para almacenar cadenas de caracteres (como palabras) de manera que los ***prefijos*** comunes se compartan entre ellas.
Cada nivel del árbol representa una letra, y los nodos intermedios conducen a posibles continuaciones.

Por ejemplo, las palabras “sol” y “sopa” comparten el prefijo “so”, por lo que sus rutas en el trie comparten los dos primeros nodos.

### Ventajas:
- Permite buscar, insertar o eliminar palabras en tiempo proporcional a su longitud (O(L)).
- Ideal para aplicaciones como autocompletado, corrección ortográfica o búsqueda por prefijos.

### Desventaja:
- Consume más memoria que una lista o tabla hash, especialmente si las palabras no comparten muchos prefijos.
------------------------
## Archivo: triearreglos.py

El **Trie por Arreglos** utiliza un enfoque basado en índices numéricos y listas anidadas para representar los nodos del árbol. Cada nivel corresponde a un carácter de la cadena y los hijos se almacenan en una tabla fija (por ejemplo, de tamaño 26 para letras en minúscula).

### Comportamiento

- Cada nodo es un arreglo de tamaño fijo con 26 posiciones (una por letra del alfabeto).
- Cada carácter de la palabra determina el índice del siguiente nodo (índice = ord(letra) - ord('a')).
- Los nodos terminales marcan el final de una palabra válida.
- Inserciones y búsquedas recorren los niveles según las letras de la cadena.
- Elimina y limpia los nodos vacíos si ya no representan palabras válidas.
------------------------
## Archivo: triepunteros.py

El ***Trie por Punteros*** utiliza nodos enlazados dinámicamente, donde cada nodo contiene un diccionario que mapea caracteres a sus hijos.
Es más flexible que la versión por arreglos, ya que no necesita reservar memoria para caracteres inexistentes.

### Comportamiento

- Cada nodo es un objeto con un atributo hijos (diccionario {char: nodo}) y un indicador fin_palabra.
- Las palabras se insertan creando enlaces dinámicos para cada carácter.
- Las búsquedas y borrados son recursivos y eficientes en longitud de palabra.
- El espacio ocupado depende directamente de los caracteres efectivamente usados.
------------------------
## Arboles

Un ***Árbol Binario de Búsqueda (ABB)*** es una estructura en forma de árbol donde cada nodo tiene como máximo dos hijos:

Los valores menores se almacenan en el subárbol izquierdo.

Los valores mayores en el subárbol derecho.

Esta propiedad permite buscar, insertar y eliminar elementos de forma eficiente, ya que cada comparación descarta la mitad del árbol.

### Ventajas:
- Búsqueda, inserción y eliminación con complejidad promedio O(log n).
- Mantiene los elementos ordenados naturalmente.

### Desventaja:
- Si no se balancea, puede degradarse a una lista lineal (O(n)) cuando los datos se insertan en orden.
------------------------
## Archivo: abbvectorheap.py

El ***Árbol Binario de Búsqueda por Arreglo (ABBVectorHeap)*** simula la estructura de un árbol binario utilizando un vector ordenado.
Cada inserción conserva el orden mediante operaciones de desplazamiento o reordenamiento del vector.

### Comportamiento

- Los elementos se mantienen siempre ordenados dentro del arreglo.
- Las búsquedas se realizan mediante recorridos lineales o binarios.
- Permite imprimir el árbol simulando niveles de profundidad.
- Es una versión conceptual simple, más cercana a un heap ordenado que a un árbol dinámico real.
------------------------
## Archivo: abbpunteros.py

El ***Árbol Binario de Búsqueda por Punteros (AbbPunteros)*** utiliza nodos enlazados con referencias a sus hijos izquierdo y derecho, representando fielmente la estructura clásica de un árbol binario.

### Comportamiento

- Cada nodo almacena un valor y dos punteros (izq, der).
- Inserta recursivamente siguiendo el orden: menores a la izquierda, mayores a la derecha.
- El borrado contempla los tres casos clásicos (sin hijos, un hijo o dos hijos).
- La impresión se realiza mediante recorrido inorden, mostrando los elementos ordenados ascendentemente.
------------------------

## Comparación general

| Característica                    | Trie (Arreglos)               | Trie (Punteros)               | ABB VectorHeap             | ABB Punteros              |
| --------------------------------- | ----------------------------- | ----------------------------- | -------------------------- | ------------------------- |
| **Estructura base**               | Arreglo fijo                  | Nodos enlazados               | Arreglo ordenado           | Nodos enlazados           |
| **Tipo de datos**                 | Cadenas                       | Cadenas                       | Genéricos ordenables       | Genéricos ordenables      |
| **Tamaño**                        | Limitado (alfabeto fijo)      | Dinámico                      | Dinámico                   | Dinámico                  |
| **Inserción**                     | O(L)                          | O(L)                          | O(n·log n)                 | O(log n)                  |
| **Búsqueda**                      | O(L)                          | O(L)                          | O(log n)                   | O(log n)                  |
| **Eliminación**                   | O(L)                          | O(L)                          | O(n)                       | O(log n)                  |
| **Uso de memoria**                | Alto                          | Medio                         | Medio                      | Medio                     |
| **Flexibilidad**                  | Baja (tabla fija)             | Alta (crecimiento dinámico)   | Media                      | Alta                      |
| **Complejidad de implementación** | Alta                          | Media                         | Baja                       | Media                     |
| **Eficiencia promedio**           | Muy alta en prefijos          | Alta                          | Media                      | Alta                      |