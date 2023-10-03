import json
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("Graph Node Visualiation")
    graph_file_path = 'graph_json/soal_ppt.json'

    with open(graph_file_path) as gf:
        graph_json = json.load(gf)

    start_node: str = graph_json["start"]
    goal_node: str = graph_json["goal"]
    graph: dict = graph_json["graph"]

    graph_net = nx.Graph()

    for k in graph.keys():
        current_node = graph[k]

        for edge in current_node:
            graph_net.add_edge(k, edge[0], weight=edge[1])

    pos = nx.spring_layout(graph_net, seed=7)
    edge_labels = nx.get_edge_attributes(graph_net, "weight")

    nx.draw_networkx_nodes(graph_net, pos, node_size=800)
    nx.draw_networkx_edges(graph_net, pos, width=3)
    nx.draw_networkx_edge_labels(graph_net, pos, edge_labels)
    nx.draw_networkx_labels(graph_net, pos, font_size=16, font_family="sans-serif")

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

