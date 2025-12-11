import heapq

INPUT_PATH = "day_8_input.txt"


type Point = tuple[int, int, int]


def distance(pair: tuple[Point, Point]) -> int:
    (a, b) = pair
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2]- b[2]) ** 2


def load_input() -> list[Point]:
    result = []
    with open(INPUT_PATH, "r") as f:
        for line in f:
            triple = line.split(',')
            point = (int(triple[0]), int(triple[1]), int(triple[2]))
            result.append(point)
    return result


def shortest_paths(points: list[Point], limit: int = 0) -> list[Point, Point]:
    pairs = [(a, b) for (i, a) in enumerate(points) for b in points[i+1:]]
    if limit == 0:
        return sorted(pairs, key = distance)
    else:
        return heapq.nsmallest(limit, pairs, distance)

def make_circuits(points: list[Point]) -> dict[Point, int]:
    return {p: i for (i, p) in enumerate(points) }



def add_connexion(circuits: dict[Point, int], connexion: tuple[Point, Point]):
    (a, b) = connexion 
    c_a = circuits[a]
    c_b = circuits[b]
    new_c = min(c_a, c_b)
    for p, c in circuits.items():
        if c == c_a or c == c_b:
            circuits[p] = new_c

def is_connected(circuits: dict[Point, int]) -> bool:
    return len(set(circuits.values())) == 1


def circuits_list(circuits: dict[Point, int]) -> list[list[Point]]:
    return [ [p for p in circuits if circuits[p] == c] for c in set(circuits.values())]


def main_1():
    points = load_input()
    circuits = make_circuits(points)
    connexions = shortest_paths(points, limit = 1000)
    for connexion in connexions:
        add_connexion(circuits, connexion)
    circ_list = circuits_list(circuits)
    three_largest = heapq.nlargest(3, circ_list, len)
    result = len(three_largest[0]) * len(three_largest[1]) * len(three_largest[2])
    print(result)


def main_2():
    points = load_input()
    circuits = make_circuits(points)
    connexions = shortest_paths(points)
    for connexion in connexions:
        add_connexion(circuits, connexion)
        if is_connected(circuits):
            (a ,b) = connexion
            print(a[0] * b[0])
            break


if __name__ == "__main__":
    main_2()
