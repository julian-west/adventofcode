"""Day 16 Advent of Code"""

from typing import Tuple, Dict, List, Set
import re


def load_input(file: str) -> Tuple[Dict, List[int], List[List[int]]]:
    """Load input

    Returns a dictionary with the valid values for each field, a list with your
    ticket values, and a list of lists for the nearby tickets
    """
    with open(file, "r") as input_file:
        info_blocks = input_file.read().split("\n\n")

    # Process rules
    rules = info_blocks[0].split("\n")
    rules_dict = {}
    for rule in rules:
        field, first_region, second_region = re.match(
            r"(^[^:]*):\s(\d+-\d+)\sor\s(\d+-\d+)", rule
        ).groups()

        ranges = [
            tuple(int(x) for x in region.split("-"))
            for region in [first_region, second_region]
        ]
        rules_dict[field] = ranges

    # Process your ticket
    your_ticket = [int(x) for x in info_blocks[1][13:].split(",")]

    # Process nearby tickets
    nearby_tickets = []
    for ticket in filter(None, info_blocks[2][16:].split("\n")):
        nearby_tickets.append([int(x) for x in ticket.split(",")])

    return rules_dict, your_ticket, nearby_tickets


def find_valid_ints(rules: Dict) -> Set:
    """Find a set of integers which are valid given the set of rules"""
    valid_set = set()
    for ranges in rules.values():
        for bounds in ranges:
            valid_set = valid_set.union(set(range(bounds[0], bounds[1] + 1)))
    return valid_set


def part1(rules: Dict, nearby_tickets: List[List[int]]) -> int:
    """Check which tickets are invalid. Return sum of invalid numbers"""
    valid_numbers = find_valid_ints(rules)

    invalid_numbers = []
    for ticket in nearby_tickets:
        for value in ticket:
            if not value in valid_numbers:
                invalid_numbers.append(value)

    return sum(invalid_numbers)


if __name__ == "__main__":
    rules_dict, your_ticket, nearby_tickets = load_input("input.txt")

    # Part 1
    print(part1(rules_dict, nearby_tickets))
