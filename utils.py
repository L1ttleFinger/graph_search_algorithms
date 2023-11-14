import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from search_algorithms import bfs, dfs

graph_dict = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 7, 8, 9],
    4: [1, 10, 11, 12],
    5: [2, 13, 14],
    6: [2, 15, 16],
    7: [3],
    8: [3],
    9: [3],
    10: [4],
    11: [4],
    12: [4],
    13: [5],
    14: [5],
    15: [6],
    16: [6],
}


def generate_graph():
    graph = Graph(graph_dict).graph
    return graph


def graph_search(algorithm, graph, start):
    if algorithm == "Breadth-First Search":
        return bfs(graph, start)
    elif algorithm == "Depth-First Search":
        return dfs(graph, start)
    else:
        return bfs(graph, start)


def plot_graph(graph, color_map, plot_holder):
    G = nx.Graph(graph)
    pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", args="")
    nx.draw(G, pos, node_size=500, node_color=color_map, with_labels=True)
    plot_holder.pyplot()


def run_visualization(algorithm, graph, plot_holder, start, step_duration=0.5):
    visited = graph_search(algorithm, graph, start)
    n = len(visited)
    for i in range(n):
        color_map = []
        for node in graph:
            if node in visited[:i]:
                color_map.append("lightgreen")
            elif node == visited[i]:
                color_map.append("cyan")
            else:
                color_map.append("lightgray")
        plot_graph(graph, color_map, plot_holder)
        plt.pause(step_duration)
    plot_graph(graph, "lightgreen", plot_holder)
