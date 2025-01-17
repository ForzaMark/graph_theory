import networkx as nx
from math import isclose
import numpy as np
from own_weisfeiler_leman import weisfeiler_leman_one_iteration, hash_distribution_has_changed, weisfeiler_leman_with_convergence

def edge_count_invariant(reaction_center, partition_representant_reaction_center):
    edge_count_reaction_center = len(reaction_center.edges)
    edge_count_partition_representant = len(partition_representant_reaction_center.edges)

    return edge_count_reaction_center == edge_count_partition_representant

def vertex_count_invariant(reaction_center, partition_representant_reaction_center):
    vertex_count_reaction_center = len(reaction_center.nodes)
    vertex_count_partition_representant = len(partition_representant_reaction_center.nodes)

    return vertex_count_reaction_center == vertex_count_partition_representant

def weisfeiler_lehman_invariant(reaction_center, partition_representant_reaction_center):  
    edge_attribute = 'order'
    node_attribute = 'element_charge'

    reaction_center_hash = nx.weisfeiler_lehman_graph_hash(reaction_center, edge_attr=edge_attribute, node_attr=node_attribute, iterations = 1)
    partition_representant_hash = nx.weisfeiler_lehman_graph_hash(partition_representant_reaction_center, edge_attr=edge_attribute, node_attr=node_attribute, iterations = 1)

    return reaction_center_hash == partition_representant_hash

def rank_invariant(reaction_center, partition_representant_reaction_center):
    reaction_center_rank = float(np.linalg.matrix_rank(nx.to_pandas_adjacency(reaction_center).values))
    partition_representant_rank = float(np.linalg.matrix_rank(nx.to_pandas_adjacency(partition_representant_reaction_center).values))

    return isclose(reaction_center_rank, partition_representant_rank, rel_tol=1e-6)

# TODO: check if this implementation for degree invariant is actually correct
def vertex_degree_invariant(reaction_center, partition_representant_reaction_center):
    reaction_center_degrees = sorted([degree for node, degree in list(reaction_center.degree)])
    partition_representant_degrees = sorted([degree for node, degree in list(partition_representant_reaction_center.degree)])

    return reaction_center_degrees == partition_representant_degrees

def av_length_invariant(reaction_center, partition_representant_reaction_center):
    if nx.is_connected(reaction_center) and nx.is_connected(partition_representant_reaction_center):
        avg_path_length_reaction_center = nx.average_shortest_path_length(reaction_center)
        avg_path_length_partition_representant = nx.average_shortest_path_length(partition_representant_reaction_center)

        return isclose(avg_path_length_reaction_center, avg_path_length_partition_representant, rel_tol=1e-6)
    else:
        return True

def global_clustering_invariant(reaction_center, partition_representant_reaction_center):
    global_clustering_reaction_center = nx.transitivity(reaction_center)
    global_clustering_partition_representant = nx.transitivity(partition_representant_reaction_center)

    return isclose(global_clustering_reaction_center,global_clustering_partition_representant , rel_tol=1e-6)

def graph_diameter_invariant(reaction_center, partition_representant_reaction_center):
    if nx.is_connected(reaction_center) and nx.is_connected(partition_representant_reaction_center):
        reaction_center_diameter = nx.diameter(reaction_center)
        partition_representant_reaction_center_diameter = nx.diameter(partition_representant_reaction_center)

        return reaction_center_diameter == partition_representant_reaction_center_diameter
    else:
        return True

def graph_girth_invariant(reaction_center, partition_representant_reaction_center):
    reaction_center_girth = nx.girth(reaction_center)
    partition_representant_reaction_center_girth = nx.girth(partition_representant_reaction_center)

    return reaction_center_girth == partition_representant_reaction_center_girth

def own_weisfeiler_leman_convergence_invariant(reaction_center, partition_representant_reaction_center):
    reaction_center_wl = weisfeiler_leman_with_convergence(reaction_center)["hash"]
    representant_center_wl = weisfeiler_leman_with_convergence(partition_representant_reaction_center)["hash"]

    return not hash_distribution_has_changed(reaction_center_wl, representant_center_wl)

def own_weisfeiler_leman_one_iteration_invariant(reaction_center, partition_representant_reaction_center):
    reaction_center_wl = weisfeiler_leman_one_iteration(reaction_center)["hash"]
    representant_center_wl = weisfeiler_leman_one_iteration(partition_representant_reaction_center)["hash"]

    return not hash_distribution_has_changed(reaction_center_wl, representant_center_wl)