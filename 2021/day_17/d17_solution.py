"""Day 17 Solution"""

import re
from dataclasses import dataclass
from math import sqrt


@dataclass
class Velocity:
    forward: int
    vertical: int


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Target:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def hit(self, p: Position) -> bool:
        """Check if coordinate is within the target area"""
        if self.min_x <= p.x <= self.max_x and self.min_y <= p.y <= self.max_y:
            return True
        return False


def process_input(input_str: str) -> Target:
    """Extract numbers from input string"""
    return Target(*[int(i) for i in re.findall(r"-?\d+", input_str)])


def calc_v0_max(target: Target) -> Velocity:
    """Calculate the maximum velocity to reach target"""
    return Velocity(target.max_x, abs(target.min_y + 1))


def calc_v0_min(target: Target) -> Velocity:
    """Calculate the minimum velocity to reach target"""
    return Velocity(int(sqrt(target.min_x * 2)), target.min_y)


def reaches_target(v: Velocity, target: Target) -> bool:
    p = Position(0, 0)
    while True:
        p.x += v.forward
        p.y += v.vertical
        v.forward -= 1 if v.forward else 0
        v.vertical -= 1
        if p.x > target.max_x or p.y < target.min_y:
            return False
        if target.hit(p):
            return True


def calc_highest_vertical_position(v: Velocity) -> int:
    return v.vertical * (v.vertical + 1) // 2


def part_1(target: Target) -> int:
    v0_max = calc_v0_max(target)
    return calc_highest_vertical_position(v0_max)


def part_2(target: Target) -> int:
    v0_min = calc_v0_min(target)
    v0_max = calc_v0_max(target)
    r2 = 0
    for v0_forward in range(v0_min.forward, v0_max.forward + 1):
        for v0_vertical in range(v0_min.vertical, v0_max.vertical + 1):
            r2 += reaches_target(Velocity(v0_forward, v0_vertical), target)
    return r2


if __name__ == "__main__":
    with open("input.txt") as input:
        target = process_input(input.read().strip())

    part_1_ans = part_1(target)
    print(part_1_ans)

    part_2_ans = part_2(target)
    print(part_2_ans)
