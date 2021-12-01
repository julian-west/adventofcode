"""Day 19 Advent of Code"""
from typing import Dict, List, Tuple


def load_input(file: str) -> Tuple:
    """load data input"""
    with open(file, "r") as input_file:
        data = input_file.readlines()
        data = [line.strip() for line in data]

    rules_data = data[: data.index("")]
    msgs = data[data.index("") :]

    rules = {}
    for line in rules_data:
        rule_num, rule_options = line.split(": ")
        options = [op.split() for op in rule_options.split("|")]
        rules[int(rule_num)] = options

    return rules, msgs


def solve(num: int, rules: Dict, str_rules: Dict) -> List:
    """Find all valid message possibilities"""
    rule_options = rules[num]

    if ['"a"'] in rule_options:
        return ["a"]
    if ['"b"'] in rule_options:
        return ["b"]

    if num in str_rules:
        return str_rules[num]

    final = []
    for option in rule_options:
        str_ops: List[str] = []
        for rule in option:
            sub_ops = solve(int(rule), rules, str_rules)

            if len(str_ops) == 0:
                str_ops = sub_ops.copy()
            else:
                combined = []
                for s in sub_ops:
                    for op in str_ops:
                        combined.append(op + s)
                str_ops = combined.copy()
        final += str_ops
    str_rules[num] = final

    return final


def part1(rules: Dict, msgs: List) -> int:
    """Solve part 1"""
    all_possibilities = solve(num=0, rules=rules, str_rules={})
    return len([msg for msg in msgs if msg in all_possibilities])


if __name__ == "__main__":
    rules, msgs = load_input("input.txt")

    # part 1
    print(part1(rules, msgs))
