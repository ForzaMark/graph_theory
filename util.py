from synutility.SynIO.data_type import load_from_pickle

def aggregate_charge_and_element_attributes(reaction):
    for node, attributes in reaction.nodes.data():
        attributes["element_charge"] = f"{attributes['element']}{attributes['charge']}"

    return reaction

def load_reactions(path = "./ITS_graphs.pkl.gz"):
    data = load_from_pickle(path)
    reactions = [reaction["ITS"] for reaction in data]
    reactions = [aggregate_charge_and_element_attributes(reaction) for reaction in reactions]

    return reactions