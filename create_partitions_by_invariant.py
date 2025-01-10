from get_reaction_center import get_reaction_center

def find_partition_by_invariant(partitions, reaction_center, invariant_check_function):
    for index, partition in enumerate(partitions):
        # TODO mheimer: remove 1 index when not using enumerate anmore for debugging

        #partition_representant = partition[0][1]
        partition_representant = partition[0]
        reaction_center_partition_representant = get_reaction_center(partition_representant)

        if invariant_check_function(reaction_center, reaction_center_partition_representant):
            return index
        
    return False


def create_partitions_by_invariant(reactions, invariant_check_function):
    partitions = []

    for reaction_its in reactions:

        # TODO mheimer: remove 1 index when not using enumerate anmore for debugging
        #reaction_center = get_reaction_center(reaction_its[1])
        reaction_center = get_reaction_center(reaction_its)
        invariant_partition_index = find_partition_by_invariant(partitions, reaction_center, invariant_check_function)

        if type(invariant_partition_index) is int:
            partitions[invariant_partition_index].append(reaction_its)
        else:
            partitions.append([reaction_its])
    
    return partitions