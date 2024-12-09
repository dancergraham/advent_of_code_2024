from pathlib import Path


def parse_input(input_str: str):
    return [line.replace("^", ".")
            for line in input_str.splitlines()]


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def find_initial(map):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '^':
                return (x, y)


def contains(map, position):
    x, y = position
    return 0 <= x < len(map[0]) and 0 <= y < len(map)


def part_1(input_str):
    visited = set()
    lab_map = parse_input(input_str)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W
    direction_index = 0
    position = find_initial(input_str.splitlines())
    try:
        while contains(lab_map, position):
            visited.add(position)
            x0, y0 = position
            dx, dy = directions[direction_index]
            (x1, y1) = (x0 + dx, y0 + dy)
            match lab_map[y1][x1]:
                case '#':
                    direction_index = (direction_index + 1) % 4
                case '.':
                    position = (x1, y1)
    except IndexError:
        pass
    return len(visited)

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W

def part_2(input_str):
    def is_loop(lab_map, position, direction_index):
        this_loop = set()
        try:
            while contains(lab_map, position):
                this_loop.add((position, direction_index))
                x0, y0 = position
                dx, dy = directions[direction_index]
                (x1, y1) = (x0 + dx, y0 + dy)
                if not contains(lab_map, (x1, y1)):
                    return False, None
                match lab_map[y1][x1]:
                    case '#':
                        direction_index = (direction_index + 1) % 4
                    case '.':
                        position = (x1, y1)
                        if (position, direction_index) in this_loop:
                            return True, len(this_loop)
        except IndexError:
            return False, None

    visited = set()
    lab_map = parse_input(input_str)
    direction_index = 0
    position = find_initial(input_str.splitlines())
    loop_positions = set()
    loop_lengths = []
    try:
        while contains(lab_map, position):
            visited.add((position, direction_index))
            x0, y0 = position
            dx, dy = directions[direction_index]
            (x1, y1) = (x0 + dx, y0 + dy)
            match lab_map[y1][x1]:
                case '#':
                    direction_index = (direction_index + 1) % 4
                case '.':
                    new_map = add_object(lab_map, (x1, y1))
                    is_loopy, loop_length = is_loop(new_map, position, direction_index)
                    if is_loopy:
                        loop_positions.add((x1, y1))
                        loop_lengths.append(loop_length)
                        print(f"Loop at {x1}, {y1}, length {loop_length}")
                    position = (x1, y1)
    except IndexError:
        pass
    print(min(loop_lengths))
    return len(loop_positions)




def add_object(old_map, position):
    x, y = position
    new_map = [list(row) for row in old_map]
    new_map[y][x] = '#'
    return new_map


if __name__ == '__main__':
    main()
