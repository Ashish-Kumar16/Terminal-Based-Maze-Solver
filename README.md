# Maze Generator and Solver

This Python script generates a maze of specified size and wall percentage, allowing you to find and visualize a path from the start (S) to the end (E) point.

## How to Use

1. **Run the Script:**
    - Make sure you have Python installed.
    - Execute the script using a Python interpreter.

    ```bash
    python maze_generator_solver.py
    ```

2. **Input Maze Size and Wall Percentage:**
    - Enter the size of the maze (n x n).
    - Input the wall percentage (percentage of blocked cells).

3. **Menu Options:**
    - **Print Path (1):** Find and print the path from start to end.
    - **Generate Another Puzzle (2):** Regenerate a new maze.
    - **Exit (3):** Terminate the program.

## Maze Legend

- **S:** Start point
- **E:** End point
- **▓:** Wall (blocked cell)
- **◌:** Open space
- **◍:** Path

## Example Output

```bash
Generated Maze:
+---+---+---+---+
| S | ◌ | ▓ | ◌ |
+---+---+---+---+
| ◌ | ▓ | ◌ | ◌ |
+---+---+---+---+
| ▓ | ◌ | ◌ | ◌ |
+---+---+---+---+
| ◌ | ◌ | ▓ | E |
+---+---+---+---+

Generated Maze:
1. Print Path
2. Generate Another Puzzle
3. Exit
Enter your choice (1/2/3):
```

## Dependencies

No external dependencies are required. The script uses only the built-in `random` module.

## Notes

- The maze is generated with a maximum of 25% walls based on the specified wall percentage.
- The path is found using a depth-first search algorithm.
- The path is marked with '◍' in the maze.
- You can regenerate the maze or exit the program as needed.
