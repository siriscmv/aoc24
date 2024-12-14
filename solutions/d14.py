from re import search
from functools import reduce
from operator import mul


X, Y = 101, 103


def parser(input):
    return [
        list(map(int, search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()))
        for line in input
    ]


def simulate(robot, time):
    x, y, vx, vy = robot
    fx, fy = (x + time * vx) % X, (y + time * vy) % Y

    return (fx, fy)


def quad(x, y):
    if x < X // 2:
        if y < Y // 2:
            return 0
        elif y > Y // 2:
            return 1
    elif x > X // 2:
        if y < Y // 2:
            return 2
        elif y > Y // 2:
            return 3

    return -1


def display(robots):
    for j in range(Y):
        for i in range(X):
            if (i, j) in robots:
                print(".", end="")
            else:
                print(" ", end="")
        print()


def p1(input):
    robots = [0] * 4

    for robot in input:
        q = quad(*simulate(robot, time=100))
        if q != -1:
            robots[q] += 1

    return reduce(mul, robots)


def p2(input):
    i = 0

    while True:
        i += 1
        positions = [simulate(robot, time=i) for robot in input]

        if len(positions) == len(set(positions)):
            display(positions)
            return i
