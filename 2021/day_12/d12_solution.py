"""Day 12 Solution"""
import networkx as nx


def create_graph(edges: list[str]) -> nx.Graph:
    g = nx.Graph()
    edge_list = list(map(lambda x: x.split("-"), edges))
    g.add_edges_from(edge_list)
    return g


def find_paths(
    graph: nx.Graph, s: str = "start", seen: set[str] = {"start"}, p2: bool = False
) -> int:
    if s == "end":
        return 1
    paths = 0
    for neighbor in graph.neighbors(s):
        if neighbor.islower():
            if neighbor not in seen:
                paths += find_paths(graph, neighbor, seen | {neighbor}, p2)
            elif p2 and neighbor not in {"start", "end"}:
                paths += find_paths(graph, neighbor, seen | {neighbor}, False)
        else:
            paths += find_paths(graph, neighbor, seen, p2)
    return paths


def part_1(graph: nx.Graph) -> int:
    return find_paths(graph)


def part_2(graph: nx.Graph) -> int:
    return find_paths(graph, p2=True)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        edges = input.read().splitlines()

    graph = create_graph(edges)

    part_1_ans = part_1(graph)
    print(part_1_ans)

    part_2_ans = part_2(graph)
    print(part_2_ans)
