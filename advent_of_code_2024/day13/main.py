import math
import re
from pathlib import Path


def parse_input(input_str: str):
    for machine in input_str.split("\n\n"):
        machine = re.findall(""".*: X[+=](.*), Y[+=](.*)""", machine)
        yield ((int(a), int(b)) for a, b in machine)


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    for (a1, a2), (b1, b2), (c1, c2) in parse_input(input_str):
        B = (c1 - (a1 / a2) * c2) / (b1 - (a1 / a2) * b2)
        A = (c1 - B * b1) / a1
        if 0 <= A <= 100 and 0 <= B <= 100:
            if math.isclose(A, round(A)) and math.isclose(B, round(B)):
                answer += A * 3 + B
    return answer


def isclose(a, b):
    return abs(a - b) < 0.001


def part_2(input_str):
    answer = 0
    for (a1, a2), (b1, b2), (c1, c2) in parse_input(input_str):
        c1 += 10000000000000
        c2 += 10000000000000
        B = (c1 - (a1 / a2) * c2) / (b1 - (a1 / a2) * b2)
        A = (c1 - B * b1) / a1
        if isclose(A, round(A)) and isclose(B, round(B)):
            answer += A * 3 + B
    return answer


if __name__ == '__main__':
    main()
