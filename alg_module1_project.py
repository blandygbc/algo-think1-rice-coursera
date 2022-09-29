"""
This is Gabriel Blandy's Module 1 Project 1 file
"""
from collections import Counter

# Exemple Graph number 1
EX_GRAPH0 = {0:set([1,2]),
             1:set([]),
             2:set([])}

# Exemple Graph number 2
EX_GRAPH1 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3]),
             3:set([0]),
             4:set([1]),
             5:set([2]),
             6:set([])}

# Exemple Graph number 3
EX_GRAPH2 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3,7]),
             3:set([7]),
             4:set([1]),
             5:set([2]),
             6:set([]),
             7:set([3]),
             8:set([1,2]),
             9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """
    Create a new Graph based on the number of nodes param
    """
    new_digraph = dict()
    if (num_nodes <= 0): 
        return new_digraph
    for column in range(num_nodes):
        in_degrees = set([])
        for row in range(num_nodes): 
            if(row != column): 
                in_degrees.add(row)
        new_digraph[column] = in_degrees
    return new_digraph

def compute_in_degrees(digraph): 
    """ 
    This function return a dictionary with the same set of keys (nodes)
    as digraph whose corresponding values are the number of edges whose 
    head matches a particular node.
    """
    computed_digraph = dict()
    for key in digraph.keys():
        counter = 0
        for values in digraph.values():
            if(key in values): 
                counter+=1
        computed_digraph[key]=counter
    return computed_digraph

def in_degree_distribution(digraph): 
    """ 
    This function return a dictionary whose keys correspond to in-degrees 
    of nodes in the graph. The value associated with each particular 
    in-degree is the number of nodes with that in-degree. In-degrees with 
    no corresponding nodes in the graph are not included in the dictionary.
    """
    new_digraph = dict()
    computed_digraph = compute_in_degrees(digraph)
    for in_degree in computed_digraph.values():
        if in_degree in new_digraph:
            new_digraph[in_degree]+=1
        else:
            new_digraph[in_degree]=1
    if(len(new_digraph.keys())>1):
        sorted_digraph = {key: val for key, val in sorted(new_digraph.items(), key = lambda e: e[0])}
        return sorted_digraph
    else:
        return new_digraph