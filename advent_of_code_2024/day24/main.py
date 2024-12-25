from operator import and_, or_, xor
from pathlib import Path
from itertools import count

operators = {'AND': and_, 'OR': or_, 'XOR': xor}

class Connection:
    def __init__(self, left, right, operator, out_wire):
        self.left = left
        self.right = right
        self.operator = operator
        self.out_wire = out_wire

    def __repr__(self):
        return f"{self.left} {self.operator} {self.right} -> {self.out_wire}"

    def evaluate(self, wires):
        return operators[self.operator](int(wires[self.left]),
                                        int(wires[self.right]))

def parse_input(input_str: str):
    wires, connections = {}, []
    for line in input_str.splitlines():
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)

        elif "->" in line:
            left, opera, right, _, out_wire = line.split()
            connections.append(Connection(left, right, opera, out_wire))
    return wires, connections


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    wires, connections = parse_input(input_str)
    print(wires, connections)
    while connections:
        for connection in connections:
            if connection.left not in wires or connection.right not in wires:
                continue
            wires[connection.out_wire] = connection.evaluate(wires)
            connections.remove(connection)
    output = []
    for i in count():
        if (digit:= f"z{i:02}") in wires:
            output.append(str(wires[digit]))
        else:
            break

    return int("".join(output)[::-1], base=2)


def part_2(input_str):
    answer = 0
    input_str = parse_input(input_str)
    return answer


if __name__ == '__main__':
    main()
