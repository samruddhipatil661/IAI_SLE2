def get_neighbors(maze, cell):
    """Return valid 4-directional open-cell neighbors."""
    rows, cols = len(maze), len(maze[0])
    r, c = cell
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
            yield (nr, nc)


def create_sample_maze():
    """Create a small sample maze. 0 = open, 1 = wall."""
    return [
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
