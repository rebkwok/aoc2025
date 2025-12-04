from utils import read_file_as_lines


def part1(input_path):
    data = read_file_as_lines(input_path)
    current = 50
    zeros = 0
    for line in data:
        direction = line[0]
        count = int(line[1:]) % 100

        if direction == "R":
            current += count
        else:
            current -= count

        current = current % 100
        if current == 0:
            zeros += 1
        print(current)
    print("Zeros: " + str(zeros))


def part2(input_path):
    data = read_file_as_lines(input_path)
    current = 50
    zeros = 0

    for i, line in enumerate(data):
        print(f"Line {i}: {line}")
        print(f"start: {current}")
        print(f"zeros: {zeros}")

        direction = line[0]
        count_including_rotations = int(line[1:])
        count = count_including_rotations % 100

        direction = line[0]
        count = int(line[1:]) % 100

        if direction == "R":
            new_current = current + count
        else:
            new_current = current - count

        new_current = new_current % 100
        # count if we land on 0
        if new_current == 0:
            zeros += 1
        elif current != 0:
            # did the turn go through zero?
            # only check if we didn't start on zero
            if direction == "R" and new_current < current:
                print("R, through 0")
                zeros += 1
            elif direction == "L" and new_current > current:
                print("L, through 0")
                zeros += 1
        
        # add the full rotations
        full_rotations = count_including_rotations // 100
        zeros += full_rotations

        current = new_current
        print(f"end: {current}")
        print(f"zeros: {zeros}\n")

    print(current)
    print("Zeros: " + str(zeros))

