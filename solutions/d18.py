from collections import deque


def parser(input):
    coordinates = []

    for line in input:
        y, x = map(int, line.split(","))
        coordinates.append((x, y))

    return coordinates


def bfs(matrix):
    queue = deque([(0, 0, 0)])
    visited = {}
    ans = float("inf")
    m, n = len(matrix), len(matrix[0])

    while queue:
        x, y, l = queue.popleft()

        if (x, y) in visited and visited[(x, y)] <= l:
            continue

        visited[(x, y)] = l

        if x == m - 1 and y == n - 1:
            ans = min(ans, l)
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 0:
                queue.append((nx, ny, l + 1))

    return ans


def fill(coords, count, size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for x, y in coords[:count]:
        matrix[x][y] = 1

    return matrix


def p1(input):
    return bfs(fill(input, count=1024, size=71))


def p2(input):
    for i in range(1, len(input) + 1):
        if bfs(fill(input, count=i, size=71)) == float("inf"):
            y, x = input[i - 1]
            return f"{x},{y}"
