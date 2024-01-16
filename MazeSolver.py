def print_colored(char):
    colors = {
        'S': '\033[91m',  # Red for Start
        'E': '\033[91m',  # Red for End
        '▓': '\033[91m',  # Red for Walls
        '◌': '\033[94m',  # Blue for Open Space
        '◍': '\033[92m',  # Green for Path
    }
    return f"{colors.get(char, char)}{char}\033[0m"