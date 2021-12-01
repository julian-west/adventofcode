"""Day 19 tests"""
from solution import load_input, part1

test_rules, test_msgs = load_input("test_input.txt")


def test_part1(rules=test_rules, msgs=test_msgs, expected=2):
    """Test part1 function"""
    assert part1(rules, msgs) == expected
