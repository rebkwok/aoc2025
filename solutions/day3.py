from utils import read_file_as_lines


def part1(input_path):
    data = read_file_as_lines(input_path)

    joltages = []

    for batch in data:
        batch_as_ints = [int(batt) for batt in batch]
        top = max(batch_as_ints)

        # is the max at the end?
        if top == batch_as_ints[-1]:
            second_top = top
            top = max(batch_as_ints[0:-1])
        else:
            top_ix = batch_as_ints.index(top)
            rest = batch_as_ints[top_ix + 1:]
            second_top = max(rest)
        joltages.append(int(f"{top}{second_top}"))
    
    print(joltages)
    print(sum(joltages))
        


def get_largest_possible(batch, remainder):
    for target in range(9, 0, -1):
        for i, num in enumerate(batch):
            if num == target and (len(batch) - batch.index(num)) >= remainder:
                return num, batch[batch.index(num) + 1:]

def part2(input_path):
    data = read_file_as_lines(input_path)

    joltages = []

    for batch in data:
        batch_as_ints = [int(batt) for batt in batch]

        joltage = ""
        # find the largest number that still leaves enough remaining
        for i in range(12, 0, -1):
            num, batch_as_ints = get_largest_possible(batch_as_ints, i)
            joltage += str(num)
        joltages.append(int(joltage))

    print(sum(joltages))
                
