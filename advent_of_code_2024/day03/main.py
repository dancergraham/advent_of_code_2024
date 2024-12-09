from pathlib import Path


def parse_input(input_str: str):
    return input_str


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")

import re


def mul(a, b):
    return a * b


def part_1(input_str):
    answer = 0

    for instruction in re.findall(r"mul[(][\d]{1,3},[\d]{1,3}[)]", input_str):
        answer += eval(instruction)

    return answer


def part_2(input_str):
    answer = 0
    activate = True
    for instruction in re.findall(r"mul[(][\d]{1,3},[\d]{1,3}[)]|do\(\)|don't\(\)", input_str):
        if instruction == "do()":
            activate = True
        elif (instruction == "don't()"):
            activate = False
        elif activate:
            answer += eval(instruction)
    return answer


if __name__ == '__main__':
    main()
