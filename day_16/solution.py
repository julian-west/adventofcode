"""Day 16 Advent of Code"""

from typing import Tuple, Dict, List, Set
import re
import numpy as np


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

        valid_numbers = set()
        for region in [first_region, second_region]:
            region_bounds = [int(x) for x in region.split("-")]
            region_valid = set(range(region_bounds[0], region_bounds[1] + 1))
            valid_numbers = valid_numbers.union(region_valid)

        rules_dict[field] = valid_numbers

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
    for valid_field_values in rules.values():
        valid_set = valid_set.union(valid_field_values)

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


def part2(rules: Dict, your_ticket: List[int], nearby_tickets: List[List[int]]) -> int:
    """Solve part 2"""

    solved_fields = {}

    valid_numbers = find_valid_ints(rules)

    valid_nearby_tickets = []
    for ticket in nearby_tickets:
        if not set(ticket) - set(valid_numbers):
            valid_nearby_tickets.append(ticket)

    tickets = np.vstack((your_ticket, nearby_tickets))
    ticket_field_unique_values = np.apply_along_axis(set, 0, tickets)

    while len(rules) >= len(solved_fields):
        still_to_solve = [ix for ix in range(len(rules)) if ix not in solved_fields]
        for ix in range(tickets.shape[1]):
            valid_fields = []
            outstanding_fields = [
                field for field in rules.keys() if field not in solved_fields.values()
            ]
            for field in outstanding_fields:
                if (
                    not (ticket_field_unique_values[ix] ^ rules[field])
                    & ticket_field_unique_values[ix]
                ):
                    valid_fields.append(field)
            if len(valid_fields) == 1:
                solved_fields[ix] = valid_fields[0]

        print(solved_fields)
        print(len(outstanding_fields))

    return solved_fields


if __name__ == "__main__":
    rules_dict, your_ticket, nearby_tickets = load_input("input.txt")

    # Part 1
    print(part1(rules_dict, nearby_tickets))

    # Part 2
    print(part2(rules_dict, your_ticket, nearby_tickets))
