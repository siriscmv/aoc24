def parser(input):
    wires_list, gates_list = map(
        lambda x: x.split("\n"), ("\n".join(input)).split("\n\n")
    )

    wires, gates = {}, {}

    for w in wires_list:
        wire, val = w.split(": ")
        wires[wire] = int(val)

    for gate in gates_list:
        out = gate.split(" -> ")
        a, b, c = out[0].split(" ")

        gates[out[1]] = (a, b, c, out[1])

    return wires, gates


def output(wires, gates, gate):
    a, op, b, c = gate

    if gate in wires:
        return wires[gate]

    for val in [a, b]:
        if val not in wires:
            output(wires, gates, gates[val])

    if op == "AND":
        out = wires[a] & wires[b]
    elif op == "OR":
        out = wires[a] | wires[b]
    elif op == "XOR":
        out = wires[a] ^ wires[b]

    wires[c] = out
    return out


def solve(input):
    wires, gates = input
    num = []

    for gate in gates:
        out = output(wires, gates, gates[gate])

        if gate.startswith("z"):
            num.append((gate, out))

    num.sort(reverse=True)
    return "".join([str(n[1]) for n in num])


def make_wire(char, num):
    return char + str(num).rjust(2, "0")


def verify_z(wire, num, gates):
    if wire not in gates:
        return False
    op, x, y = gates[wire]
    if op != "XOR":
        return False
    if num == 0:
        return sorted([x, y]) == ["x00", "y00"]
    return (
        verify_intermediate_xor(x, num, gates)
        and verify_carry_bit(y, num, gates)
        or verify_intermediate_xor(y, num, gates)
        and verify_carry_bit(x, num, gates)
    )


def verify_intermediate_xor(wire, num, gates):
    if wire not in gates:
        return False
    op, x, y = gates[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]


def verify_carry_bit(wire, num, gates):
    if wire not in gates:
        return False
    op, x, y = gates[wire]
    if num == 1:
        if op != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR":
        return False
    return (
        verify_direct_carry(x, num - 1, gates)
        and verify_recarry(y, num - 1, gates)
        or verify_direct_carry(y, num - 1, gates)
        and verify_recarry(x, num - 1, gates)
    )


def verify_direct_carry(wire, num, gates):
    if wire not in gates:
        return False
    op, x, y = gates[wire]
    if op != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]


def verify_recarry(wire, num, gates):
    if wire not in gates:
        return False
    op, x, y = gates[wire]
    if op != "AND":
        return False
    return (
        verify_intermediate_xor(x, num, gates)
        and verify_carry_bit(y, num, gates)
        or verify_intermediate_xor(y, num, gates)
        and verify_carry_bit(x, num, gates)
    )


def verify(num, gates):
    return verify_z(make_wire("z", num), num, gates)


def progress(gates):
    i = 0

    while True:
        if not verify(i, gates):
            break
        i += 1

    return i


def p1(input):
    return int(solve(input), 2)


# https://github.com/hyperneutrino/advent-of-code/blob/main/2024/day24p2.py
def p2(input):
    _, gates = input

    for gate in gates:
        val = gates[gate]
        gates[gate] = (val[1], val[0], val[2])

    swaps = []

    for _ in range(4):
        baseline = progress(gates)
        for x in gates:
            for y in gates:
                if x == y:
                    continue
                gates[x], gates[y] = gates[y], gates[x]
                if progress(gates) > baseline:
                    break
                gates[x], gates[y] = gates[y], gates[x]
            else:
                continue
            break
        swaps += [x, y]

    return ",".join(sorted(swaps))
