def parser(input):
    matrix = [list(line) for line in input]

    for i, line in enumerate(matrix):
        for j, cell in enumerate(line):
            if cell == "^":
                return matrix, (i, j)


def move(matrix, curr, i, j):
    m, n = len(matrix), len(matrix[0])

    if curr == 0:
        if i - 1 >= 0 and matrix[i - 1][j] == "#":
            curr = 1
            j += 1
        else:
            i -= 1
    elif curr == 1:
        if j + 1 < n and matrix[i][j + 1] == "#":
            curr = 2
            i += 1
        else:
            j += 1
    elif curr == 2:
        if i + 1 < m and matrix[i + 1][j] == "#":
            curr = 3
            j -= 1
        else:
            i += 1
    elif curr == 3:
        if j - 1 >= 0 and matrix[i][j - 1] == "#":
            curr = 0
            i -= 1
        else:
            j -= 1

    return curr, i, j


def simulate(input, p2=False):
    matrix, (x, y) = input
    seen = {}
    curr = 0
    i, j = x, y
    m, n = len(matrix), len(matrix[0])

    while 0 <= i < m and 0 <= j < n:
        if p2:
            if (i, j, curr) in seen:
                return True
            seen[(i, j, curr)] = True
        else:
            matrix[i][j] = "X"

        prev = (i, j)

        for itr in range(4):
            if itr == 3 and p2:
                return True
            curr, i, j = move(matrix, curr, i, j)
            if not (0 <= i < m and 0 <= j < n) and p2:
                return False
            if matrix[i][j] != "#":
                break

            i, j = prev


def p1(input):
    simulate(input)
    return sum(1 for line in input[0] for cell in line if cell == "X")


def p2(input):
    matrix, (x, y) = input
    ans = 0

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell != ".":
                continue

            matrix[i][j] = "#"
            if simulate((matrix, (x, y)), p2=True):
                ans += 1
            matrix[i][j] = "."

    return ans
