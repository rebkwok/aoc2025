from utils import read_file_as_grid, adjacent_grid_positions


def identify_accessible(grid):
    accessible = []
    for row_i, row in enumerate(grid):
        for col_i, value in enumerate(row):
            if value == "@":
                adjacent = adjacent_grid_positions(row_i, col_i, grid)
                adjacent_rolls = sum(
                    1 for (r, c) in adjacent if grid[r][c] == "@"
                )
                if adjacent_rolls < 4:
                    accessible.append((row_i, col_i))
    return accessible


def part1(input_path):
    grid = read_file_as_grid(input_path)
    accessible = identify_accessible(grid)
    print(len(accessible))


def part2(input_path):
    grid = read_file_as_grid(input_path)

    accessible = identify_accessible(grid)
    removed = 0

    while len(accessible) > 0:
        for pos in accessible:
            grid[pos[0]][pos[1]] = "x"
        removed += len(accessible)
        accessible = identify_accessible(grid)
    
    print(removed)