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



def print_colored(char):
    colors = {
        'S': '\033[91m',  # Red for Start
        'E': '\033[91m',  # Red for End
        '▓': '\033[91m',  # Red for Walls
        '◌': '\033[94m',  # Blue for Open Space
        '◍': '\033[92m',  # Green for Path
    }
    return f"{colors.get(char, char)}{char}\033[0m"

def print_maze(maze):
    for row in maze:
        print(" ".join(map(print_colored, row)))
def find_path(maze, start, end):
    visited = set()

    def dfs(current):
        if current == end:
            return [end]
        visited.add(current)

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (current[0] + move[0], current[1] + move[1])
            if (
                0 <= new_pos[0] < len(maze)
                and 0 <= new_pos[1] < len(maze[0])
                and new_pos not in visited
                and maze[new_pos[0]][new_pos[1]] != '▓'
            ):
                path = dfs(new_pos)
                if path:
                    return [current] + path
        return []

    path = dfs(start)
    return path
def mark_path(maze, path):
    for position in path:
        maze[position[0]][position[1]] = '◍'
