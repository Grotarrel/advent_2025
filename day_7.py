

INPUT_PATH = "day_7_input.txt"

class Pos:
    def __init__(self, splitter: bool = False, paths: int = 0):
        self.splitter = splitter
        self.paths = paths

def read_pos(c: str) -> Pos:
    if c == '.':
        return Pos()
    if c == 'S':
        return Pos(paths = 1)
    if c == '^':
        return Pos(splitter = True)

def load_input() -> list[list[Pos]]:
    lines = open(INPUT_PATH, "r").read().splitlines()
    grid = [[read_pos(c) for c in line] for line in lines]
    return grid

def split_at(line: str, c: int) -> str:
    if c == 0:
        return line[c] + '|' + line[c+2:]
    elif c == len(line) - 1:
        return line[:c-1] + '|' + line[c]
    else:
        return line[:c-1] + '|' + line[c] + '|' + line[c+2:]
    
def propagate_at(line: str, c: int) -> str:
    return line[:c] + '|' + line[c+1:]

def process_line(grid: list[list[Pos]], l: int):
    for (c, pos) in enumerate(grid[l]):
        if grid[l+1][c].splitter:
            try:
                grid[l+1][c-1].paths += pos.paths
            except IndexError:
                pass 
            try:
                grid[l+1][c+1].paths += pos.paths
            except IndexError:
                pass
        else:
            grid[l+1][c].paths += pos.paths

def process_grid(grid: list[str]):
    for l in range(len(grid)-1):
        process_line(grid, l)

def main():
    grid = load_input()
    process_grid(grid)
    total_paths = sum([pos.paths for pos in grid[-1]])
    print(total_paths)

if __name__ == "__main__":
    main()
