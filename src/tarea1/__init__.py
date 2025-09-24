# -*- coding: utf-8 -*-
"""
Programa principal para utilizar el modelo Diccionario.

Programado por Braulio José Solano Rojas.
"""

from __future__ import annotations

import sys

from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from tarea1.diccionario import Diccionario
from tarea1.listaordenadadinamica import ListaOrdenadaDinámica
from tarea1.listaordenadaestatica import ListaOrdenadaEstática

console = Console()


# =====================
# Utilidades de pantalla
# =====================


def panel_contenido(
    texto: str, *, titulo: str = "Diccionario", width: int | None = None
) -> None:
    """Imprime un Panel con doble línea y fondo azul, como el recuadro del Pascal."""
    console.clear()
    if width is None:
        # Mantener proporción similar a 80 columnas del original
        width = min(80, max(40, console.size.width - 4))
    panel = Panel(
        Align.left(texto),
        title=titulo,
        title_align="center",
        padding=(1, 4),
        box=box.DOUBLE,
        width=width,
        style="white on blue",
    )
    console.print(panel, justify="left")


def pausa(msg: str = "Pulse [bold]Enter[/] para continuar…") -> None:
    Prompt.ask(msg, default="", show_default=False)


def leer_hilera(pregunta: str) -> str:
    """Lee una hilera similar a TDato (máx. 20 chars como en el Pascal)."""
    s = Prompt.ask(pregunta).strip()
    return s[:20]


# =====================
# Lectura de una tecla (sin Enter)
# =====================


def leer_tecla(validos: str) -> str:
    """Lee una sola tecla y la devuelve sin requerir Enter.

    - En Windows usa `msvcrt.getwch()`.
    - En Unix usa `termios` + `tty` en modo raw.
    Ignora teclas fuera de `validos`.
    """
    try:
        import msvcrt  # type: ignore
    except Exception:
        msvcrt = None  # type: ignore

    if msvcrt is not None:  # Windows
        while True:
            ch = msvcrt.getwch()
            # Descartar prefijos de teclas especiales (setas, F1, etc.)
            if ch in ("\x00", "\xe0"):
                _ = msvcrt.getwch()
                continue
            if ch in validos:
                console.print(ch, end="")  # eco visual como en Pascal
                return ch
    else:  # Unix
        import termios
        import tty

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in validos:
                    console.print(ch, end="")
                    return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


# =====================
# Operaciones de menú
# =====================


def agregar(diccionario: Diccionario) -> None:
    texto = "Digite la hilera que desea agregar:"
    panel_contenido(texto)
    h = leer_hilera("")
    if diccionario.miembro(h):
        console.print("[yellow]El elemento YA existe.[/]")
    else:
        diccionario.inserte(h)
        console.print("[green]Elemento insertado.[/]")
    pausa()


def borrar(diccionario: Diccionario) -> None:
    texto = "Digite la hilera que desea borrar:"
    panel_contenido(texto)
    h = leer_hilera("")
    if diccionario.borre(h):
        console.print("[green]Elemento borrado.[/]")
    else:
        console.print("[red]El elemento NO existe.[/]")
    pausa()


def existencia(diccionario: Diccionario) -> None:
    texto = "Digite la hilera que desea verificar:"
    panel_contenido(texto)
    h = leer_hilera("")
    if diccionario.miembro(h):
        console.print("[green]El elemento existe.[/]")
    else:
        console.print("[red]El elemento NO existe.[/]")
    pausa()


def imprimir(diccionario: Diccionario) -> None:
    panel_contenido("Imprimir el diccionario")
    diccionario.imprima()
    pausa()


def limpiar(diccionario: Diccionario) -> None:
    diccionario.limpie()
    panel_contenido("Diccionario limpio.")
    pausa()


# ============
# Menúes
# ============

def render_menu_etapa() -> None:
    cuerpo = (
        "\n"  # deja un margen superior dentro del panel
        "            Etapa\n\n"
        "[1] Menú diccionarios (entregas 1 y 2)\n"
        "[2] Pruebas de rendimiento ([italic]benchmarking[/])\n\n"
        "Digite una opción [_]"
    )
    panel_contenido(cuerpo)


def render_menu_clase() -> None:
    cuerpo = (
        "\n"  # deja un margen superior dentro del panel
        "            Clase Diccionario\n\n"
        "[1] ListaOrdenadaDinámica\n"
        "[2] ListaOrdenadaEstática\n"
        "[3] TablaHashAbierta\n"
        "[4] ABBPunteros\n"
        "[5] ABBVectorHeap\n"
        "[6] TriePunteros\n"
        "[7] TrieArreglos\n\n"
        "Digite una opción [_]"
    )
    panel_contenido(cuerpo)


def render_menu_diccionario() -> None:
    cuerpo = (
        "\n"  # deja un margen superior dentro del panel
        "            Diccionario\n\n"
        "[1] Agregar un elemento al diccionario\n"
        "[2] Borrar un elemento del diccionario\n"
        "[3] Existencia de un elemento en el diccionario\n"
        "[4] Imprimir el diccionario\n"
        "[5] Limpiar el diccionario\n"
        "[6] Salir\n\n"
        "Digite una opción [_]"
    )
    panel_contenido(cuerpo)


def menu_etapa() -> str:
    try:
        render_menu_etapa()
        # leer una sola tecla válida y eco inmediato
        return leer_tecla("12")
    except BaseException:
        raise ValueError("No se pudo devolver una opción.")


def menu_clase() -> Diccionario:
    try:
        while True:
            render_menu_clase()
            # leer una sola tecla válida y eco inmediato
            opcion = leer_tecla("1234567")
            match opcion:
                case "1":
                    return ListaOrdenadaDinámica()
                case "2":
                    return ListaOrdenadaEstática(100)
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    pass
    except BaseException:
        raise ValueError("No se pudo instanciar una clase diccionario.")


def menu_diccionario(diccionario: Diccionario) -> None:
    try:
        while True:
            render_menu_diccionario()
            # leer una sola tecla válida y eco inmediato
            opcion = leer_tecla("123456")
            # pequeña pausa visual como en Pascal
            # (no Delay, pero el eco ya se ve)
            match opcion:
                case "1":
                    agregar(diccionario)
                case "2":
                    borrar(diccionario)
                case "3":
                    existencia(diccionario)
                case "4":
                    imprimir(diccionario)
                case "5":
                    limpiar(diccionario)
                case "6":
                    console.clear()
                    break
    finally:
        del diccionario


def main() -> None:
    opcion = menu_etapa()
    match opcion:
        case "1":
            diccionario = menu_clase()
            menu_diccionario(diccionario)
        case "2":
            pass


if __name__ == "__main__":
    main()