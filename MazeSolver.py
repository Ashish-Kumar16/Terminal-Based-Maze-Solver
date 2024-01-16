def print_maze(maze):
    for row in maze:
        print(" ".join(map(print_colored, row)))