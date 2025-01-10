from get_reaction_center import get_reaction_center

def find_partition_by_invariant(partitions, reaction_center, invariant_check_function):
    for index, partition in enumerate(partitions):
        partition_representant = partition[0]
        #reaction_center_partition_representant = get_reaction_center(partition_representant)

        if invariant_check_function(reaction_center, partition_representant):
            return index
        
    return False


def create_partitions_by_invariant(reaction_centers, invariant_check_function):
    partitions = []

    for reaction_center in reaction_centers:
        invariant_partition_index = find_partition_by_invariant(partitions, reaction_center, invariant_check_function)

        if type(invariant_partition_index) is int:
            partitions[invariant_partition_index].append(reaction_center)
        else:
            partitions.append([reaction_center])
    
    return partitions