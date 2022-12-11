from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation: str
    test: int
    target: tuple[int, int]


def parse_input(input) -> list:
    monkeys = []

    monkeys_string = [monkey.strip() for monkey in input.split("\n\n")]
    for m in monkeys_string:

        name, items, operation, test, if_true, if_false = [
            line.strip() for line in m.split("\n")
        ]
        items = deque([int(item.strip()) for item in items[16:].split(",")])
        operation = operation.split("=")[-1].strip()
        test = int(test.split(" ")[-1])
        if_true = int(if_true.split(" ")[-1])
        if_false = int(if_false.split(" ")[-1])
        target = (if_false, if_true)

        monkeys.append(Monkey(items, operation, test, target))
    return monkeys


def solve(monkeys: list, part: int, rounds: int) -> int:

    monkeys = deepcopy(monkeys)

    divisor = 1
    for m in monkeys:
        divisor *= m.test

    counter = defaultdict(int)
    for _ in range(rounds):
        for i, m in enumerate(monkeys):
            while m.items:
                counter[i] += 1

                old = m.items.popleft()  # noqa: F841
                new = eval(m.operation)
                if part == 1:
                    new //= 3
                else:
                    new %= divisor
                test = (new % m.test) == 0
                target_monkey = m.target[test]
                monkeys[target_monkey].items.append(new)

    top, second = sorted(counter.values(), reverse=True)[:2]
    return top * second


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        monkeys_string = puzzle_input.read()

    monkeys = parse_input(monkeys_string)

    part_1_ans = solve(monkeys, part=1, rounds=20)
    print(part_1_ans)

    part_2_ans = solve(monkeys, part=2, rounds=10_000)
    print(part_2_ans)
