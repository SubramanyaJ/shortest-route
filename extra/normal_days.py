import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def reflect_data(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i] = matrix[i][j]
    return matrix

def floyd_warshall(matrix):
    n = len(matrix)
    dist = np.array(matrix, dtype=float)
    dist[dist == -1] = float('inf')
    next_node = [[None if matrix[i][j] == -1 else j for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    return dist, next_node

def reconstruct_path(next_node, start, end):
    if next_node[start][end] is None:
        return []
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path

def plot_shortest_path(matrix, next_node, labels):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j:
                path = reconstruct_path(next_node, i, j)
                if path:
                    G = nx.Graph()
                    for x in range(len(matrix)):
                        for y in range(x + 1, len(matrix)):
                            if matrix[x][y] != -1:
                                G.add_edge(labels[x], labels[y])

                    path_edges = []
                    path_weights = {}
                    for k in range(len(path) - 1):
                        edge = (labels[path[k]], labels[path[k + 1]])
                        path_edges.append(edge)
                        path_weights[edge] = matrix[path[k]][path[k + 1]]

                    pos = nx.spring_layout(G)
                    plt.figure(figsize=(10, 6))

                    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, alpha=0.6)
                    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
                    nx.draw_networkx_edge_labels(G, pos, edge_labels=path_weights, font_size=8)

                    plt.title(f"Shortest Path: {labels[i]} to {labels[j]}")
                    plt.show()

# Original data (with -1 for missing values)
data = [
    [-1, 4, 4, 6, 7, 7, 7, 9],
    [-1, -1, 4, 5, 6, 4, 4, 5],
    [-1, -1, -1, 4, 5, 6, 5, 7],
    [-1, -1, -1, -1, 5, 2, 3, 6],
    [-1, -1, -1, -1, -1, 5, 4, 6],
    [-1, -1, -1, -1, -1, -1, 4, 2],
    [-1, -1, -1, -1, -1, -1, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1, -1]
]

# Reflect data along the diagonal
matrix = reflect_data(data)

# Node labels
labels = [
    "National College", "Ramakrishna Circle", "Tagore Circle",
    "Bull Temple", "NR Colony", "Hanumanthanagar Ward Office",
    "Front Gate", "Back Gate"
]

# Compute shortest paths
shortest_paths, next_node = floyd_warshall(matrix)

# Plot shortest paths for every pair of points
plot_shortest_path(matrix, next_node, labels)
