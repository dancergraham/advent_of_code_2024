from main import part_1, part_2

TEST_INPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def test_part_1():
    assert part_1(TEST_INPUT) == 3749


def test_part_2():
    assert part_2(TEST_INPUT) == 11387


if __name__ == '__main__':
    test_part_1()
    test_part_2()
