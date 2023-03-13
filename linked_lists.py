class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        next_node = Node(value)
        if self.head is None:
            self.head = next_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)

    def traverse(self):
        values = [self.head.value]
        next_node = self.head.next
        while next_node:
            values.append(next_node.value)
            next_node = next_node.next
        print(values)


def linked_list_traverse_test():
    ll = LinkedList(5)
    ll.append(2)
    ll.append(8)
    ll.append(10)
    ll.append(1)
    ll.traverse()


def remove_duplicates(ll):
    """
    You're given the head of a Singly Linked List whose nodes are in sorted order with
    respect to their values. Write a function that returns a modified version of the Linked
    List that doesn't contain any nodes with duplicate values. The Linked List should be
    modified in place (i.e., you shouldn't create a brand new list), and the modified
    Linked List should still have its nodes sorted with respect to their values.

    Each LinkedList node has an integer value as well as a next node pointing to the next
    node in the list or to Nonde if it's the tail of the list

    Sample Input:
    linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

    Sample Output:
    1 -> 3 -> 4 -> 5 -> 6 // the head node with value 1

    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the number of nodes in the Linked List

    :param ll: instance of LinkedList
    :return:
    """
    if not ll.head:
        return
    nn = ll.head
    while nn:
        aux = nn.value
        while nn.next and nn.next.value == aux:
            nn.next = nn.next.next
        nn = nn.next


def linked_list_remove_duplicates_test():
    ll = LinkedList(1)
    ll.append(1)
    ll.append(3)
    ll.append(4)
    ll.append(4)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(6)
    ll.traverse()
    remove_duplicates(ll)
    ll.traverse()
