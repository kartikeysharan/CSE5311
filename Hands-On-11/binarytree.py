class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        traversal = []
        self._inorder_traversal_recursive(self.root, traversal)
        return traversal

    def _inorder_traversal_recursive(self, node, traversal):
        if node:
            self._inorder_traversal_recursive(node.left, traversal)
            traversal.append(node.key)
            self._inorder_traversal_recursive(node.right, traversal)

# Example usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder traversal:", bst.inorder_traversal())  # Output: [1, 3, 4, 5, 6, 7, 8]
print("Search 6:", bst.search(6))  # Output: True
print("Search 2:", bst.search(2))  # Output: False
