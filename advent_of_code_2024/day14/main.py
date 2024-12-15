import math
import re
from pathlib import Path


class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy


def parse_input(input_str: str):
    for line in input_str.splitlines():
        x, y, dx, dy = map(int, re.search(r"p=(.*),(.*) v=(.*),(.*)", line).groups())
        yield x, y, dx, dy


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    if len(input_str.splitlines()) == 12:  # Test input
        width, height = 11, 7
    else:
        width, height = 101, 103
    quadrants = {0: 0, 1: 0, 2: 0, 3: 0}
    for robot in parse_input(input_str):
        x, y, dx, dy = robot
        x_position = (x + 100 * dx) % width
        y_position = (y + 100 * dy) % height
        if x_position < width // 2 and y_position < height // 2:
            quadrants[0] += 1
        elif x_position > width // 2 and y_position < height // 2:
            quadrants[1] += 1
        elif x_position < width // 2 and y_position > height // 2:
            quadrants[2] += 1
        elif x_position > width // 2 and y_position > height // 2:
            quadrants[3] += 1
    return math.prod(quadrants.values())


def part_2(input_str):
    robots = [Robot(*robot) for robot in parse_input(input_str)]
    width, height = 101, 103
    for i in range(7753):
        is_not_tannenbaum = 0
        for robot in robots:
            if robot.x < 51:
                x_position = robot.x
            else:
                x_position = 51 - robot.x
            y_position = robot.y

            if x_position + y_position < 30:
                is_not_tannenbaum += 1
            robot.x = (robot.x + robot.dx) % width
            robot.y = (robot.y + robot.dy) % height
        plot(robots)
        print(is_not_tannenbaum, i)


def plot(robots):
    width, height = 101, 103
    grid = [["." for _ in range(width)] for _ in range(height)]
    for robot in robots:
        grid[robot.y][robot.x] = "#"
    for row in grid:
        print("".join(row))

    print()


if __name__ == '__main__':
    main()
