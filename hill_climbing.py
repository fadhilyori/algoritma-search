def hill_climbing_search(graph: dict, start, goal):
    current_node = start
    path = [current_node]
    total_weight = 0

    while current_node != goal:
        neighbors = graph.get(current_node)

        # Check if no more neighbors, then stop climbing
        if not neighbors:
            break

        # Calculate the heuristic value for each neighbor
        heuristic_value = []
        for neighbor, weight in neighbors:
            heuristic_value.append((neighbor, weight + total_weight))

        # Sort the neighbors by their heuristic values in ascending order
        heuristic_value.sort(key=lambda x: x[1])

        # Get the best neighbor with the lowest weight
        best_neighbor, best_weight = heuristic_value[0]

        # Update the current node, path, and total weight
        current_node = best_neighbor
        path.append(current_node)
        total_weight = best_weight

    return path, total_weight


if __name__ == '__main__':
    weighted_graph = {
        'A': [('B', 3), ('L', 5)],
        'B': [('C', 6)],
        'L': [('D', 8)],
        'C': [('D', 3), ('E', 5)],
        'D': [('I', 3)],
        'E': [('F', 2), ('K', 7), ('H', 1), ('I', 8)],
        'I': [('J', 2)],
        'H': [('K', 5), ('J', 3)],
        'F': [('G', 3)],
        'G': [],
        'K': [],
        'J': [],
    }

    start_node = 'A'
    goal_node = 'J'
    path, min_weight = hill_climbing_search(weighted_graph, start_node, goal_node)

    if path[-1] == goal_node:
        print(f"Found a path: {path}")
        print(f"Total Weight: {min_weight}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
