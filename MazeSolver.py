def mark_path(maze, path):
    for position in path:
        maze[position[0]][position[1]] = '◍'