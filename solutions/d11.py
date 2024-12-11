from functools import cache


def parser(input):
    return list(map(int, "\n".join(input).split(" ")))


@cache
def blink(num, blinks):
    if not blinks:
        return 1

    if num == 0:
        return blink(1, blinks - 1)
    elif len(str(num)) % 2 == 0:
        n = str(num)
        a, b = int(n[: len(n) // 2]), int(n[len(n) // 2 :])
        return blink(a, blinks - 1) + blink(b, blinks - 1)
    else:
        return blink(num * 2024, blinks - 1)


def length(input, blinks):
    return sum([blink(num, blinks) for num in input])


def p1(input):
    return length(input, 25)


def p2(input):
    return length(input, 75)
