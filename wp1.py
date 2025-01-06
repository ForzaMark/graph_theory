from synutility.SynVis.graph_visualizer import GraphVisualizer
from synutility.SynVis.graph_visualizer import GraphVisualizer
import matplotlib.pyplot as plt
import networkx as nx

from synutility.SynIO.data_type import load_from_pickle

from get_reaction_center import get_reaction_center
from visualize_graph import visualize_graph

def examine_graph(its_graph):
    print(its_graph.edges)
    print(its_graph.nodes)

    print(its_graph.edges.data())
    print(its_graph.nodes.data())

if __name__ == "__main__":
    data = load_from_pickle("/home/mark/Documents/graph_theory/ITS_graphs.pkl.gz")

    fig, ax = plt.subplots(2, 1, figsize = (25, 20 ))
    vis = GraphVisualizer ()

    reaction = data[600]

    reaction_center = get_reaction_center(reaction["ITS"])

    visualize_graph(reaction["ITS"], with_reaction_center=True)