import time
from create_partitions_by_invariant import create_partitions_by_invariant
from cluster_reaction_centers import cluster_reaction_centers
from synutility.SynIO.data_type import load_from_pickle
from invariant_combinations import invariant_combinations
from invariants import edge_count_invariant, vertex_count_invariant, weisfeiler_lehman_invariant, rank_invariant, vertex_degree_invariant, global_clustering_invariant, av_length_invariant, graph_diameter_invariant, graph_girth_invariant
from get_reaction_center import get_reaction_center

def aggregate_charge_and_element_attributes(reaction):
    for node, attributes in reaction.nodes.data():
        attributes["element_charge"] = f"{attributes['element']}{attributes['charge']}"

    return reaction

def load_reaction_centers():
    data = load_from_pickle("C:/Users/Mark/Documents/graph_theory/ITS_graphs.pkl.gz")
    reactions = [reaction["ITS"] for reaction in data]
    reaction_centers = [get_reaction_center(reaction) for reaction in reactions]
    reaction_centers = [aggregate_charge_and_element_attributes(reaction) for reaction in reaction_centers]

    return reaction_centers

if __name__ == "__main__":
    reaction_centers = load_reaction_centers()
    partitions = []

    invariant_config = [
        rank_invariant,
        vertex_count_invariant,
        edge_count_invariant,
        vertex_degree_invariant,
        weisfeiler_lehman_invariant
    ]
        
    start_time = time.time()

    for invariant_index, invariant_check_function in enumerate(invariant_config):
        print('parititions length at invariant index', invariant_index,  len(partitions))

        if invariant_index == 0:
            partitions = create_partitions_by_invariant(reaction_centers, invariant_check_function)
        else:
            all_sub_partitions = []
            for index, partition in enumerate(partitions):
                
                sub_partitions = create_partitions_by_invariant(partition, invariant_check_function)

                all_sub_partitions = all_sub_partitions + sub_partitions

            partitions = all_sub_partitions

        print(f"{invariant_index}'s partition length = {len(partitions)}")

    overall_partitions = []

    for pre_filtered_partition in partitions:
        p = cluster_reaction_centers(pre_filtered_partition)
        overall_partitions = overall_partitions + p 

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

    print(f"Partitions via invariants found: {len(partitions)}")
    print(f"Partitions finally found: {len(overall_partitions)}")