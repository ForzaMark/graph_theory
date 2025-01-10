from synutility.SynIO.data_type import load_from_pickle
import networkx as nx
from math import isclose
import time
import numpy as np
from synutility.SynIO.data_type import load_from_pickle
import networkx as nx
from math import isclose
import time
import numpy as np
from create_partitions_by_invariant import create_partitions_by_invariant
from cluster_reaction_centers import cluster_reaction_centers
from get_reaction_center import get_reaction_center
from create_partitions_by_invariant import create_partitions_by_invariant
from cluster_reaction_centers import cluster_reaction_centers
import pickle
from visualize_graph import visualize_graph


def aggregate_charge_and_element_attributes(reaction):
    for node, attributes in reaction.nodes.data():
        attributes["element_charge"] = f"{attributes['element']}{attributes['charge']}"

    return reaction
data = load_from_pickle("C:/Users/jwins/OneDrive/Bilder/Dokumente/graph_theory/ITS_graphs.pkl.gz")

print("Done loading data.")
reactions = [reaction["ITS"] for reaction in data]
reactions = [aggregate_charge_and_element_attributes(reaction) for reaction in reactions]
reaction_centers = [get_reaction_center(reaction) for reaction in reactions]

def weisfeiler_leman_1_new(graph):

    c1 = {}
    for node_label in graph.nodes:
        c1[node_label] = 1 

    for iteration in range(1): 
        l1 = {}
        for node_label in graph.nodes:
            neighbours1 = graph.neighbors(node_label)
            l1[node_label] = (
                c1[node_label],
                [c1[neighbour_label] for neighbour_label in neighbours1],
            )
        c1_new = {}
        for key in c1.keys():
            l1_values = l1[key]
            h1 = hash((l1_values[0], tuple(sorted(l1_values[1]))))  
            c1_new[key] = h1
        c1 = c1_new
    # Histogramm der Hash-Werte
    hash_dict = {}
    for node, h in c1.items():  
        if h not in hash_dict:
            hash_dict[h] = {"count": 0, "nodes": []}
        hash_dict[h]["count"] += 1
        hash_dict[h]["nodes"].append(node)
    #print({"graph": graph, "hash": hash_dict})
    return {"graph": graph, "hash": hash_dict}
def weisfeiler_leman_2_new(reaction_center1, reaction_center2):
    c1, c2 = {}, {}

    for node_label in reaction_center1.nodes:
        c1[node_label] = 1
    for node_label in reaction_center2.nodes:
        c2[node_label] = 1

    for iteration in range(1, 3):
        l1, l2 = {}, {}

        for node_label in reaction_center1.nodes:
            neighbours1 = reaction_center1.neighbors(node_label)
            l1[node_label] = (c1[node_label], [c1[neighbour_label] for neighbour_label in neighbours1])

        for node_label in reaction_center2.nodes:
            neighbours2 = reaction_center2.neighbors(node_label)
            l2[node_label] = (c2[node_label], [c2[neighbour_label] for neighbour_label in neighbours2])

        c1_new, c2_new = {}, {}

        for key in c1.keys():
            l1_values = l1[key]
            h1 = hash((l1_values[0], tuple(sorted(l1_values[1]))))  # Sortierte Nachbarn für Konsistenz
            c1_new[key] = h1
        
        for key in c2.keys():
            l2_values = l2[key]
            h2 = hash((l2_values[0], tuple(sorted(l2_values[1]))))  # Sortierte Nachbarn für Konsistenz
            c2_new[key] = h2

        c1, c2 = c1_new, c2_new
    
    # Extrahiere die Hash-Werte
    hashes_c1 = set(c1.values())
    hashes_c2 = set(c2.values())

    # Schnittmenge der Hashes
    common_hashes = hashes_c1.intersection(hashes_c2)

    print("Gemeinsame Hashes:", common_hashes)

    # Rückgabe, ob es irgendeinen gemeinsamen Hash gibt
    return len(common_hashes) > 0
def run_weisfeiler_leman_for_all_new(graphs, output_file='wl_results.pkl'):
    result_list = []
    for graph in graphs:
        wl_result = weisfeiler_leman_1_new(graph)
        result_list.append(wl_result)
    print(result_list)
    return result_list
visualize_graph(reaction_centers[0])
visualize_graph(reaction_centers[1])
visualize_graph(reaction_centers[2])
visualize_graph(reaction_centers[3])
visualize_graph(reaction_centers[4])
run_weisfeiler_leman_for_all_new(reaction_centers[0:4])