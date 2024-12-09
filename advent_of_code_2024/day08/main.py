from collections import defaultdict
from itertools import permutations
from pathlib import Path


def parse_input(input_str: str):
    antennas = defaultdict(list)
    for y, line in enumerate(input_str.splitlines()):
        for x, char in enumerate(line):
            if char != ".":
                antennas[char].append((x, y))
    return antennas


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def contains(grid, position):
    x, y = position
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def part_1(input_str):
    antennas = parse_input(input_str)
    antinodes = set()
    for antenna, positions in antennas.items():
        for antenna_a, antenna_b in permutations(positions, 2):
            spacing_vec = [antenna_a[i] - antenna_b[i] for i in range(2)]
            antinode = (antenna_a[0] + spacing_vec[0] , antenna_a[1] + spacing_vec[1] )
            if contains(input_str.splitlines(), antinode):
                antinodes.add(antinode)
    return len(antinodes)


def part_2(input_str):
    antennas = parse_input(input_str)
    antinodes = set()
    for antenna, positions in antennas.items():
        for antenna_a, antenna_b in permutations(positions, 2):
            spacing_vec = [antenna_a[i] - antenna_b[i] for i in range(2)]
            inside = True
            i = 0
            while inside:
                antinode = (antenna_a[0] + spacing_vec[0] * i, antenna_a[1] + spacing_vec[1] * i)
                if contains(input_str.splitlines(), antinode):
                    i += 1
                    antinodes.add(antinode)
                else:
                    inside = False
    return len(antinodes)


if __name__ == '__main__':
    main()
