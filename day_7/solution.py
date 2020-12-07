"""
Networkx graph implementation
"""

import re
import networkx as nx
import matplotlib.pyplot as plt


def load_input(file):
    """Load input rules"""

    with open(file, "r") as f:
        raw_rules = f.read().splitlines()

    return raw_rules


def process_rules_into_tuples(raw_rules):

    rules = []
    for rule in raw_rules:
        parent, child = rule[:-1].split("contain")
        parent = parent.replace("bags", "").strip()

        for c in child.split(","):
            pat = "\s(\d+)\s([a-z]+\s[a-z]+)"
            if re.match(pat, c):
                quantity, bag = re.match(pat, c).groups()
                rules.append((parent, bag, int(quantity)))

    return rules


def create_rule_graph(rules):

    DG = nx.DiGraph()
    DG.add_weighted_edges_from(rules)

    return DG


def count_bags_inside(graph, parent):
    total = 0
    for node, edge in graph[parent].items():
        total += edge["weight"] * count_bags_inside(graph, node) + edge["weight"]

    return total


if __name__ == "__main__":
    raw_rules = load_input("input.txt")

    # Part 1
    rules = process_rules_into_tuples(raw_rules)
    graph = create_rule_graph(rules)
    print(len(nx.ancestors(graph, "shiny gold")))

    # Part 2
    print(count_bags_inside(graph, "shiny gold"))
