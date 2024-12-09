from pathlib import Path


def parse_input(input_str: str):
    rules, updates = input_str.split("\n\n")
    rules = rules.splitlines()
    rules = [rule.split("|") for rule in rules]
    updates = updates.splitlines()
    updates = [update.split(",") for update in updates]
    return rules, updates


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    rules, updates = parse_input(input_str)
    for update in updates:
        middle_page = update[len(update)//2]
        in_right_order = correctly_ordered(rules, update)
        if in_right_order:
            answer += int(middle_page)
    return answer


def correctly_ordered(rules, update):
    in_right_order = True
    for i, page in enumerate(update):
        for a, b in rules:
            if a == page:
                if b in update[:i]:
                    return False
    return in_right_order

def fix_order(rules, update):
    for i, page in enumerate(update):
        for a, b in rules:
            if a == page:
                if b in update[:i]:
                    i_b = update.index(b)
                    update[i] = b
                    update[i_b] = a
                    return update


def part_2(input_str):
    answer = 0
    rules, updates = parse_input(input_str)
    for update in updates:
        middle_page = update[len(update)//2]
        in_right_order = correctly_ordered(rules, update)
        if not in_right_order:
            while not correctly_ordered(rules, update):
                update = fix_order(rules, update)
            middle_page = update[len(update) // 2]
            answer += int(middle_page)
    return answer

if __name__ == '__main__':
    main()
