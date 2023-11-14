import networkx as nx
import matplotlib.pyplot as plt

graph_dict = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8, 9],
    4: [10, 11, 12],
    5: [13, 14],
    6: [15, 16],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
}


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph = graph_dict


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


def bfs(graph, start):
    queue = [start]
    visited = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


def graph_search(algorithm, graph, start):
    if algorithm == "Breadth-First Search":
        return bfs(graph, start)
    elif algorithm == "Depth-First Search":
        return dfs(graph, start)
    else:
        return bfs(graph, start)


def generate_graph():
    graph = Graph(graph_dict).graph
    return graph


def plot_graph(graph, color_map, plot_holder):
    G = nx.Graph(graph)
    pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", args="")
    nx.draw(G, pos, node_size=500, node_color=color_map, with_labels=True)
    plot_holder.pyplot()


def run_search(algorithm, graph, plot_holder, start):
    visited = graph_search(algorithm, graph, start)
    n = len(visited)
    for i in range(n + 1):
        color_map = []
        for node in graph:
            if node in visited[:i]:
                color_map.append("lightgreen")
            elif node == visited[i]:
                color_map.append("cyan")
            else:
                color_map.append("lightgray")
        plot_graph(graph, color_map, plot_holder)
        if i < n:
            plt.pause(0.6)
