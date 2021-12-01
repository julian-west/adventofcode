"""
Networkx graph implementation
"""

import re

import networkx as nx


def load_input(file: str) -> list:
    """Load input rules into list of strings"""

    with open(file, "r") as f:
        raw_rules = f.read().splitlines()

    return raw_rules


def create_edge_list(raw_rules: list) -> list:
    """Create an edge list for the graph

    Converts list of string rules into edge list (list of tuples)

    create_edge_list(["bright indigo bags contain 4 shiny turquoise bags, 3 wavy yellow bags."])
    >>> [ ('bright indigo','shiny turquoise', 4), ('bright indigo','wavy yellow',3) ]

    """
    rules = []
    for rule in raw_rules:
        parent, child = rule[:-1].split("contain")
        parent = parent.replace("bags", "").strip()

        for c in child.split(","):
            pat = r"\s(\d+)\s([a-z]+\s[a-z]+)"
            if re.match(pat, c):
                quantity, bag = re.match(pat, c).groups()
                rules.append((parent, bag, int(quantity)))

    return rules


def create_rule_graph(edge_list: list) -> nx.DiGraph:
    """Create graph encoding the rules from a list of tuples (edge list)"""

    DG = nx.DiGraph()
    DG.add_weighted_edges_from(edge_list)
    return DG


def count_bags_inside(graph: nx.DiGraph, parent: str) -> int:
    """Recursively count how many bags would be contained within any given bag"""
    total = 0
    for node, edge in graph[parent].items():
        total += edge["weight"] * count_bags_inside(graph, node) + edge["weight"]

    return total


if __name__ == "__main__":
    raw_rules = load_input("input.txt")

    # Part 1
    rules = create_edge_list(raw_rules)
    graph = create_rule_graph(rules)
    print(len(nx.ancestors(graph, "shiny gold")))

    # Part 2
    print(count_bags_inside(graph, "shiny gold"))
