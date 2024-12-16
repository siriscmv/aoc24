def parser(input):
    state, moves = "\n".join(input).split("\n\n")

    moves = [ch for ch in moves if ch != "\n"]
    state = [list(line) for line in state.split("\n")]

    return state, moves


def next_coord(i, j, m):
    if m == "^":
        return i - 1, j
    elif m == ">":
        return i, j + 1
    elif m == "v":
        return i + 1, j
    elif m == "<":
        return i, j - 1


def out_of_bounds(state, i, j):
    return i < 0 or i >= len(state) or j < 0 or j >= len(state[0])


def can_move(state, i, j, m):
    x, y = next_coord(i, j, m)

    if out_of_bounds(state, x, y) or state[x][y] == "#":
        return False

    if state[x][y] in "[]":
        if m in "^v":
            other_half_y = y + 1 if state[x][y] == "[" else y - 1
            return can_move(state, x, y, m) and can_move(state, x, other_half_y, m)
        else:
            return can_move(state, x, y, m)

    return state[x][y] == "." or can_move(state, x, y, m)


def move(state, i, j, m, first=False):
    x, y = next_coord(i, j, m)

    if out_of_bounds(state, x, y):
        return i, j

    if state[x][y] == "#":
        return i, j
    elif state[x][y] == ".":
        state[x][y], state[i][j] = state[i][j], state[x][y]
        return x, y

    elif state[x][y] in "O[]":
        if (
            not can_move(state, x, y, m)
            or (state[x][y] == "[" and not can_move(state, x, y + 1, m))
            or (state[x][y] == "]" and not can_move(state, x, y - 1, m))
        ):
            return i, j

        prev = state[x][y]
        move(state, x, y, m)
        if m in "v^":
            if prev == "[":
                move(state, x, y + 1, m)
            if prev == "]":
                move(state, x, y - 1, m)

        state[x][y] = "@" if first else state[i][j]

        if first:
            state[i][j] = "."

        if m in "v^":
            if prev == "[":
                state[x][y + 1] = "."
            if prev == "]":
                state[x][y - 1] = "."

        return x, y


def score(state):
    ans = 0

    for i, line in enumerate(state):
        for j, ch in enumerate(line):
            if ch in "O[":
                ans += i * 100 + j

    return ans


def get_robot(state):
    for i, line in enumerate(state):
        for j, ch in enumerate(line):
            if ch == "@":
                return i, j


def scale_up(input):
    state, moves = input
    for i, row in enumerate(state):
        new_row = []
        for j, ch in enumerate(row):
            if ch == "#":
                new_row.extend(["#", "#"])
            elif ch == "O":
                new_row.extend(["[", "]"])
            elif ch == ".":
                new_row.extend([".", "."])
            elif ch == "@":
                new_row.extend(["@", "."])

        state[i] = new_row

    return state, moves


def solve(input):
    state, moves = input

    i, j = get_robot(state)

    for m in moves:
        i, j = move(state, i, j, m, first=True)

    return score(state)


def p1(input):
    return solve(input)


def p2(input):
    return solve(scale_up(input))
