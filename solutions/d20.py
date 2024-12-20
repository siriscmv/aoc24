from collections import deque


def parser(input):
    matrix = [list(line) for line in input]
    start, end = None, None
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "#":
                matrix[i][j] = 0
            else:
                if cell == "S":
                    start = (i, j)
                elif cell == "E":
                    end = (i, j)
                matrix[i][j] = 1
    return matrix, start, end


def bfs(matrix, start, end):
    queue = deque([(start[0], start[1], 0)])
    seen = {}
    m, n = len(matrix), len(matrix[0])

    while queue:
        i, j, time = queue.popleft()

        if seen.get((i, j), float("inf")) <= time:
            continue

        seen[(i, j)] = time

        if (i, j) == end:
            continue

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj]:
                queue.append((ni, nj, time + 1))

    return seen


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reachable(curr, threshold):
    for i in range(curr[0] - threshold, curr[0] + threshold + 1):
        for j in range(curr[1] - threshold, curr[1] + threshold + 1):
            d = dist(curr, (i, j))

            if d <= threshold:
                yield (i, j, d)


def solve(input, threshold, min_time=100):
    matrix, start, end = input
    seen = bfs(matrix, start, end)
    ans = 0

    for i, j in seen:
        for p, q, d in reachable((i, j), threshold):
            if (p, q) not in seen:
                continue

            new_time = seen[(i, j)] + d + seen[end] - seen[(p, q)]
            if seen[end] - new_time >= min_time:
                ans += 1

    return ans


def p1(input):
    return solve(input, 2)


def p2(input):
    return solve(input, 20)
