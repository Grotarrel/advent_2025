from typing import TypedDict
import math

Prob = TypedDict('Prob', {'numbers': list[int], 'op': str})

INPUT_PATH = "day_6_input.txt"

def read_column(lines: list[str], col: int) -> tuple[int | None, str]:
    column = ''.join([line[col] for line in lines])
    number_str = column[:-1].strip()
    if number_str == '':
        number = None
    else:
        number = int(number_str)
    op = column[-1].strip()
    return (number, op)



def load_input() -> list[Prob]:
    input = open(INPUT_PATH, "r").read().splitlines()
    size = len(input[0])
    numbers = []
    result = []
    for col in range(size-1, -1, -1):
        (n, op) = read_column(input, col)
        if not n:
            continue
        numbers.append(n)
        if op:
            result.append({"numbers": numbers, "op": op})
            numbers = []
    return result

def compute_prob(p: Prob) -> int:
    if p["op"] == '+':
        return sum(p["numbers"])
    elif p["op"] == '*':
        return math.prod(p["numbers"])
    
def main():
    input = load_input()
    print(sum([compute_prob(p) for p in input]))

if __name__ == "__main__":
    main()