def dfs(u, graph, visited=None):
    if visited is None:
        visited = set()

    visited.add(u)
    if u in graph:
        for v in graph[u]:
            if v not in visited:
                dfs(v, graph, visited)


if __name__ == '__main__':
    with open('input.txt') as input_file:
        graph = {}
        for line in input_file:
            u, inside = line.split(' bags contain ')
            if inside != 'no other bags.':
                insides = [' '.join(bag.split()[1:3]) for bag in inside[:-1].split(', ')]
                for v in insides:
                    graph.setdefault(v, []).append(u)
        visited = set()
        dfs('shiny gold', graph, visited)
        print(len(visited - {'shiny gold'}))
