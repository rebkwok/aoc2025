def read_file(input_path):
    return input_path.read_text()


def read_file_as_lines(input_path):
    return read_file(input_path).strip().split("\n")


def read_file_as_grid(input_path, apply_fn=str):
    data = read_file_as_lines(input_path)
    return [[apply_fn(ch) for ch in line] for line in data]


def adjacent_grid_positions(r, c, grid):
    
    positions = [
        (r-1, c-1),
        (r-1, c),
        (r-1, c+1),
        (r, c-1),
        (r, c+1),
        (r+1, c-1),
        (r+1, c),
        (r+1, c+1)
    ]
    
    available_positions = []
    for position in positions:
        if any([p < 0 for p in position]):
            continue
        r, c = position
        if r >= len(grid):
            continue
        if c >= len(grid[0]):
            continue
        available_positions.append(position)
    
    return available_positions