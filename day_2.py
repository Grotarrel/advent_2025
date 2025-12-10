import re

INPUT_PATH = "day_2_input.txt"

def is_invalid(id: int) -> bool:
    return bool(re.fullmatch(r"(\d+)\1+", str(id)))
    

def list_invalid(start: int, end: int) -> list[int]:
    return [id for id in range(start, end+1) if is_invalid(id) ]


def sum_invalid(start: int, end: int) -> int:
    return sum(list_invalid(start, end))


def read_range(input: str) -> tuple[int, int]:
    s = input.split('-')
    return (int(s[0]), int(s[1]))


def load_input() -> list[(int, int)]:
    with open(INPUT_PATH, "r") as f:
        text = f.read()
    ranges = text.split(',')
    return [read_range(r) for r in ranges]


def main():
    input = load_input()
    count = sum([sum_invalid(start, end) for (start,end) in input])
    print(count)

if __name__ == "__main__":
    main()