import pytest
from d11_solution import parse_input, solve

test_input = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


@pytest.fixture
def monkeys():
    return parse_input(test_input)


@pytest.mark.parametrize(
    "part,rounds,expected",
    [
        (1, 20, 10605),
        (2, 10000, 2713310158),
    ],
)
def test_solve(part, rounds, expected, monkeys):
    assert solve(monkeys, part, rounds) == expected
