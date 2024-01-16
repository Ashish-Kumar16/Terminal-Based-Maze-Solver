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