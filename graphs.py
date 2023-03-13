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
        """
        You're given a Node class that has a name and an array of optional children
        nodes. When put together, nodes form an acyclic tree like structure.

        Implement the depth_firsth_search method on the Node class, which takes in an
        empty array, traverses the tree using the Depth-first Search approach
        (specifically navigating the tree from left to right), stores all of the nodes'
        names in the input array, and returns it.

        Sample Input:
                         A
                     /   |   \
                    B    C    D
                   / \        / \
                  E  F       G   H
                    / \       \
                   I  J        K

        Sample Output: ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

        Optimal Space & Time Complexity
        O(v + e) time | O(v) space - where v is the number of vertices of the input
        graph and e is the number of edges of the input graph

        :param array: children array of current node
        :return:
        """
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
    Your're given a list of edges  representing an unweighted, directed graph with at least
    one node. Write a function that returns a boolean representing whether the given graph
    contains a cycle.

    For the purpose of this question, a cycle is defined as any number of vertices, including
    just one vertex, that are connected in a closed chain. A cycle can also be defined as a
    chain of at least one vertex in which the first vertex is the same as the last.

    The given list is what's called an adjacency list, and it represents a graph. The number
    of vertices in the graph is equal to the length of edges, where each index i in edges contains
    vertex i's outbound edges, in no particular order. Each individual edge is represented
    by a positive integer that denotes an index (a destination vertex) in the list that this
    vertex is connected to. Note that these edges are directed, meaning that you can only travel
    from a particular vertex to its destination, not the other way around (unless the destination
    vertex itself has an outbound edge to the original vertex).

    Also note that this graph may contain self-loops. A self-loop is an edge that has the same
    destination and origin; in other words, it's an edge that connects a vertex to itself.
    For the purpose of this question, a self-loop is considered a cycle.

    Sample Input:
    edges  = [
        [1, 3],
        [2, 3, 4],
        [0],
        [],
        [2, 5],
        [],
    ]

    Sample Output: true
    // There are multiple cycles in this graph:
    // 1) 0 -> 1 -> 2 -> 0
    // 2) 0 -> 1 -> 4 -> 2 -> 0
    // 3) 1 -> 2 -> 0 -> 1
    // These are just 3 examples; there are more.

    Optimal Space & Time Complexity
    O(v + e) time | O(v) space - where v is the number of vertices and e is the number of
    edges in the graph

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
