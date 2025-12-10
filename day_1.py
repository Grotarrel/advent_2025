import re 

INPUT_PATH = "day_1_input.txt"

def load_input() -> list[(str, int)]:
    with open(INPUT_PATH, "r") as f:
        return [(line[0], int(line[1:])) for line in f]
    
    
def run_instruction(pos: int, direction: str, distance: int) -> tuple[int, int]:
    sign = {'L': -1, 'R': 1}
    new_pos = pos + sign[direction] * distance
    n = abs(new_pos // 100)
    new_pos = new_pos % 100
    if direction == 'L':
        if new_pos == 0:
            n += 1
        if pos == 0:
            n -= 1
    return (new_pos, n)



def run_instructions_1(instructions: list[(str, int)], init_pos: int = 50) -> int:
    sign = {'L': -1, 'R': 1}
    pos = init_pos
    nb_0 = 0
    for (direction, distance) in instructions:
        pos += sign[direction] * distance
        pos = pos % 100
        if pos == 0:
            nb_0 += 1
    return nb_0 


def run_instructions_2(instructions: list[(str, int)], init_pos: int = 50) -> int:
    pos = init_pos
    result = 0
    for (direction, distance) in instructions:
        (pos, n) = run_instruction(pos, direction, distance)
        print((direction, distance), " -> ", (pos, n))
        result += n
    return result


def main():
    instr = load_input()
    print(run_instructions_2(instr))

if __name__ == "__main__":
    main()
