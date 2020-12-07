def dfs(u, graph, visited):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v, graph, visited)


def count_dfs(u, graph, visited=None, depth=0):
    if visited is None:
        visited = set()

    visited.add(u)
    res = 1
    for v, count in graph[u]:
        if v not in visited:
            x = count_dfs(v, graph, visited, depth + 1)
            res += int(count) * x
    visited.remove(u)
    return res


def parse_rule(rule):
    rule = rule[:-1]
    rule_bag, insides = rule.split(' bags contain ')
    if insides == 'no other bags.':
        insides = []
    else:
        insides = insides[:-1].split(', ')
        insides = [tuple(bag.split()[:-1]) for bag in insides]
    return rule_bag, insides


def base_graph(rules):
    bags = set()
    for bag, insides in rules:
        bags.add(bag)
        for count, spec, color in insides:
            other_bag = f'{spec} {color}'
            bags.add(other_bag)
    return {bag: set() for bag in bags}


def inward_graph(rules):
    graph = base_graph(rules)
    for bag, insides in rules:
        for count, spec, color in insides:
            other_bag = f'{spec} {color}'
            graph[other_bag].add(bag)
    return graph


def outward_graph(rules):
    graph = base_graph(rules)
    for bag, insides in rules:
        for count, spec, color in insides:
            other_bag = f'{spec} {color}'
            graph[bag].add((other_bag, count))
    return graph


if __name__ == '__main__':
    with open('input.txt') as input_file:
        rules = [parse_rule(line) for line in input_file]
        graph = outward_graph(rules)
        print(count_dfs('shiny gold', graph) - 1)
