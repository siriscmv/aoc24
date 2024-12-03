from re import findall, match


def parser(input):
    return "\n".join(input)


MUL_REGEX = r"mul\((\d+),(\d+)\)"
INS_REGEX = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"


def p1(input):
    return sum([int(a) * int(b) for a, b in findall(MUL_REGEX, input)])


def p2(input):
    do = True
    ans = 0

    for ins in findall(INS_REGEX, input):
        if ins == "do()":
            do = True
        elif ins == "don't()":
            do = False
        elif do:
            mul = match(MUL_REGEX, ins)
            ans += int(mul.group(1)) * int(mul.group(2))

    return ans
