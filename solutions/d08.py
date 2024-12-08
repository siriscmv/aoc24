from collections import defaultdict


def parser(input):
    antennas = defaultdict(list)
    matrix = [list(line) for line in input]

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell != ".":
                antennas[cell].append((i, j))

    return antennas, matrix


def count(input, p2=False):
    antennas, matrix = input
    m, n = len(matrix), len(matrix[0])
    antinodes = set()

    for freq in antennas:
        curr = antennas[freq]

        for i, (p, q) in enumerate(curr):
            for j, (r, s) in enumerate(curr):
                if i == j:
                    continue

                if p2:
                    antinodes.add((p, q))
                ix = 0

                while True:
                    ix += 1
                    path = ((p - r) * ix, (q - s) * ix)
                    antinode = (p + path[0], q + path[1])
                    if 0 <= antinode[0] < m and 0 <= antinode[1] < n:
                        antinodes.add(antinode)
                    else:
                        break

                    if not p2:
                        break

    return len(antinodes)


def p1(input):
    return count(input)


def p2(input):
    return count(input, p2=True)
