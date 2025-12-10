INPUT_PATH = "day_5_input.txt"

def read_range(s: str) -> tuple[int, int]:
    split = s.split('-')
    return (int(split[0]), int(split[1]))

def load_input() -> tuple[list[int, int],list[int]]:
    fresh = []
    with open(INPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    for (i, line) in enumerate(lines):
        if line == '':
            break 
        (start, end) = read_range(line)
        fresh.append((start, end))
    ids = [int(line) for line in lines[i+1:]]
    return (fresh, ids)

def is_fresh(fresh: list[int, int], id: int) -> bool:
    for (start, end) in fresh:
        if start <= id and id <= end:
            return True
    return False

def update_ranges(ranges: list[int, int], start: int, end: int) -> list[int, int]:
    for (i, (lower, upper)) in enumerate(ranges):
        if start <= upper:
            if end < lower:
                return ranges[:i] + [(start, end)] + ranges[i:]
            else:
                n = max( (j for j in range(i,len(ranges)) if end >= ranges[j][0]) )
                new_lower = min(start, lower)
                new_upper = max(end, ranges[n][1])
                return ranges[:i] + [(new_lower, new_upper)] + ranges[n+1:]
    return ranges + [(start, end)]

def build_ranges(bounds: list[int, int]) -> list[int, int]:
    result = []
    for (start, end) in bounds:
        result = update_ranges(result, start, end)
    return result


def count_fresh(ranges: list[int, int]) -> int:
    return sum([ end-start+1 for (start, end) in ranges])


def main_1():
    (fresh, ids) = load_input()
    print(len([id for id in ids if is_fresh(fresh, id)]))

def main_2():
    (bounds, _) = load_input()
    ranges = build_ranges(bounds)
    print(count_fresh(ranges))


if __name__ == "__main__":
    main_2()
