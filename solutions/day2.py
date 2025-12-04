from utils import read_file_as_lines


def is_repeated(digits):
    digit_count = len(digits)
    if digit_count % 2 != 0:
        return False
    return digits[0:int(digit_count/2)] == digits[int(digit_count/2):]


def part1(input_path):
    data = read_file_as_lines(input_path)[0]
    ranges = data.split(",")
    invalid_ids = []
    for idrange in ranges:
        start, end = idrange.split("-")
        for i in range(int(start), int(end) + 1):
            if is_repeated(str(i)):
                invalid_ids.append(i)
    print(sum(invalid_ids))


def is_invalid(digits):
    # only 1 digit
    digit_count = len(digits)
    if digit_count == 1:
        return False
    # all the same digit
    if len(set(digits)) == 1:
        return True
    
    for chunk_length in range(2, len(digits)//2 + 1):
        if digit_count % chunk_length != 0:
            continue
        repeated_chunk = None
        for i in range(0, (digit_count - chunk_length) + 1, chunk_length):
            this_chunk = digits[i:i + chunk_length]
            if not repeated_chunk:
                repeated_chunk = this_chunk
            elif this_chunk != repeated_chunk:
                repeated_chunk = None
                break
        if repeated_chunk:
            return True

    return False


def part2(input_path):
    data = read_file_as_lines(input_path)[0]
    ranges = data.split(",")
    invalid_ids = []
    for idrange in ranges:
        start, end = idrange.split("-")
        for i in range(int(start), int(end) + 1):
            if is_invalid(str(i)):
                print(i)
                invalid_ids.append(i)
    print("Result")
    print(sum(invalid_ids))