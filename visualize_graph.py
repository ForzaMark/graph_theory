from synutility.SynVis.graph_visualizer import GraphVisualizer
import matplotlib.pyplot as plt
from get_reaction_center import get_reaction_center, get_reaction_center_old

def visualize_graph(its_graph, with_reaction_center = True):
    fig, ax = plt.subplots(2, 1, figsize = (25, 20 ))
    vis = GraphVisualizer()

    vis.plot_its(its_graph, ax[0], use_edge_color=True)

    if with_reaction_center:
        reaction_center = get_reaction_center(its_graph)
        vis.plot_its(reaction_center, ax[1], use_edge_color=True)