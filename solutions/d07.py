def parser(input):
    parsed = []

    for line in input:
        test_val, vals = line.split(": ")
        vals = list(map(int, vals.split(" ")))
        test_val = int(test_val)
        parsed.append((test_val, vals))

    return parsed


def concat(a, b):
    return int(str(a) + str(b))


def is_valid(test_val, vals, p2=False):
    if len(vals) == 0:
        return test_val == 0
    elif len(vals) == 1:
        return test_val == vals[0]

    a, b = vals[0], vals[1]

    return (
        is_valid(test_val, [a * b] + vals[2:], p2)
        or is_valid(test_val, [a + b] + vals[2:], p2)
        or (p2 and is_valid(test_val, [concat(a, b)] + vals[2:], p2))
    )


def p1(input):
    return sum(test_val for test_val, vals in input if is_valid(test_val, vals))


def p2(input):
    return sum(
        test_val for test_val, vals in input if is_valid(test_val, vals, p2=True)
    )
