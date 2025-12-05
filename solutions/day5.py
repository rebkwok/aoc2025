from utils import read_file_as_lines


def collapse_ranges(ranges):
    ranges.sort()
    collapsed_ranges = ranges[:1]
    for frange in ranges[1:]:    
        previous = collapsed_ranges[-1]
        if previous[1] >= frange[0]:
            if frange[1] < previous[1]:
                stop = previous[1]
            else:
                stop = frange[1]
            collapsed_ranges[-1] = (previous[0], stop)
        else:
            collapsed_ranges.append(frange)
    return collapsed_ranges


def part1(input_path):
    data = read_file_as_lines(input_path)
    split = data.index("")
    
    fresh_ranges = [it.split("-") for it in data[:split]]
    fresh_ranges = [(int(start), int(stop)) for start, stop in fresh_ranges]
    ingredients = [int(ing_id) for ing_id in data[split + 1:]]
    
    collapsed_ranges = collapse_ranges(fresh_ranges)

    count = 0
    for ing in ingredients:
        in_range = next((True for (start, stop) in collapsed_ranges if start <= ing <= stop), None)
        if in_range:
            count += 1
            continue
    
    print(count)


def part2(input_path):
    data = read_file_as_lines(input_path)
    split = data.index("")
    
    fresh_ranges = [it.split("-") for it in data[:split]]
    fresh_ranges = [(int(start), int(stop)) for start, stop in fresh_ranges]
    
    collapsed_ranges = collapse_ranges(fresh_ranges)

    total = sum([(stop - start) + 1 for start, stop in collapsed_ranges])

    print(total)