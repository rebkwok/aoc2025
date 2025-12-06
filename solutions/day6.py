import math
from utils import read_file_as_lines, read_file_as_grid


operator_functions = {
        "+": sum,
        "*": math.prod
    }

def unroll_puzzles_1(data):

    data = [line.split() for line in data]

    puzzles = {}
    for line in data:
        for i, col in enumerate(line):
            try:
                col = int(col)
            except ValueError:
                col = col.strip().rstrip()
                col = operator_functions[col]

            puzzles.setdefault(i, []).append(col)
    
    return puzzles


def calculate_total(puzzles):
    total = 0
    for puzzle in puzzles:
        total += puzzle[-1](puzzle[0:-1])
    return total


def part1(input_path):
    data = read_file_as_lines(input_path)
    puzzles = unroll_puzzles_1(data)
    
    total = calculate_total(puzzles.values())
    print(total)


def unroll_puzzles_2(data):
    for line in data:
        line.reverse()

    puzzles = []
    current_puzzle = {"numbers": [], "func": None}

    for col_i in range(len(data[0])):
        columns = [line[col_i] for line in data]
        if set(columns) == {" "}:
            # new puzzle
            puzzles.append([*current_puzzle["numbers"], current_puzzle["func"]])
            current_puzzle = {"numbers": [], "func": None}
        else:
            number = int(''.join(columns[:-1]))
            current_puzzle["numbers"].append(number)
            if columns[-1] != " ":
                current_puzzle["func"] = operator_functions[columns[-1]]
    
    if current_puzzle["numbers"]:
        puzzles.append([*current_puzzle["numbers"], current_puzzle["func"]])

    return puzzles


def part2(input_path):
    data = read_file_as_grid(input_path, keep_whitespace=True)
    puzzles = unroll_puzzles_2(data)
    total = calculate_total(puzzles)
    print(total)
