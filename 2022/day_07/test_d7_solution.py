"""Test day 7 solution"""
import pytest
from d7_solution import get_dir_sizes, get_dir_tree, part_1, part_2

test_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


@pytest.fixture
def commands():
    return list(filter(None, [line.strip() for line in test_input.split("\n")]))


@pytest.fixture
def dir_tree(commands):
    return get_dir_tree(commands)


@pytest.fixture
def dir_sizes(dir_tree):
    return get_dir_sizes(dir_tree)


def test_part_1(dir_sizes):
    assert part_1(dir_sizes, threshold=100_000) == 95_437


def test_part_2(dir_sizes):
    assert (
        part_2(
            dir_sizes,
            max_disk_space=70_000_000,
            required_disk_space=30_000_000,
        )
        == 24_933_642
    )
