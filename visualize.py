import json
import networkx as nx
import matplotlib.pyplot as plt

from matplotlib.pyplot import Axes
from networkx.classes import Graph


def generate_graph(gd: dict) -> Graph:
    gn = nx.Graph()

    for k in gd.keys():
        current_node = gd[k]

        for edge in current_node:
            gn.add_edge(k, edge[0], weight=edge[1])

    return gn


if __name__ == '__main__':
    print("Graph Node Visualiation")
    graph_file_path: str = 'graph_json/soal_ppt.json'

    with open(graph_file_path) as gf:
        graph_json = json.load(gf)

    start_node: str = graph_json["start"]
    goal_node: str = graph_json["goal"]
    graph_dict: dict = graph_json["graph"]

    graph_net: Graph = generate_graph(graph_dict)

    pos: dict = nx.spring_layout(graph_net, seed=7)
    edge_labels: dict = nx.get_edge_attributes(graph_net, "weight")

    nx.draw_networkx_nodes(graph_net, pos, node_size=800)
    nx.draw_networkx_edges(graph_net, pos, width=3)
    nx.draw_networkx_edge_labels(graph_net, pos, edge_labels)
    nx.draw_networkx_labels(graph_net, pos, font_size=16, font_family="sans-serif")

    ax: Axes = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
