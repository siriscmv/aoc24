def parser(input):
    return [list(map(int, line)) for line in input]


def dfs(matrix, i, j, visited, goals, p2):
    m, n = len(matrix), len(matrix[0])
    if matrix[i][j] == 9 and (p2 or (i, j) not in goals):
        goals.add((i, j))
        return 1

    visited.add((i, j))
    ans = 0

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        p, q = i + dx, j + dy
        if (
            0 <= p < m
            and 0 <= q < n
            and (p, q) not in visited
            and matrix[p][q] - matrix[i][j] == 1
        ):
            ans += dfs(matrix, p, q, visited, goals, p2)

    visited.remove((i, j))
    return ans


def score(input, p2=False):
    ans = 0

    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            if not cell:
                ans += dfs(input, i, j, set(), set(), p2)

    return ans


def p1(input):
    return score(input)


def p2(input):
    return score(input, p2=True)
