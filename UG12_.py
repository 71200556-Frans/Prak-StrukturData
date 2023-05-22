class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class Tree:
    def __init__(self, root):
        self.root = root

    def sums(self, node):
        if node is None:
            return 0

        total = node.data
        for child in node.children:
            total += self.sums(child)

        return total

    def sibling(self, node):
        if node is None or node is self.root:
            return 0

        parent = self.find_parent(node)
        total = 0
        for child in parent.children:
            if child is not node:
                total += child.data

        return total

    def find_parent(self, node):
        if node is None or node is self.root:
            return None

        for child in self.root.children:
            if node in child.children:
                return child

        return None


# Struktur tree sesuai testcase
val200 = Node(200)
val5 = Node(5)
val7 = Node(7)
val2 = Node(2)
val3 = Node(3)
val4 = Node(4)
val8 = Node(8)
val33 = Node(33)
val99 = Node(99)

val200.add_child(val5)
val200.add_child(val7)
val5.add_child(val2)
val5.add_child(val3)
val7.add_child(val4)
val7.add_child(val8)
val8.add_child(val33)
val33.add_child(val99)

t = Tree(val200)

# Testcase 1
print(f'Total value of node {val200.data} and all of its descendants = {t.sums(val200)}')

# Testcase 2
print(f'Total value of all siblings of node {val33.data} = {t.sibling(val33)}')
