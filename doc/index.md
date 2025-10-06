# Tarea Programada 1

**Autores:**

- Andres Salas Acuña — C37104
- Agustín Soto Chaves — C4K199

## Introducción

Este proyecto implementa tres estructuras de datos que permiten almacenar y gestionar elementos de forma eficiente: una **lista ordenada estática** (basada en arreglos), una **lista ordenada dinámica** (basada en nodos enlazados) y una **tabla hash abierta** (basada en listas dinámicas).

Todas estas estructuras heredan de una clase base abstracta llamada `Diccionario`, la cual define una interfaz común que incluye las operaciones fundamentales: **inserción**, **borrado**, **búsqueda**, **limpieza** e **impresión**, esto garantiza que las tres implementaciones sean intercambiables y comparables bajo el mismo modelo lógico de funcionamiento.

El objetivo general es comparar el rendimiento, la eficiencia y el comportamiento de cada estructura frente a distintas cargas de trabajo, las listas ordenadas (estática y dinámica) permiten mantener los elementos en orden, pero presentan un tiempo de inserción y búsqueda proporcional al tamaño de la lista, en contraste la tabla hash abierta utiliza una función de dispersión (**hash**) para calcular la posición de almacenamiento de cada elemento, alcanzando un tiempo promedio de acceso **constante O(1)**, incluso con grandes volúmenes de datos.

## Archivo: `listaordenadaestatica.py`

Implementa una **lista ordenada estática** utilizando el arreglo definido en la clase `Array`, el tamaño máximo se define al momento de creación y no puede crecer dinámicamente.

### Comportamiento

- Inserta elementos de forma ordenada ascendente.
- Al insertar, los elementos mayores se desplazan a la derecha para mantener el orden.
- Al eliminar, los elementos posteriores se desplazan a la izquierda.
- Verifica si un elemento es miembro mediante búsqueda lineal.
- Permite limpiar completamente la lista y obtener su representación en texto.

## Archivo: `listaordenadadinamica.py`

Representa un nodo individual de la lista enlazada, cada nodo almacena un elemento y una referencia (`siguiente`) al nodo siguiente, y se utiliza como unidad básica para construir la lista dinámica ordenada.

Con esta Implementación, la lista ordenada dinámica, a diferencia
de la lista estática, su tamaño no está limitado y puede crecer o
reducirse según las operaciones realizadas.

### Comportamiento

- Mantiene el orden ascendente automáticamente al insertar.
- Cada inserción encuentra la posición correcta recorriendo los nodos O(n).
- Al eliminar, ajusta los punteros para mantener la conexión de la lista.
- Permite acceder a un elemento por índice mediante recorrido.
- Implementa operaciones de búsqueda (`miembro`) y limpieza (`limpie`).

## Tabla Hash

Una Tabla Hash es una estructura de datos que permite
almacenar elementos asociados a una clave y acceder a ellos
rápidamente mediante una función hash, dicha función convierte la
clave en un número entero que indica la posición donde el elemento se
guardará dentro de un arreglo, cuando dos claves producen el mismo
índice (lo que sería una colisión), se aplican técnicas para resolverlo, entre ellas, el encadenamiento separado (hash abierto) guarda los elementos que colisionan en una lista enlazada asociada a esa posición.

El uso de una función hash adecuada y un control del factor de
carga garantizan que las operaciones de inserción, búsqueda y
eliminación se realicen en tiempo promedio constante O(1), incluso con
grandes volúmenes de datos.

## Archivo: `tablahashabierta.py`

La **Tabla Hash** Abierta amplía el conjunto de estructuras implementadas en este proyecto, introduciendo un enfoque más eficiente para la búsqueda, inserción y eliminación de elementos, a diferencia de las listas ordenadas (estática y dinámica), que dependen de recorridos secuenciales, la tabla hash utiliza una función hash para determinar la posición de cada elemento en una tabla de acceso directo, permitiendo operaciones promedio en tiempo constante. Esta estructura también hereda de la clase abstracta Diccionario, garantizando compatibilidad con las mismas operaciones básicas (inserte, borre, miembro, limpie, imprima).

## Función Hash y Aleatoriedad

La función hash utilizada convierte cada carácter de la clave en su valor numérico y los combina multiplicativamente con una base prima (47), calculando luego el módulo con el tamaño de la tabla (inicialmente 11), esto genera un valor uniforme dentro del rango de índices disponibles.

Una buena función hash debe distribuir los elementos de manera uniforme entre las posiciones, evitando colisiones, para evaluar su **aleatoriedad**, se observa la longitud promedio de las listas en la tabla: si la mayoría tiene tamaños similares, la dispersión se considera adecuada; una distribución equilibrada mantiene el rendimiento esperado de O(1).

### Comportamiento

- Convierte las hileras (`string`) en números enteros mediante la función hash.
- Calcula la posición del elemento con el operador módulo (`%`).
- Si dos elementos generan el mismo índice (colisión), ambos se almacenan en una lista enlazada ordenada (`ListaOrdenadaDinámica`).

## Redistribución (Rehash)

Cuando la tabla alcanza un alto **factor de carga**, es decir, cuando el número de elementos almacenados **N** se aproxima al tamaño de la tabla **M** las colisiones se vuelven más frecuentes, en este caso se investigó que cuando **N/M > 0.7** se tiene que implementar este proceso.

Para mantener la eficiencia, se realiza un proceso de **redistribución o rehash**, que consiste en:

1. Crear una nueva tabla del doble de tamaño.
2. Recalcular el índice hash de cada elemento con el nuevo tamaño.
3. Reinsertar todos los elementos en sus nuevas posiciones.

Este proceso tiene una **complejidad temporal de O(N)** y garantiza que el rendimiento general de la tabla no se degrade a medida que crece el número de elementos.

## Comparación general

| Característica                    | Lista Estática | Lista Dinámica  | Tabla Hash Abierta          |
| --------------------------------- | -------------- | --------------- | --------------------------- |
| **Estructura base**               | Arreglo fijo   | Nodos enlazados | Arreglo de listas enlazadas |
| **Tamaño**                        | Limitado       | Dinámico        | Dinámico                    |
| **Inserción**                     | O(n)           | O(n)            | O(1)                        |
| **Eliminación**                   | O(n)           | O(n)            | O(1)                        |
| **Búsqueda**                      | O(n)           | O(n)            | O(1)                        |
| **Uso de memoria**                | Bajo           | Medio           | Alto                        |
| **Flexibilidad**                  | Limitada       | Alta            | Muy alta                    |
| **Complejidad de implementación** | Baja           | Media           | Alta                        |
| **Redistribución (rehash)**       | No aplica      | No aplica       | O(N) ocasional              |
