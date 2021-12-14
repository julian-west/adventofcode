"""Day 14 Solution"""
from collections import Counter, defaultdict


def process_polymer(polymer_str: str) -> dict[str, int]:
    """Extract pairs and count their frequency"""
    return Counter([a + b for a, b in zip(polymer_str, polymer_str[1:])])


def process_pairs(pairs_str: str) -> dict[str, str]:
    """Process input string of pairs"""
    pairs = dict()
    for pair in pairs_str.strip().split("\n"):
        split = pair.split(" -> ")
        pairs[split[0]] = split[1]
    return pairs


def polymerise(
    polymer: dict[str, int], pairs: dict[str, str], steps: int
) -> dict[str, int]:
    """Apply the polymerisation for a given number of steps"""
    for _ in range(steps):
        new_polymer = defaultdict(int)
        for pair, count in polymer.items():
            for new_pair in [pair[0] + pairs[pair], pairs[pair] + pair[1]]:
                new_polymer[new_pair] += count
        polymer = new_polymer
    return polymer


def get_element_counts(polymer: dict[str, int]) -> dict[str, int]:
    """Get the total count for each unique element in the polymer"""
    unique_elements = set("".join(polymer))
    return {
        c: max(
            sum(count for (p1, _), count in polymer.items() if c == p1),
            sum(count for (_, p2), count in polymer.items() if c == p2),
        )
        for c in unique_elements
    }


def get_answer(element_counts: dict[str, int]) -> int:
    """Get the final answer. Subtract minimum count from maximum count"""
    return max(element_counts.values()) - min(element_counts.values())


def run_simulation(polymer: dict[str, int], pairs: dict[str, str], steps: int) -> int:
    """Run the simulation

    'Polymerise' the polymer given the number of steps and pair rules.

    Return the maximum element count minus the minimum element count
    """
    final_polymer = polymerise(polymer, pairs, steps)
    counts = get_element_counts(final_polymer)
    return get_answer(counts)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        polymer, pairs = input.read().split("\n\n")

    polymer = process_polymer(polymer)
    pairs = process_pairs(pairs)

    part_1_ans = run_simulation(polymer, pairs, 10)
    print(part_1_ans)

    part_2_ans = run_simulation(polymer, pairs, 40)
    print(part_2_ans)
