import json


def hill_climbing_search(graph: dict, start: str, goal: str) -> (list, int):
    current_node = start
    previous_node = start
    path = [current_node]
    total_weight = 0
    iteration_count = 0

    while current_node != goal:
        print(f"#{iteration_count} Current path: {path}")
        neighbors = graph.get(current_node)

        # Check if no more neighbors, then stop climbing
        if not neighbors:
            break

        # Calculate the heuristic value for each neighbor
        heuristic_value = []
        for neighbor, weight in neighbors:
            # Ignore previous visited node
            if neighbor != previous_node:
                heuristic_value.append((neighbor, weight + total_weight))

        # Sort the neighbors by their heuristic values in ascending order
        heuristic_value.sort(key=lambda x: x[1])

        # Get the best neighbor with the lowest weight
        best_neighbor, best_weight = heuristic_value[0]

        # Update the current node, path, and total weight
        previous_node = current_node
        current_node = best_neighbor
        path.append(current_node)
        total_weight = best_weight
        iteration_count += 1

    return path, total_weight


if __name__ == '__main__':
    print("Hill Climbing for Graph")
    graph_file_path = 'graph_json/soal_ppt.json'

    with open(graph_file_path) as gf:
        graph_json = json.load(gf)

    start_node = graph_json["start"]
    goal_node = graph_json["goal"]
    graph = graph_json["graph"]
    solution_path, min_weight = hill_climbing_search(graph, start_node, goal_node)

    if solution_path[-1] == goal_node:
        print(f"\nFound a path: {solution_path}")
        print(f"Total Weight: {min_weight}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
        print(f"Visited path: {solution_path}")
