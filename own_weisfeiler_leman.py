def as_count_dict(iteration_hash):
    by_count_dict = {}

    for hash_value, histogram in iteration_hash.items():
        count = histogram["count"]
        if count in by_count_dict:
            by_count_dict[count].append(sorted(histogram["nodes"]))
        else:
            by_count_dict[count] = [sorted(histogram["nodes"])]

    return by_count_dict

def hash_distribution_has_changed(previous_iteration_hash, current_iteration_hash):
    previous_count_dict = as_count_dict(previous_iteration_hash)
    current_count_dict = as_count_dict(current_iteration_hash)

    if previous_count_dict.keys() == current_count_dict.keys():
        for key, previous_nodes in previous_count_dict.items():
            current_nodes = current_count_dict[key]

            for previous_node in previous_nodes:
                if not previous_node in current_nodes:
                    return True
    else: 
        return True
    
    return False

def get_nodes_element_lookup(graph):
    return {node: attributes["element"] for node, attributes in graph.nodes.data()}

def wf_iteration(c, graph):
    element_lookup = get_nodes_element_lookup(graph)

    l = {}
    for node_label in graph.nodes:
        neighbours1 = graph.neighbors(node_label)
        l[node_label] = (
            c[node_label],
            [c[neighbour_label] for neighbour_label in neighbours1],
        )

    c_new = {}
    for key in c.keys():
        l_values = l[key]
        hash_value = hash((l_values[0], tuple(sorted(l_values[1]))))  
        c_new[key] = hash_value
    c = c_new

    hash_dict = {}
    for node, hash_value in c.items():  
        if hash_value not in hash_dict:
            hash_dict[hash_value] = {"count": 0, "nodes": []}
        hash_dict[hash_value]["count"] += 1
        hash_dict[hash_value]["nodes"].append(element_lookup[node])

    return {"graph": graph, "hash": hash_dict, "c": c}


def weisfeiler_leman_one_iteration(graph):
    c = {}
    for node_label in graph.nodes:
        c[node_label] = 1

    return wf_iteration(c, graph)
    

def weisfeiler_leman_with_convergence(graph, index = 0):
    first_iteration = weisfeiler_leman_one_iteration(graph)
    previous_iteration = first_iteration

    for i in range(100):
        c = previous_iteration["c"]
        current_iteration = wf_iteration(c, graph)

        if hash_distribution_has_changed(previous_iteration["hash"], current_iteration["hash"]):
            previous_iteration = current_iteration
        else:
            return current_iteration
        
    print('graph did not converge', index)