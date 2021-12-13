"""Day 13 tests"""
from d13_solution import Fold, Point, part_1

points = [
    Point(6, 10),
    Point(0, 14),
    Point(9, 10),
    Point(0, 3),
    Point(10, 4),
    Point(4, 11),
    Point(6, 0),
    Point(6, 12),
    Point(4, 1),
    Point(0, 13),
    Point(10, 12),
    Point(3, 4),
    Point(3, 0),
    Point(8, 4),
    Point(1, 10),
    Point(2, 14),
    Point(8, 10),
    Point(9, 0),
]

folds = [Fold("y", 7), Fold("x", 5)]


def test_part_1():
    assert part_1(points, folds[0]) == 17
