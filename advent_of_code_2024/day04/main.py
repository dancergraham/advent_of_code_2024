from collections import defaultdict
from pathlib import Path
import re

def parse_input(input_str: str):
    return input_str

def lr(input_str: str):
    return input_str.splitlines()


def ud(input_str: str):
    return["".join([line[i] for line in input_str.splitlines()]) for i in range(len(input_str.splitlines()[0]))]


def diagonal(input_str: str):
    diagonals = []
    width = len(input_str.splitlines()[0])
    grid = input_str.splitlines()
    # iterate over the diagonals from near the top right to top left(excluded)
    # iterate over the diagonals from near the top left to bottom left
    for starting_column in range(-len(grid), len(grid)):
        diagonal = []
        for row in range(len(grid)):
            column = starting_column + row
            if contains(grid, (row, column)):
                diagonal.append(grid[row][column])
        diagonals.append("".join(diagonal))
    return diagonals


def lanogaid(input_str: str):
    diagonals = []
    width = len(input_str.splitlines()[0])
    grid = input_str.splitlines()
    # iterate over the diagonals from near the top right to top left(excluded)
    # iterate over the diagonals from near the top left to bottom left
    for starting_column in range(len(grid) * 2):
        diagonal = []
        for row in range(len(grid)):
            column = starting_column - row
            if contains(grid, (row, column)):
                diagonal.append(grid[row][column])
        diagonals.append("".join(diagonal))
    return diagonals

def contains(map, position):
    x, y = position
    return 0 <= x < len(map[0]) and 0 <= y < len(map)


def main():
    puzzle_input = Path('input.txt').read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


def part_1(input_str):
    answer = 0
    answer += sum(len(re.findall("XMAS", line)) for line in lr(input_str))
    answer += sum(len(re.findall("SAMX", line)) for line in lr(input_str))
    answer += sum(len(re.findall("XMAS", line)) for line in ud(input_str))
    answer += sum(len(re.findall("SAMX", line)) for line in ud(input_str))
    answer += sum(len(re.findall("XMAS", line)) for line in diagonal(input_str))
    answer += sum(len(re.findall("SAMX", line)) for line in diagonal(input_str))
    answer += sum(len(re.findall("XMAS", line)) for line in lanogaid(input_str))
    answer += sum(len(re.findall("SAMX", line)) for line in lanogaid(input_str))
    return answer

def part_1a(input_str):
    answer = 0
    grid = input_str.splitlines()
    width = len(input_str.splitlines()[0])
    directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    candidates = {(i, j, None) : directions for i in range(width) for j in range(width)}
    for letter in "XMAS":
        new_candidates = defaultdict(list)
        for (row, col, prev_dir), directions in candidates.items():
            if grid[row][col] == letter:
                for direction in directions:
                    new_candidates[(row, col)].append(direction)
    return answer

def part_2(input_str):
    import re
    r = re.compile(r"M(?=.S.{138}.A..{138}M.S|.M.{138}.A..{138}S.S)|S(?=.M.{138}.A..{138}S.M|.S.{138}.A..{138}M.M)", re.DOTALL)
    return len(r.findall(input_str))


if __name__ == '__main__':
    main()
