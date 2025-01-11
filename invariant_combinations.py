from invariants import edge_count_invariant, vertex_count_invariant, weisfeiler_lehman_invariant, rank_invariant, vertex_degree_invariant, global_clustering_invariant, av_length_invariant, graph_diameter_invariant, graph_girth_invariant

invariant_combinations_old = [
    {
        0: edge_count_invariant,
        1: vertex_degree_invariant,
        2: weisfeiler_lehman_invariant
    },
    {
        0: rank_invariant,
        1: vertex_count_invariant,
        2: edge_count_invariant,
        3: vertex_degree_invariant,
        4: weisfeiler_lehman_invariant
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: vertex_degree_invariant,
        3: rank_invariant,
        4: weisfeiler_lehman_invariant
    },
    {
        0: vertex_count_invariant,
        1: weisfeiler_lehman_invariant
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant
    },
    {
        0: vertex_count_invariant,
        1: av_length_invariant,
        2: weisfeiler_lehman_invariant
    },
    {
        0: vertex_degree_invariant,
        1: av_length_invariant,
        2: weisfeiler_lehman_invariant
    }
]

import random

fns_without_wl = [
    edge_count_invariant,
    vertex_count_invariant,
    rank_invariant,
    vertex_degree_invariant,
    global_clustering_invariant,
    av_length_invariant,
    graph_diameter_invariant,
    graph_girth_invariant
]

from itertools import combinations

two_tuples = list(combinations(fns_without_wl, 2))
three_tuples = list(combinations(fns_without_wl, 3))
four_tuples = list(combinations(fns_without_wl, 4))

all_combinations = two_tuples + three_tuples + four_tuples
random.shuffle(all_combinations)

executable_combinations = all_combinations[:20]
with_wl = [combination + (weisfeiler_lehman_invariant,) for combination in all_combinations]

all_combinations = executable_combinations + with_wl
all_combinations = [{index: func for index, func in enumerate(config)} for config in all_combinations]

invariant_combinations = invariant_combinations_old + all_combinations
