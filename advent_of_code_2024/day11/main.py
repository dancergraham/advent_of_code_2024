import math
from functools import lru_cache
from pathlib import Path


def parse_input(input_str: str):
    return [int(x) for x in input_str.split()]


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def digits(n):
    return math.floor(math.log10(n)) + 1


@lru_cache(maxsize=1_000_000)
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count_stones(1, blinks - 1)
    elif (d := digits(stone)) % 2 == 0:
        a, b = divmod(stone, 10 ** (d // 2))
        return count_stones(a, blinks - 1) + count_stones(b, blinks - 1)
    return count_stones(2024 * stone, blinks - 1)


def part_1(input_str):
    stones = parse_input(input_str)
    return sum(count_stones(stone, 25) for stone in stones)


def part_2(input_str):
    stones = parse_input(input_str)
    return sum(count_stones(stone, 75) for stone in stones)


if __name__ == '__main__':
    main()
