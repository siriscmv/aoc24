from collections import Counter


def parser(input):
    left, right = [], []

    for line in input:
        l, r = map(int, line.split("   "))
        left.append(l)
        right.append(r)

    return left, right


def p1(input):
    left, right = input
    n = len(left)

    left.sort()
    right.sort()

    return sum([abs(left[i] - right[i]) for i in range(n)])


def p2(input):
    left, right = input
    counts = Counter(right)

    return sum([num * counts[num] for num in left])
