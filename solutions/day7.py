from utils import read_file_as_grid



def walk(row_i, col_i, grid, splits=[], nodes=[]):
    nodes.append((row_i, col_i))
    if row_i + 1 == len(grid):
        # at the end
        return
    if (row_i + 1, col_i) in splits:
        # already been here
        return
    
    if grid[row_i + 1][col_i] == "^":
        splits.append((row_i + 1, col_i))
        new_positions = []
        if col_i > 0:
            new_positions.append((row_i + 1, col_i - 1))
        if col_i < (len(grid[0]) - 1):
            new_positions.append((row_i + 1, col_i + 1))
    else:
        new_positions = [(row_i + 1, col_i)]

    for position in new_positions:
        walk(position[0], position[1], grid, splits, nodes)

    return splits, nodes



def part1(input_path):
    grid = read_file_as_grid(input_path)

    for i, row in enumerate(grid):
        if i % 2:
            assert set(row) == {"."}
    
    start = grid[0].index("S")

    splits, nodes = walk(0, start, grid)
    print(len(splits))
    return splits, nodes


def walk2(row_i, col_i, grid, path=[], solutions=[]):
    if row_i + 1 == len(grid):
        solutions[0] += 1
        # at the end
        return
    
    if grid[row_i + 1][col_i] == "^":
        new_positions = []
        if col_i > 0:
            new_positions.append((row_i + 1, col_i - 1))
        if col_i < (len(grid[0]) - 1):
            new_positions.append((row_i + 1, col_i + 1))
    else:
        new_positions = [(row_i + 1, col_i)]

    for position in new_positions:
        path.append(position)
        walk2(position[0], position[1], grid, path, solutions)
        path.pop() # backtrack

        if solutions[0] % 1000 == 0:
            print(solutions[0])


def part2(input_path):
    grid = read_file_as_grid(input_path)

    for i, row in enumerate(grid):
        if i % 2:
            assert set(row) == {"."}
    
    start = grid[0].index("S")

    solutions = [0]
    walk2(0, start, grid, solutions=solutions)

    print(solutions)

# def part2(input_path):
#     splits, nodes = part1(input_path)
#     tree, start, end = nodes_to_tree(nodes)
#     print(dfs_iterative(tree, start, goal=end[0]))


def nodes_to_tree(nodes):
    # get rid of duplicates and odd numbers rows, no splits there
    nodes = {node for node in nodes if (node[0] % 2 == 0)} 
    sorted_nodes = sorted(nodes)

    tree = {}
    for current_node in sorted_nodes:
        children = [node for node in nodes if node[0] == current_node[0] + 2 and node[1] in [current_node[1] - 1,  current_node[1] + 1]]
        tree[current_node] = children
    print(sorted_nodes)
    return tree, sorted_nodes[0], sorted_nodes[-1]


def dfs_iterative(tree, start, goal):
    visited = set()  # Track visited nodes
    stack = [start]  # Stack for DFS
    solutions = 0
    print(tree)
    while stack:  # Continue until stack is empty
        node = stack.pop()  # Pop a node from the stack
        if node[0] == goal:
            solutions += 1
        if node not in visited:
            visited.add(node)  # Mark node as visited
            stack.extend(reversed(tree[node]))  # Add child nodes to stack
            
    return solutions

