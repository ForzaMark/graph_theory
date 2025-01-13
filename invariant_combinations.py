from invariants import labeled_vertex_invariant, edge_count_invariant, vertex_count_invariant, weisfeiler_lehman_invariant, rank_invariant, vertex_degree_invariant, av_length_invariant, own_weisfeiler_leman_convergence_invariant, own_weisfeiler_leman_one_iteration_invariant

invariant_combinations_without_wl = [
    {
        0: vertex_count_invariant,
    },
    {
        0: vertex_degree_invariant,
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant
    },
    {
        0: vertex_count_invariant,
        1: labeled_vertex_invariant
    },
    {
        0: vertex_degree_invariant,
        1: labeled_vertex_invariant,
    },
    {
        0: edge_count_invariant,
        1: labeled_vertex_invariant,
    },
    {
        0: vertex_degree_invariant,
        1: av_length_invariant,
    },
    {
        0: edge_count_invariant,
        1: vertex_degree_invariant
    },
    {
        0: edge_count_invariant,
        1: av_length_invariant
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: vertex_degree_invariant
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: av_length_invariant
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: labeled_vertex_invariant
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: rank_invariant
    },
    {
        0: vertex_count_invariant,
        1: vertex_degree_invariant,
        2: av_length_invariant
    },
    {
        0: vertex_count_invariant,
        1: vertex_degree_invariant,
        2: labeled_vertex_invariant
    },
    {
        0: rank_invariant,
        1: vertex_count_invariant,
        2: edge_count_invariant,
        3: vertex_degree_invariant,
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: vertex_degree_invariant,
        3: rank_invariant,
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: vertex_degree_invariant,
        3: labeled_vertex_invariant,
    },
    {
        0: vertex_count_invariant,
        1: edge_count_invariant,
        2: vertex_degree_invariant,
        3: av_length_invariant
    }
]

invariant_combinations_with_wl = [{index: func for index, func in (combination.items())} | {len(combination): weisfeiler_lehman_invariant} for combination in invariant_combinations_without_wl]
invariant_combinations_with_own_wl_one_iteration = [{index: func for index, func in (combination.items())} | {len(combination): own_weisfeiler_leman_one_iteration_invariant} for combination in invariant_combinations_without_wl]
invariant_combinations_with_own_wl_convergence = [{index: func for index, func in (combination.items())} | {len(combination): own_weisfeiler_leman_convergence_invariant} for combination in invariant_combinations_without_wl]
only_own_wl_combination = [
    {
        0: own_weisfeiler_leman_convergence_invariant
    },
    {
        0: own_weisfeiler_leman_one_iteration_invariant
    }
]

invariant_combinations = invariant_combinations_without_wl + invariant_combinations_with_wl + invariant_combinations_with_own_wl_one_iteration + invariant_combinations_with_own_wl_convergence + only_own_wl_combination