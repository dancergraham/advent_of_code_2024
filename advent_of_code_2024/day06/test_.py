from main import part_1, part_2

TEST_INPUT = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_part_1():
    assert part_1(TEST_INPUT) == 41


def test_part_2():
    ans = part_2(TEST_INPUT)
    assert ans == 6


if __name__ == '__main__':
    test_part_1()
    test_part_2()
