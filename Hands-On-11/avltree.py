class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _fix_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self._fix_height(node)
        self._fix_height(new_root)

        return new_root

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self._fix_height(node)
        self._fix_height(new_root)

        return new_root

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)

        self._fix_height(node)

        balance = self._balance(node)

        # Left-Left case
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        # Right-Right case
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        # Left-Right case
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right-Left case
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

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
avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(15)
avl_tree.insert(25)

print("Inorder traversal:", avl_tree.inorder_traversal())  # Output: [10, 15, 20, 25, 30]
