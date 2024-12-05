from collections import defaultdict


def parser(input):
    rules, updates = "\n".join(input).split("\n\n")

    rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

    rules_map = defaultdict(lambda: ([], []))

    for a, b in rules:
        rules_map[b][0].append(a)
        rules_map[a][1].append(b)

    return rules_map, updates


def is_correct(rules_map, update):
    for i, a in enumerate(update):
        for j, b in enumerate(update):
            if j < i:
                if a not in rules_map[b][1]:
                    return False
            elif j > i:
                if a not in rules_map[b][0]:
                    return False
    return True


def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]


def rectify(rules_map, update):
    update = set(update)
    graph = {a: [] for a in update}

    for a in update:
        for b in rules_map[a][1]:
            if b in update:
                graph[b].append(a)

    return topological_sort(graph)


def p1(input):
    rules_map, updates = input

    return sum(
        [
            update[len(update) // 2]
            for update in updates
            if is_correct(rules_map, update)
        ]
    )


def p2(input):
    rules_map, updates = input

    return sum(
        [
            rectify(rules_map, update)[len(update) // 2]
            for update in updates
            if not is_correct(rules_map, update)
        ]
    )
