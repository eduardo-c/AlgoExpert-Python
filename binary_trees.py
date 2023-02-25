

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    return root


def bfs(root):
    if not root:
        return
    queue = [root]
    while queue:
        n = queue.pop(0)
        print(n.value, end=" ")
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)


def bfs_test():
    root = build_tree()
    bfs(root)


def node_depths(root):
    if not root:
        return 0
    current_level = [root]
    level = 0
    count = 0
    while current_level:
        next_level = []
        for n in current_level:
            count += level
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        current_level = next_level
        level += 1
    return count


def node_depths_test():
    root = build_tree()
    print(node_depths(root))


def invert_binary_tree(root):
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            aux = node.left
            node.left = node.right
            node.right = aux
            q.append(node.left)
            q.append(node.right)


def invert_binary_tree_test():
    root = build_tree()
    bfs(root)
    print()
    invert_binary_tree(root)
    bfs(root)
