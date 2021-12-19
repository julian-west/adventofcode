"""Day 19 Solution"""
import math
from copy import deepcopy
from itertools import combinations

import numpy as np


def process_input(input_str: str) -> list[np.ndarray]:
    """Process the scanner string inputs"""
    scanners = input_str.strip().split("\n\n")
    scanners = [x.split("---\n")[-1].split("\n") for x in scanners]
    return [np.array([list(map(int, y.split(","))) for y in x]) for x in scanners]


def rotations():
    """Generate all possible rotation functions"""
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(np.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = np.cross(vi, vj)
                yield lambda x: np.matmul(x, np.array([vi, vj, vk]))


def fit(
    scanners: list[np.ndarray],
    hashes: list[dict[tuple, tuple]],
    i: int,
    j: int,
    v: tuple[int, int, int],
):
    """Find the correct rotation/translation to make the jth scanner map fit the ith"""
    s1, s2 = scanners[i], scanners[j]
    for rot in rotations():
        s2t = rot(s2)
        p = hashes[i][v][0]
        for q in hashes[j][v]:
            diff = s1[p, :] - s2t[q, :]
            if len((b := set(map(tuple, s2t + diff))) & set(map(tuple, s1))) >= 12:
                return diff, b, rot


def map_hash(coords: np.ndarray) -> dict[tuple, tuple]:
    """
    Generate a hashset of sorted absolute coordinate differences
    between pairs of points
    """
    return {
        tuple(sorted(map(abs, coords[i, :] - coords[j, :]))): (i, j)
        for i, j in combinations(range(len(coords)), 2)
    }


def match(hashes):
    """Figure out which pairs of scanner aps have sufficient overlap"""
    for i, j in combinations(range(len(hashes)), 2):
        if len(m := set(hashes[i]) & set(hashes[j])) >= math.comb(12, 2):
            yield i, j, next(iter(m))


def solve(scanners):
    """Given a list of scanner maps, return list of positions and set of beacons"""
    scanners = deepcopy(scanners)
    positions = {0: (0, 0, 0)}
    hashes = list(map(map_hash, scanners))
    beacons = set(map(tuple, scanners[0]))
    while len(positions) < len(scanners):
        for i, j, v in match(hashes):
            if not (i in positions) ^ (j in positions):
                continue
            elif j in positions:
                i, j = j, i
            positions[j], new_beacons, rot = fit(scanners, hashes, i, j, v)
            scanners[j] = rot(scanners[j]) + positions[j]
            beacons |= new_beacons
    return [positions[i] for i in range(len(scanners))], beacons


def part_1(beacons):
    """Part 1 answer"""
    return len(beacons)


def part_2(positions):
    """Part 2 answer"""
    return max(np.abs(x - y).sum() for x, y in combinations(positions, 2))


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        scanners = process_input(input_file.read())

    positions, beacons = solve(scanners)

    part_1_ans = part_1(beacons)
    print(part_1_ans)

    part_2_ans = part_2(positions)
    print(part_2_ans)
