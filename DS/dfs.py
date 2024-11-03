graph = {
    "1": ["4", "2"],
    "4": ["1", "3"],
    "3": ["4", "10", "9", "2"],
    "10": ["3"],
    "9": ["3"],
    "2": ["1", "3", "8", "7", "5"],
    "8": ["2", "7", "5"],
    "7": ["2", "8", "5"],
    "5": ["2", "8", "7", "6"],
    "6": ["5"],
}


visited = set()


def dfs(visited: set, graph, node):
    if node in visited:
        return
    visited.add(node)
    print(node, end=" ,")
    for neighbor in graph[node]:
        dfs(visited, graph, neighbor)


dfs(visited, graph, "1")
