# Juan David Martinez Mira
# Formato de entrada: primero tamaño del tablero (n), luego coordenadas de la reina (fila columna) separadas por espacio.
# Muchos Bloqueos

import random


tamano = int(input("Tamaño del tablero: "))
reina_x = int(input("Coordenada X de la reina (1 a {}): ".format(tamano)))
reina_y = int(input("Coordenada Y de la reina (1 a {}): ".format(tamano)))
num_bloqueos = int(input("Número de bloqueos aleatorios: "))


tablero = [["." for _ in range(tamano)] for _ in range(tamano)]
tablero[reina_y - 1][reina_x - 1] = "R"

bloqueos = set()
while len(bloqueos) < num_bloqueos:
    bx = random.randint(1, tamano)
    by = random.randint(1, tamano)
    if (bx, by) != (reina_x, reina_y) and (bx, by) not in bloqueos:
        bloqueos.add((bx, by))
        tablero[by - 1][bx - 1] = "X"


def marcar_movimientos():
    direcciones = [
        (1, 0), (-1, 0),  # Horizontal
        (0, 1), (0, -1),  # Vertical
        (1, 1), (-1, -1), # Diagonal principal
        (1, -1), (-1, 1)  # Diagonal secundaria
    ]
    for dx, dy in direcciones:
        x, y = reina_x, reina_y
        while True:
            x += dx
            y += dy
            if 1 <= x <= tamano and 1 <= y <= tamano:
                if tablero[y - 1][x - 1] == "X":
                    break
                if tablero[y - 1][x - 1] == ".":
                    tablero[y - 1][x - 1] = "*"
            else:
                break


marcar_movimientos()

for fila in reversed(tablero):
    print(" ".join(fila))
