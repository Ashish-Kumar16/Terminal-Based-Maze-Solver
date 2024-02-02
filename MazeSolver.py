import random

def generate_maze(size):
    # Initialize an empty maze with '◌' representing open spaces
    maze = [['◌' for _ in range(size)] for _ in range(size)]

    # Set start and end points
    start = (0, 0)
    end = (size - 1, size - 1)

    # Mark the start and end points in the maze
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    # Calculate the maximum allowed number of walls based on the 25% limit
    max_walls = int(size * size * 0.25)

    # Add walls randomly to the maze
    num_walls = 0
    while num_walls < max_walls:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        # Ensure that walls are not placed on start, end, or existing walls
        while (row, col) == start or (row, col) == end or maze[row][col] == '▓':
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        maze[row][col] = '▓'
        num_walls += 1

    return maze, start, end

def print_colored(char):
    # Define colors for different characters in the maze
    colors = {
        'S': '\033[0;33m',  # Red for Start
        'E': '\033[0;33m',  # Red for End
        '▓': '\033[91m',  # Red for Walls
        '◌': '\033[94m',  # Blue for Open Space
        '◍': '\033[92m',  # Green for Path
    }
    return f"{colors.get(char, char)}{char}\033[0m"

def print_maze_without_points(maze):
    # Display the maze without start and end points
    horizontal_line = "+---" * len(maze[0]) + "+"

    print(horizontal_line)

    for row in maze:
        for cell in row:
            print(f"| {print_colored(cell)} ", end="")
        print("|")
        print(horizontal_line)

def print_maze_with_points(maze, start, end):
    # Display the maze with start and end points marked
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    # print("\nStart and End Points:")
    print_maze_without_points(maze)

def find_path(maze, start, end):
    # Use Depth-First Search to find a path from start to end
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

def mark_path(maze, path, start, end):
    # Mark the path found by DFS in the maze
    for position in path:
        maze[position[0]][position[1]] = '◍'

def main():
    size = int(input("Enter the size of the maze (n x n): "))
    maze, start, end = generate_maze(size)
    print("\nGenerated Maze:")
    print_maze_without_points(maze)

    while True:
        choice = input("\nGenerated Maze: \n1. Print Path \n2. Generate Another Puzzle \n3. Exit\nEnter your choice (1/2/3): ")

        if choice == '1':
            path = find_path(maze, start, end)
            if path:
                mark_path(maze, path, start, end)
                print("\n Maze with path:")
                print_maze_with_points(maze, start, end)
            else:
                print("\nNo path exists.")
        
        elif choice == '2':
            maze, start, end = generate_maze(size)
            print("\nGenerated Maze:")
            print_maze_without_points(maze)
        elif choice == '3':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
