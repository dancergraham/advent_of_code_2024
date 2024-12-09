from .main import part_1, part_2

TEST_INPUT = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


def test_part_1():

    assert part_1(TEST_INPUT) == 161


def test_part_2():
    assert part_2(TEST_INPUT) == None


if __name__ == '__main__':
    test_part_1()
    test_part_2()
