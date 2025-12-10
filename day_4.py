INPUT_PATH = "day_4_input.txt"

def load_input() -> list[list[bool]]:
    with open(INPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    return [[c == '@' for c in line] for line in lines]


def adjacent(grid: list[list[bool]], x: int, y: int) -> list[bool]:
    result = []
    for i in range(x-1,x+2):
        if i < 0:
            continue
        for j in range(y-1,y+2):
            if (i,j) == (x,y) or j < 0:
                continue
            try:
                result.append(grid[i][j])
            except IndexError:
                continue
    return result


def accessible(grid: list[list[bool]], x: int, y: int) -> bool:
    adjacent_rolls = [x for x in adjacent(grid, x, y) if x]
    return len(adjacent_rolls) <= 3

def all_accessible(grid: list[list[bool]]) -> list[int, int]:
    return [(x,y) for x in range(0,len(grid)) for y in range(0,len(grid[0])) if grid[x][y] and accessible(grid, x,y)]


def update_grid(grid: list[list[bool]]) -> int:
    to_remove = all_accessible(grid)
    for (x,y) in to_remove:
        grid[x][y] = False
    return len(to_remove)


def main():
    grid = load_input()
    total_removed = 0
    while True:
        removed = update_grid(grid)
        total_removed += removed
        if removed == 0:
            break
    print(total_removed)

if __name__ == "__main__":
    main()
    