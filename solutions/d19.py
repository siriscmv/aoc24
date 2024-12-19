def parser(input):
    patterns, designs = ("\n".join(input)).split("\n\n")

    patterns = list(patterns.split(", "))
    designs = list(designs.split("\n"))

    return patterns, designs


dp = {}


def ways(patterns, design):
    ans = 0

    if design in dp:
        return dp[design]

    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern) :]

            ans += 1 if not remaining else ways(patterns, remaining)

    dp[design] = ans
    return ans


def p1(input):
    patterns, designs = input

    return len([design for design in designs if ways(patterns, design)])


def p2(input):
    patterns, designs = input

    return sum([ways(patterns, design) for design in designs])
