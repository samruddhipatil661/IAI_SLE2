from collections import deque
from maze import get_neighbors

def get_neighbors(maze, cell):
    """Return valid 4-directional open-cell neighbors."""
    rows, cols = len(maze), len(maze[0])
    r, c = cell
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
            yield (nr, nc)


def bfs(maze, start, goal):
    """Breadth-First Search. Returns path, path length, and nodes expanded."""
    queue = deque([start])
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in get_neighbors(maze, current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    if goal not in parent:
        return [], 0, nodes_expanded

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path, len(path) - 1, nodes_expanded
