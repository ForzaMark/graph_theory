from invariants import edge_count_invariant, vertex_count_invariant, weisfeiler_lehman_invariant, rank_invariant, vertex_degree_invariant, global_clustering_invariant, av_length_invariant, graph_diameter_invariant, graph_girth_invariant

invariant_combinations = [
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
        0: global_clustering_invariant
    }
]

# Global Clustering = 7 
# Average Length = 52
# Girth = 8
# Diameter = 7
