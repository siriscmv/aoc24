from collections import defaultdict, deque


def parser(input):
    graph = defaultdict(set)

    for line in input:
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)

    return graph


def dfs_direct(graph, node, visited, component):
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if all(node in graph[neighbor] for node in component):
                dfs_direct(graph, neighbor, visited, component)


def directly_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs_direct(graph, node, visited, component)
            components.append(component)

    return components


def p1(input):
    seen = set()

    for node in input:
        if not node.startswith("t"):
            continue

        for a in input[node]:
            for b in input[a]:
                if b in input[node]:
                    seen.add(tuple(sorted([node, a, b])))

    return len(seen)


def p2(input):
    components = directly_connected_components(input)
    longest = sorted(components, key=len)[-1]

    return ",".join(sorted(longest))
