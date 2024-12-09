from main import part_1, part_2

TEST_INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def test_part_1():
    part__ = part_1(TEST_INPUT)
    assert part__ == 18


def test_part_2():
    assert part_2(TEST_INPUT) == None


if __name__ == '__main__':
    test_part_1()
    test_part_2()
