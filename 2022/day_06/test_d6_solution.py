"""Day 6 tests"""
import pytest
from d6_solution import get_message_marker


@pytest.mark.parametrize(
    "datastream,window_size,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
    ],
)
def test_part_1(datastream, window_size, expected):
    assert get_message_marker(datastream, window_size) == expected


@pytest.mark.parametrize(
    "datastream,window_size,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26),
    ],
)
def test_part_2(datastream, window_size, expected):
    assert get_message_marker(datastream, window_size) == expected


def test_raise_value_error():
    with pytest.raises(ValueError):
        assert get_message_marker("qqqqqqqqqqqq", 4)
