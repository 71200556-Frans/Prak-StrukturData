class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.root.insert(data)

    def countGenap(self, node):
        if node is None:
            return 0

        count_left = self.countGenap(node.left)
        count_right = self.countGenap(node.right)

        if node.data % 2 == 0:
            return 1 + count_left + count_right
        else:
            return count_left + count_right

    def hasilGenap(self):
        return self.countGenap(self.root)

if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)

    print("Penjumlahan Data Genap:", binaryT.hasilGenap())
