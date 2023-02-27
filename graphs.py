class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def get_child(self, i):
        return self.children[i]

    def depth_first_search(self, array):
        array.append(self.name)
        for i in self.children:
            i.depth_first_search(array)


def depth_first_search_test():
    g = Node("A")
    g.add_child("B")
    g.add_child("C")
    g.add_child("D")
    g.get_child(0).add_child("E")
    g.get_child(0).add_child("F")
    g.get_child(2).add_child("G")
    g.get_child(2).add_child("H")
    g.get_child(0).get_child(1).add_child("I")
    g.get_child(0).get_child(1).add_child("J")
    g.get_child(2).get_child(0).add_child("K")
    a = []
    g.depth_first_search(a)
    print(a)


NOT_VISITED, VISITED, DISCARDED = 0, 1, 2


def cycle_in_graph(edges):
    """
    :param edges: Adjacency list that represents a graph
    :return: True if any cycle is found on graph, False otherwise
    """
    number_of_nodes = len(edges)
    status = [NOT_VISITED for _ in range(0, number_of_nodes)]
    for node in range(0, number_of_nodes):
        if status[node] != NOT_VISITED:
            continue
        contains_cycle = traverse_node(node, edges, status)
        if contains_cycle:
            return True
    return False


def traverse_node(node, edges, status):
    status[node] = VISITED
    children = edges[node]
    for child in children:
        if status[child] == VISITED:
            return True
        if status[child] != NOT_VISITED:
            continue
        contains_cycle = traverse_node(child, edges, status)
        if contains_cycle:
            return True
    status[node] = DISCARDED
    return False


def cycle_in_graph_test():
    edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
    print(cycle_in_graph(edges))
