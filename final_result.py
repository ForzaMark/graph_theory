import time
from create_partitions_by_invariant import create_partitions_by_invariant
from cluster_reaction_centers import cluster_reaction_centers
from invariant_combinations import invariant_combinations
from util import load_reactions
from invariants import own_weisfeiler_leman_convergence_invariant, own_weisfeiler_leman_one_iteration_invariant
import json
import random

def wp2(reactions):
    wp2_start_time = time.time()

    wp2_partitions = cluster_reaction_centers(reactions)

    wp2_end_time = time.time()

    return {
        "partitions_found": len(wp2_partitions),
        "time_elapsed": wp2_end_time - wp2_start_time
    }

def wp3(reactions, invariant_config):
    partitions = []
    partition_development = []

    complete_start_time = time.time()

    for invariant_index in range(0, len(invariant_config.values())):
        invariant_start_time = time.time()
        invariant_check_function = invariant_config[invariant_index]

        if invariant_index == 0:
            partitions = create_partitions_by_invariant(reactions, invariant_check_function)
        else:
            all_sub_partitions = []
            for partition in partitions:
                sub_partitions = create_partitions_by_invariant(partition, invariant_check_function)

                all_sub_partitions = all_sub_partitions + sub_partitions

            partitions = all_sub_partitions
        invariant_end_time = time.time()
        
        partition_development.append({'number_of_partitions': len(partitions), 'time_elapsed_by_this_invariant': invariant_end_time - invariant_start_time})
    
    pre_filtering_end_time = time.time()
    overall_partitions = []

    for pre_filtered_partition in partitions:
        p = cluster_reaction_centers(pre_filtered_partition)
        overall_partitions = overall_partitions + p 

    complete_end_time = time.time()

    complete_elapsed_time = complete_end_time - complete_start_time
    prefiltering_elapsed_time = pre_filtering_end_time - complete_start_time

    return {
        "invariant_config": [(key, value.__name__) for key, value in invariant_config.items()],
        "partition_development": partition_development,
        "prefiltering_elapsed_time": prefiltering_elapsed_time,
        "complete_elapsed_time": complete_elapsed_time,
        "partitions_found": len(overall_partitions)
    }

if __name__ == "__main__":
    reactions = load_reactions()

    #WP2
    wp2_results = wp2(reactions)
    print('########WP2############')
    print(wp2_results)

    # WP3
    print('########WP3############')
    wp3_results = []

    random.shuffle(invariant_combinations)
    for index, invariant_config in enumerate(invariant_combinations):
        print(f"Iteration {index + 1} / {len(invariant_combinations)}")
        current_result = wp3(reactions, invariant_config)
        wp3_results.append(current_result)
    
        with open('tempResult.json', 'w') as fp:
            json.dump({
                "wp2": wp2_results,
                "wp3": wp3_results,
            }, fp)

    with open('result.json', 'w') as fp:
            json.dump({
                "wp2": wp2_results,
                "wp3": wp3_results,
            }, fp)

    

    
        