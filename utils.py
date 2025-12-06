def read_file(input_path):
    return input_path.read_text()


def read_file_as_lines(input_path, keep_whitespace=False):
    if keep_whitespace:
        return read_file(input_path).split("\n")
    return read_file(input_path).strip().split("\n")
    

def read_file_as_grid(input_path, apply_fn=str, keep_whitespace=False):
    data = read_file_as_lines(input_path, keep_whitespace=keep_whitespace)
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