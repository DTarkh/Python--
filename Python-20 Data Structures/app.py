# მოიძიეთ ინფორმაცია ბინარულ ხეზე და დაწერეთ დაბეჭდვის
# ფუნქციები printLeafNodes და countEdges


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node


def printLeafNodes(root):

    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.key)

    if root.left:
        printLeafNodes(root.left)
    if root.right:
        printLeafNodes(root.right)


def countEdges(root):

    if root is None:
        return 0

    edges = 0

    if root.left:
        edges += 1 + countEdges(root.left)

    if root.right:
        edges += 1 + countEdges(root.right)
        
    return edges


tree = BinaryTree()
tree.insert(10)
tree.insert(12)
tree.insert(15)
tree.insert(17)
tree.insert(8)

print("Leaf nodes of the tree are: ")
printLeafNodes(tree.root)


print("Number of edges in the tree: ", countEdges(tree.root))
