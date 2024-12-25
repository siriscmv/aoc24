def parser(input):
    locks, keys = [], []

    for matrix in "\n".join(input).split("\n\n"):
        matrix = [list(row) for row in matrix.split("\n")]

        if all([cell == "#" for cell in matrix[0]]):
            locks.append(matrix)
        elif all([cell == "#" for cell in matrix[-1]]):
            keys.append(matrix)

    return locks, keys


def get_cols(matrix):
    cols = [-1] * len(matrix[0])

    for row in matrix:
        for j, cell in enumerate(row):
            if cell == "#":
                cols[j] += 1

    return cols


def is_match(a, b):
    combined = [aa + bb for aa, bb in zip(a, b)]

    return all([c <= 5 for c in combined])


def p1(input):
    locks, keys = input
    ans = 0

    for lock in locks:
        l = get_cols(lock)
        for key in keys:
            k = get_cols(key)
            if is_match(l, k):
                ans += 1

    return ans
