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
