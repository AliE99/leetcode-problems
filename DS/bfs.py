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


visited: list[str] = []
queue: list[str] = []


def bfs(node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


bfs("1")

print(", ".join(visited))
