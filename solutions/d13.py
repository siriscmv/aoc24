from re import search


def parser(input):
    machines = [machine for machine in "\n".join(input).split("\n\n")]
    output = []

    for machine in machines:
        p, q = search(r"Button A: X\+(\d+), Y\+(\d+)", machine).groups()
        r, s = search(r"Button B: X\+(\d+), Y\+(\d+)", machine).groups()
        x, y = search(r"Prize: X=(\d+), Y=(\d+)", machine).groups()

        output.append([int(p), int(r), int(q), int(s), int(x), int(y)])

    return output


def solve_linear_system(a, b, c, d, e, f):
    """
    Solves:
    a*x + b*y = e
    c*x + d*y = f
    """
    # Determinant of the coefficient matrix
    det = a * d - b * c

    if det == 0:
        raise ValueError("The system has no unique solution (determinant is zero).")

    # Using Cramer's Rule to find x and y
    x = (e * d - b * f) / det
    y = (a * f - e * c) / det

    return x, y


def solve(input, p2=False):
    ans = 0

    for machine in input:
        if p2:
            machine[-1] += 10000000000000
            machine[-2] += 10000000000000

        x, y = solve_linear_system(*machine)
        if int(x) == x and int(y) == y:
            ans += x * 3 + y

    return int(ans)


def p1(input):
    return solve(input)


def p2(input):
    return solve(input, p2=True)
