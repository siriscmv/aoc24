def parser(input):
    return [list(map(int, line.split(" "))) for line in input]


def is_safe(report):
    sign = -1 if report[1] < report[0] else 1
    n = len(report)

    for i in range(0, n - 1):
        a, b = report[i], report[i + 1]
        if not (1 <= abs(b - a) <= 3) or (b - a) * sign < 0:
            return False

    return True


def possible_reports(report):
    return [report] + [report[:i] + report[i + 1 :] for i in range(len(report))]


def p1(input):
    return len([report for report in input if is_safe(report)])


def p2(input):
    return len(
        [
            report
            for report in input
            if any(is_safe(r) for r in possible_reports(report))
        ]
    )
