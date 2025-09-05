# Juan David Martinez Mira
# Formato de entrada: primero tamaño del tablero (n), luego coordenadas de la reina (fila columna) separadas por espacio.
# 1 solo Bloqueo

import random


n = int(input("Tamaño del tablero: "))
fila_reina, col_reina = map(int, input("Coordenadas de la reina (fila columna, separadas por espacio): ").split())


fila_bloqueo = random.randint(1, n)
col_bloqueo = random.randint(1, n)
movs = []


direcciones = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]


for df, dc in direcciones:
    f = fila_reina + df
    c = col_reina + dc
    while 1 <= f <= n and 1 <= c <= n:
        if f == fila_bloqueo and c == col_bloqueo:
            break
        movs.append((f, c))
        f += df
        c += dc


for f in range(1, n + 1):
    linea = ""
    for c in range(1, n + 1):
        if f == fila_reina and c == col_reina:
            linea += " R "
        elif f == fila_bloqueo and c == col_bloqueo:
            linea += " X "
        elif (f, c) in movs:
            linea += " * "
        else:
            linea += " . "
    print(linea)


print("\nMovimientos posibles:", len(movs))
print("Bloqueo en:", fila_bloqueo, col_bloqueo)
