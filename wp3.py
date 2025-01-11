import time
from create_partitions_by_invariant import create_partitions_by_invariant
from cluster_reaction_centers import cluster_reaction_centers
from synutility.SynIO.data_type import load_from_pickle
from invariant_combinations import invariant_combinations


def aggregate_charge_and_element_attributes(reaction):
    for node, attributes in reaction.nodes.data():
        attributes["element_charge"] = f"{attributes['element']}{attributes['charge']}"

    return reaction

def load_reactions():
    data = load_from_pickle("C:/Users/Mark/Documents/graph_theory/ITS_graphs.pkl.gz")
    reactions = [reaction["ITS"] for reaction in data]
    reactions = [aggregate_charge_and_element_attributes(reaction) for reaction in reactions]

    return reactions

if __name__ == "__main__":
    reactions = load_reactions()
    partitions = []

    for invariant_config_index, invariant_config in enumerate(invariant_combinations):

        complete_start_time = time.time()

        for invariant_index in range(0, len(invariant_config.values())):
            invariant_check_function = invariant_config[invariant_index]

            if invariant_index == 0:
                partitions = create_partitions_by_invariant(reactions, invariant_check_function)
            else:
                all_sub_partitions = []
                for index, partition in enumerate(partitions):
                    sub_partitions = create_partitions_by_invariant(partition, invariant_check_function)

                    all_sub_partitions = all_sub_partitions + sub_partitions

                partitions = all_sub_partitions

            print(f"{invariant_index}'s partition length = {len(partitions)}")
        
        pre_filtering_end_time = time.time()
        overall_partitions = []

        for pre_filtered_partition in partitions:
            p = cluster_reaction_centers(pre_filtered_partition)
            overall_partitions = overall_partitions + p 

        complete_end_time = time.time()

        complete_elapsed_time = complete_end_time - complete_start_time
        prefiltering_elapsed_time = pre_filtering_end_time - complete_start_time
        print(f"###Invariant Config ###")
        print(invariant_config)

        print(f"Time elapsed pre: {prefiltering_elapsed_time:.2f} seconds")
        print(f"Partitions via invariants found pre: {len(partitions)}")

        print(f"Time elapsed complete: {complete_elapsed_time:.2f} seconds")
        print(f"Partitions finally found: {len(overall_partitions)}")
        print("#########################################")