import networkx as nx

def get_reaction_center(its_graph):
    reaction_center_edges = [edge for edge in its_graph.edges.data() if edge[2]["standard_order"] != 0]

    reaction_center_nodes = set()

    for start_node, end_node, order_info in reaction_center_edges:
        reaction_center_nodes.add(start_node)
        reaction_center_nodes.add(end_node)

    return nx.induced_subgraph(its_graph, reaction_center_nodes)
