def parser(input):
    return [list(line) for line in input]


DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
#      L         U       R        D

CONTINUATION_MAP = {
    0: [1, 3],  # L -> U, D
    1: [0, 2],  # U -> L, R
}


def sides(matrix, i, j):
    m, n = len(matrix), len(matrix[0])
    ans = [True] * 4

    for ix, (dx, dy) in enumerate(DIRS):
        x = i + dx
        y = j + dy

        if 0 <= x < m and 0 <= y < n and matrix[x][y] == matrix[i][j]:
            ans[ix] = False

    return ans


def flood(matrix, i, j, type, visited, p2):
    m, n = len(matrix), len(matrix[0])
    area = 1
    perimeter = 4

    visited.add((i, j))

    for ix, (dx, dy) in enumerate(DIRS):
        x = i + dx
        y = j + dy

        if 0 <= x < m and 0 <= y < n and matrix[x][y] == type:
            perimeter -= 1

            if p2 and ix in CONTINUATION_MAP:
                prev = sides(matrix, x, y)
                curr = sides(matrix, i, j)

                for q in CONTINUATION_MAP[ix]:
                    if prev[q] and curr[q]:
                        perimeter -= 1

            if (x, y) not in visited:
                res = flood(matrix, x, y, type, visited, p2)
                area += res[0]
                perimeter += res[1]

    return (area, perimeter)


def cost(input, p2=False):
    ans = 0
    visited = set()

    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            if (i, j) not in visited:
                v = set()
                res = flood(input, i, j, cell, v, p2)
                visited.update(v)
                ans += res[0] * res[1]

    return ans


def p1(input):
    return cost(input)


def p2(input):
    return cost(input, p2=True)
