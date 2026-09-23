from bfs import bfs
from dfs import dfs
from maze import create_sample_maze
from time import perf_counter


def display_result(name, result):
    path, length, nodes = result
    print(f"\n{name}")
    print("-" * 30)
    print("Path:", path)
    print("Path length:", length)
    print("Nodes expanded:", nodes)


def main():
    maze = create_sample_maze()
    start = (0, 0)
    goal = (7, 7)

    start_time = perf_counter()
    bfs_result = bfs(maze, start, goal)
    bfs_time = (perf_counter() - start_time) * 1000

    start_time = perf_counter()
    dfs_result = dfs(maze, start, goal, depth_limit=200)
    dfs_time = (perf_counter() - start_time) * 1000

    print("BFS vs DFS Maze Pathfinding")
    print("=" * 40)

    display_result("BFS", bfs_result)
    print(f"Execution time: {bfs_time:.4f} ms")

    display_result("DFS (depth limit = 200)", dfs_result)
    print(f"Execution time: {dfs_time:.4f} ms")


if __name__ == "__main__":
    main()
