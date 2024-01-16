import random

def generate_maze(size, wall_percentage):
    maze = [['◌' for _ in range(size)] for _ in range(size)]

    # Set start and end points
    start = (0, 0)
    end = (size - 1, size - 1)

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    # Calculate the maximum allowed number of walls based on the 25% limit
    max_walls = int(size * size * 0.25)

    # Add walls
    num_walls = 0
    while num_walls < max_walls:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        while (row, col) == start or (row, col) == end or maze[row][col] == '▓':
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        maze[row][col] = '▓'
        num_walls += 1

    return maze, start, end