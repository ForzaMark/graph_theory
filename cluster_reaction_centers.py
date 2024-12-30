from get_reaction_center import get_reaction_center
import networkx as nx
import networkx.algorithms.isomorphism as iso
from operator import eq
from math import isclose
from networkx.algorithms.isomorphism import generic_node_match, numerical_edge_match

def cluster_reaction_centers(set_of_reactions):
    partitions = []

    nm = generic_node_match(["charge", "element"], [0, "H"], [isclose, eq])

    # TODO: Perhabs this edge match function is not correct because the instruction says we should use order 
    # instead of standard order here
    # but order is a tuple and it is not clear how tuples should be compared
    em = iso.numerical_edge_match("standard_order", 0)

    for reaction in set_of_reactions:
        
        partition_could_be_found = False
        reaction_its = reaction["ITS"]

        for partition in partitions:
            partition_representant = partition[0]

            rc_reaction = get_reaction_center(reaction_its)
            rc_partition_representant = get_reaction_center(partition_representant)

            if nx.is_isomorphic(rc_reaction, rc_partition_representant, edge_match=em, node_match=nm):
                partition.append(reaction_its)
                partition_could_be_found = True
                break

        if not partition_could_be_found:
            partitions.append([reaction_its])

    return partitions
