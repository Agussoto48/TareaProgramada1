import random
import string
import time
import tracemalloc
import csv
from statistics import mean
from rich.console import Console
from rich.table import Table

# Importar las estructuras
from tarea1.listaordenadadinamica import ListaOrdenadaDinámica
from tarea1.listaordenadaestatica import ListaOrdenadaEstática
from tarea1.tablahashabierta import TablaHashAbierta
from tarea1.abbpunteros import AbbPunteros
from tarea1.abbvectorheap import ABBVectorHeap
from tarea1.triepunteros import TriePunteros
from tarea1.triearreglos import TrieArreglos

console = Console()


class AnalizadorRendimiento:
    def __init__(self, n: int):
        self.n = n
        self.repeticiones = 5
        self.datos = self.generar_datos(n)
        self.resultados = []


    def generar_datos(self, n: int) -> list[str]:
        return [
            ''.join(random.choices(string.ascii_lowercase, k=20))
            for _ in range(n)
        ]

    def instanciar_estructuras(self):
        return {
            "ListaOrdenadaDinámica": ListaOrdenadaDinámica,
            "ListaOrdenadaEstática": lambda: ListaOrdenadaEstática(self.n),
            "TablaHashAbierta": TablaHashAbierta,
            "ABB Punteros": AbbPunteros,
            "ABB VectorHeap": ABBVectorHeap,
            "Trie Punteros": TriePunteros,
            "Trie Arreglos": TrieArreglos,
        }

    def _medir(self, funcion):
        """Mide tiempo y memoria de una función."""
        tracemalloc.start()
        t0 = time.perf_counter()
        funcion()
        t1 = time.perf_counter()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return t1 - t0, peak / 1024**2  # segundos, MB

    def prueba_completa(self):
        estructuras = self.instanciar_estructuras()

        tabla = Table(title=f"Prueba Completa (N={self.n})", show_lines=True)
        tabla.add_column("Estructura", justify="left")
        tabla.add_column("Inserción (s)", justify="center")
        tabla.add_column("Búsqueda (s)", justify="center")
        tabla.add_column("Limpieza (s)", justify="center")
        tabla.add_column("Memoria (MB)", justify="center")
        tabla.add_column("Total (s)", justify="center")

        # Archivo CSV
        with open("pruebas.csv", mode="a", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["N", "Estructura", "Inserción (s)", "Búsqueda (s)", "Limpieza (s)", "Memoria (MB)", "Total (s)"])

            for nombre, clase in estructuras.items():
                # Saltar estructuras lentas con el tamaño grande, duran mucho
                if nombre in ("ListaOrdenadaDinámica", "ListaOrdenadaEstática") and self.n >= 100_000:
                    console.print(f"[yellow]Saltando {nombre} (demasiado lenta para N={self.n}).[/]")
                    continue

                console.print(f"[cyan]Analizando {nombre}...[/]")
                tiempos_insert, tiempos_buscar, tiempos_limp, mem_usada, tiempos_total = [], [], [], [], []

                for _ in range(self.repeticiones):
                    dic = clase()
                    tracemalloc.start()
                    t0_total = time.perf_counter()

                    # --- Inserción ---
                    t0 = time.perf_counter()
                    for d in self.datos:
                        dic.inserte(d)
                    t1 = time.perf_counter()

                    # --- Búsqueda ---
                    t2 = time.perf_counter()
                    #Agarra random 10% de datos N y los busca
                    for d in random.sample(self.datos, min(1, len(self.datos)//10)):
                        dic.miembro(d)
                    t3 = time.perf_counter()

                    # --- Limpieza ---
                    t4 = time.perf_counter()
                    dic.limpie()
                    t5 = time.perf_counter()

                    t_total = time.perf_counter() - t0_total
                    _, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()

                    tiempos_insert.append(t1 - t0)
                    tiempos_buscar.append(t3 - t2)
                    tiempos_limp.append(t5 - t4)
                    tiempos_total.append(t_total)
                    mem_usada.append(peak / 1024**2)
                fila = [
                    nombre,
                    f"{mean(tiempos_insert):.4f}",
                    f"{mean(tiempos_buscar):.4f}",
                    f"{mean(tiempos_limp):.4f}",
                    f"{mean(mem_usada):.2f}",
                    f"{mean(tiempos_total):.4f}"
                ]

                tabla.add_row(*fila)
                writer.writerow([self.n, *fila])

        console.print(tabla)
        console.rule("[bold green]Fin de la prueba completa[/]")
