from main import part_1, part_2

TEST_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def test_part_1():
    part_1_answer = part_1(TEST_INPUT)
    assert part_1_answer == 143


def test_part_2():
    part_2_answer = part_2(TEST_INPUT)
    assert part_2_answer == 123


if __name__ == '__main__':
    test_part_1()
    test_part_2()
