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

    nx.draw(graph_net, pos=nx.spring_layout(graph_net), with_labels=True)
    plt.show()
