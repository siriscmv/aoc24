from collections import defaultdict


def parser(input):
    return [int(line) for line in input]


def mix(a, b):
    return a ^ b


def prune(num):
    return num % 16777216


def secret(num):
    a = prune(mix(num * 64, num))
    b = prune(mix(a // 32, a))
    c = prune(mix(b * 2048, b))

    return c


def n_secrets(num, n):
    output = [num]

    for _ in range(n):
        res = secret(num)
        output.append(res)
        num = res

    return output


def diff(input):
    output = []
    n = len(input)

    for i in range(1, n):
        output.append(input[i] - input[i - 1])

    return output


def p1(input):
    return sum([n_secrets(num, 2000)[-1] for num in input])


def p2(input):
    profits = defaultdict(int)

    for num in input:
        seen = set()
        secrets = [n % 10 for n in n_secrets(num, 2000)]
        differences = diff(secrets)

        for i in range(len(differences) - 3):
            key = tuple(differences[i : i + 4])

            if key not in seen:
                seen.add(key)
                profits[key] += secrets[i + 4]

    return max(profits.values())
