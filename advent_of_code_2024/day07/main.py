from operator import add, mul, sub, truediv
from pathlib import Path


def parse_input(input_str: str):
    lines = input_str.splitlines()
    sums = ((int(a), [int(v) for v in b.split()]) for a, b in [line.split(": ") for line in input_str.splitlines()])
    return sums


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    for result, digits in  parse_input(input_str):
        results = {digits.pop(0)}
        operators = [add, mul]
        for b in digits:
            for a in list(results):
                for operator in operators:
                    results.add(operator(a, b))
        if result in results:
            answer += result

    return answer


def part_2(input_str):
    def concat(a, b):
        return int(f"{a}{b}")

    answer = 0
    for result, digits in  parse_input(input_str):
        results = {digits.pop(0)}
        operators = [add, mul, concat]
        for b in digits:
            new_results = []
            for a in results:
                if a <= result:
                    for operator in operators:
                        new_results.append(operator(a, b))
            results = sorted(new_results)
        if result in results:
            answer += result

    return answer


if __name__ == '__main__':
    main()
