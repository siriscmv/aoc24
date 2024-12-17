from re import match


def parser(input):
    regs, program = "\n".join(input).split("\n\n")
    registers = {"_OUT": [], "_IP": 0}

    for reg in regs.split("\n"):
        matches = match(r"Register ([A|B|C]): (\d+)", reg).groups()
        registers[matches[0]] = int(matches[1])

    prog_line = list(map(int, program.split(" ")[1].split(",")))

    program = []

    for i in range(0, len(prog_line), 2):
        program.append((prog_line[i], prog_line[i + 1]))

    return registers, program


def get_combo_op_val(registers, operand):
    if 0 <= operand <= 3:
        return operand

    if operand == 4:
        return registers["A"]

    if operand == 5:
        return registers["B"]

    if operand == 6:
        return registers["C"]

    if operand == 7:
        raise Exception("Invalid operand")


def divide(registers, operand):
    return int(registers["A"] / (2 ** get_combo_op_val(registers, operand)))


def adv(registers, operand):
    registers["A"] = divide(registers, operand)
    registers["_IP"] += 1


def bxl(registers, operand):
    registers["B"] ^= operand
    registers["_IP"] += 1


def bst(registers, operand):
    registers["B"] = get_combo_op_val(registers, operand) % 8
    registers["_IP"] += 1


def jnz(registers, operand):
    if registers["A"] != 0:
        registers["_IP"] = operand // 2
    else:
        registers["_IP"] += 1


def bxc(registers, operand):
    registers["B"] ^= registers["C"]
    registers["_IP"] += 1


def out(registers, operand):
    registers["_OUT"].append(get_combo_op_val(registers, operand) % 8)
    registers["_IP"] += 1


def bdv(registers, operand):
    registers["B"] = divide(registers, operand)
    registers["_IP"] += 1


def cdv(registers, operand):
    registers["C"] = divide(registers, operand)
    registers["_IP"] += 1


INSTRUCTIONS = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def solve(input):
    registers, program = input

    while registers["_IP"] < len(program):
        ins, operand = program[registers["_IP"]]
        INSTRUCTIONS[ins](registers, operand)

    return registers["_OUT"]


def p1(input):
    return ",".join(map(str, solve(input)))


def p2(input):
    registers, program = input
    original_program = []

    for ins, op in program:
        original_program.extend([ins, op])

    candidates = [0]
    for length in range(1, len(original_program) + 1):
        out = []

        for num in candidates:
            for offset in range(2**3):
                a = (2**3) * num + offset
                registers["_OUT"] = []
                registers["_IP"] = 0
                registers["A"] = a

                res = solve((registers, program))

                if res == original_program[-length:]:
                    out.append(a)

        candidates = out

    return min(candidates)
