from collections import deque


def parser(input):
    matrix = [list(line) for line in input]

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                end = (i, j)

    matrix[start[0]][start[1]] = "."
    return matrix, start, end


DIRS = [((0, 1), 1), ((0, -1), 3), ((1, 0), 2), ((-1, 0), 0)]


def bfs(matrix, start, end, best=None):
    m, n = len(matrix), len(matrix[0])
    queue = deque()
    visited = {}

    queue.append((start, 0, 1, [start]))  # (current position, score, direction, path)
    visited[(start, 1)] = 0  # Mark ((position, dir) => score) as visited

    ans = float("inf")
    tiles = set()

    while queue:
        curr, score, dir, path = queue.popleft()

        if curr == end:
            if best:
                if score == best:
                    tiles.update(set(path))
            else:
                ans = min(ans, score)

            continue

        for d, rot in DIRS:
            new = (curr[0] + d[0], curr[1] + d[1])
            if (
                new[0] < 0
                or new[0] >= m
                or new[1] < 0
                or new[1] >= n
                or matrix[new[0]][new[1]] == "#"
                or ((new, rot) in visited and visited[(new, rot)] <= score)
            ):
                continue

            diff = min(abs(dir - rot), 4 - abs(dir - rot))
            new_score = score + 1 + (1000 * diff)

            queue.append((new, new_score, rot, path + [new]))
            visited[(new, rot)] = new_score

    return len(tiles) if best else ans


def p1(input):
    matrix, start, end = input

    return bfs(
        matrix,
        start,
        end,
    )


def p2(input):
    matrix, start, end = input

    return bfs(matrix, start, end, best=p1(input))
