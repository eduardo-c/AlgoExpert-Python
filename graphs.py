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

