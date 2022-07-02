# поле сапера
n, m, mine = (int(i) for i in input().split())
field = [[0] * n for i in range(m)]

for i in range(mine):
    row, col = (int(i) - 1 for i in input().split())
    field[row][col] = -1

for i in range(n):
    for j in range(m):
        if field[i][j] == -1:

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = di + i
                    aj = dj + j

                    if field[ai][aj] != -1 and 0 <= ai < n and 0 <= aj < m:
                        field[ai][aj] += 1

for i in range(n):
    for j in range(m):
        print('\t', field[i][j], end = '')
    print('\n', '\n')
