from get_reaction_center import get_reaction_center
import networkx as nx
import networkx.algorithms.isomorphism as iso
from operator import eq
from math import isclose
from networkx.algorithms.isomorphism import generic_node_match, numerical_edge_match

#nm = generic_node_match(["charge", "element"], [0, "H"], [isclose, eq])

# TODO: Perhabs this edge match function is not correct because the instruction says we should use order 
# instead of standard order here
# but order is a tuple and it is not clear how tuples should be compared
#em = iso.numerical_edge_match("standard_order", 0)

def can_find_isomorphic_partition(partitions, reaction_center):
    for index, partition in enumerate(partitions):
        # TODO: mheimer remove 1 index here as well
        #partition_representant = partition[0][1]
        partition_representant = partition[0]

        rc_partition_representant = get_reaction_center(partition_representant)

        if nx.is_isomorphic(reaction_center, 
                            rc_partition_representant, 
                            edge_match=lambda n1, n2: n1["order"] == n2["order"], 
                            node_match=lambda n1, n2: n1["charge"] == n2["charge"] and n1["element"] == n2["element"]):
            return index

    return False


def cluster_reaction_centers(set_of_reactions):
    partitions = []

    # TODO mheimer: remove the enumeration here
    for index, reaction_its in enumerate(set_of_reactions):
        rc_reaction = get_reaction_center(reaction_its)

        isomorphic_partition_index = can_find_isomorphic_partition(partitions, rc_reaction)

        if type(isomorphic_partition_index) is int:
            #partitions[isomorphic_partition_index].append((index, reaction_its))
            partitions[isomorphic_partition_index].append(reaction_its)
        else:
            partitions.append([reaction_its])

    return partitions
