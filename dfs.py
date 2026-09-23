from maze import get_neighbors

def dfs(maze, start, goal, depth_limit=200):
    """Depth-Limited DFS. Returns path, path length, and nodes expanded."""
    visited = set()
    nodes_expanded = 0

    def search(current, path, depth):
        nonlocal nodes_expanded
        nodes_expanded += 1

        if current == goal:
            return path

        if depth >= depth_limit:
            return None

        visited.add(current)

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                result = search(neighbor, path + [neighbor], depth + 1)
                if result is not None:
                    return result

        return None

    result = search(start, [start], 0)

    if result is None:
        return [], 0, nodes_expanded

    return result, len(result) - 1, nodes_expanded
