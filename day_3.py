INOUT_PATH = "day_3_input.txt"

def digits_to_number(digits: list[int]) -> int:
    return int(''.join([str(d) for d in digits]))

def max_joltage(bank: list[int], nb_digits: int = 2) -> int:
    digits = []
    b = bank
    for i in range(0, nb_digits):
        buffer = nb_digits - i -1
        if buffer == 0:
            max_digit = max(b)
        else:
            max_digit = max(b[:-(nb_digits - i -1)])
        max_index = b.index(max_digit)
        digits.append(max_digit)
        b = b[max_index+1:]
    return digits_to_number(digits)

def total_joltage(banks: list[list[int]], nb_digits: int = 2) -> int:
    return sum([max_joltage(b, nb_digits) for b in banks])

def read_bank(s: str) -> list[int]:
    return [ int(d) for d in s]

def load_input() -> list[list[int]]:
    with open(INOUT_PATH, "r") as f:
        lines = f.read().splitlines()
    return [read_bank(line) for line in lines]
    
def main():
    banks = load_input()
    total = total_joltage(banks, 12)
    print(total)

if __name__ == "__main__":
    main()