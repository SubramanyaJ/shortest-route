import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Define the commute time data as adjacency matrices for both cases
# '-' values are represented as 0 (no direct path)
# During Parish
commute_parish = np.array([
    [0, 4, 3, 5, 6, 6, 0, 14],
    [4, 0, 5, 6, 11, 5, 0, 10],
    [3, 5, 0, 6, 6, 8, 0, 10],
    [5, 6, 6, 0, 9, 3, 0, 8],
    [6, 11, 6, 9, 0, 6, 0, 7],
    [6, 5, 8, 3, 6, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [14, 10, 10, 8, 7, 5, 0, 0],
    ])

# Ordinary Days
commute_ordinary = np.array([
    [0, 4, 4, 6, 7, 7, 7, 9],
    [4, 0, 4, 5, 6, 4, 4, 5],
    [4, 4, 0, 4, 5, 6, 5, 7],
    [6, 5, 4, 0, 5, 2, 3, 6],
    [7, 6, 5, 5, 0, 5, 4, 6],
    [7, 4, 6, 2, 5, 0, 4, 2],
    [7, 4, 5, 3, 4, 4, 0, 0],
    [9, 5, 7, 6, 6, 2, 0, 0],
    ])

# Point labels
labels = ["National College", "Ramakrishna Circle", "Tagore Circle", "Bull Temple", "NR Colony",
          "Hanumantha Nagar Ward Office", "Front Gate", "Back Gate"]

# Function to compute shortest paths and visualize them
def compute_and_visualize_shortest_paths(commute_matrix, labels, case_name):
    G = nx.Graph()

    # Add nodes
    for i, label in enumerate(labels):
        G.add_node(i, label=label)

    # Add weighted edges
    for i in range(len(commute_matrix)):
        for j in range(len(commute_matrix)):
            if commute_matrix[i, j] > 0:  # Only add edges with non-zero weights
                G.add_edge(i, j, weight=commute_matrix[i, j])

    # Compute and visualize shortest paths
    for source in range(len(labels)):
        for target in range(len(labels)):
            if source != target:
                try:
                    path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
                    path_edges = list(zip(path, path[1:]))

                    # Draw the graph
                    pos = nx.spring_layout(G)
                    plt.figure(figsize=(12, 8))
                    nx.draw(G, pos, with_labels=True, labels={i: labels[i] for i in range(len(labels))}, node_color='lightblue')
                    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
                    edge_labels = nx.get_edge_attributes(G, 'weight')
                    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

                    plt.title(f"Shortest Path from {labels[source]} to {labels[target]} ({case_name})")
                    plt.savefig(f"shortest_path_{case_name}_{source}_to_{target}.png")
                    plt.close()

                except nx.NetworkXNoPath:
                    print(f"No path between {labels[source]} and {labels[target]} in {case_name} case.")

# Compute shortest paths for both cases
compute_and_visualize_shortest_paths(commute_parish, labels, "during_parish")
compute_and_visualize_shortest_paths(commute_ordinary, labels, "ordinary_days")
