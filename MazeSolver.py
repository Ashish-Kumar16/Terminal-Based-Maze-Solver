def main():
    size = int(input("Enter the size of the maze: "))
    wall_percentage = int(input("Enter the wall percentage: "))

    maze, start, end = generate_maze(size, wall_percentage)

    while True:
        print("\nGenerated Maze:")
        print_maze(maze)

        choice = input("\nOptions: 1. Print Path 2. Generate Another Puzzle 3. Exit\nEnter your choice: ")

        if choice == '1':
            path = find_path(maze, start, end)
            if path:
                mark_path(maze, path)
                print("\nPath:")
                print_maze(maze)
            else:
                print("\nNo path exists.")
        elif choice == '2':
            maze, start, end = generate_maze(size, wall_percentage)
        elif choice == '3':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()