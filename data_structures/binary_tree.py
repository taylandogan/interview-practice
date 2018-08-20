from collections import deque

class TreeNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def add_left_child(self, val):
        l = TreeNode(val)
        self.left = l

    def add_right_child(self, val):
        r = TreeNode(val)
        self.right = r

    def print_node(self):
        if self.value:
            print(self.value)
        else:
            print('None')


class BinaryTree:

    def __init__(self, t):
        self.root = t

    @staticmethod
    def fromlist(node, l, index):
        if index < len(l):
            if l[index]:
                node.value = l[index]
                if len(l) > (index * 2):
                    node.add_left_child(l[index * 2])
                if len(l) > (1 + (index * 2)):
                    node.add_right_child(l[1 + (index * 2)])
                BinaryTree.fromlist(node.left, l, index * 2)
                BinaryTree.fromlist(node.right, l, index * 2 + 1)

        return node

    @staticmethod
    def build_tree_from_list(l):
        root = TreeNode(-1)
        if l:
            # Add dummy element to the front
            l = [None] + l
            BinaryTree.fromlist(root, l, 1)
        else:
            return BinaryTree(None)
        return BinaryTree(root)

    @staticmethod
    def preorder_traversal(root):
        if root:
            print(root.value)
            BinaryTree.preorder_traversal(root.left)
            BinaryTree.preorder_traversal(root.right)

    @staticmethod
    def inorder_traversal(root):
        if root:
            BinaryTree.inorder_traversal(root.left)
            print(root.value)
            BinaryTree.inorder_traversal(root.right)

    @staticmethod
    def postorder_traversal(root):
        if root:
            BinaryTree.postorder_traversal(root.left)
            BinaryTree.postorder_traversal(root.right)
            print(root.value)

    @staticmethod
    def level_order_traversal(root):
        result = []
        q = deque([])
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                result.append(node.value)
                q.append(node.left)
                q.append(node.right)
        print(result)
        return result

    @staticmethod
    def get_list_representation(root):
        res = BinaryTree.level_order_traversal(root)
        return res


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    btree = BinaryTree.build_tree_from_list(a)
    BinaryTree.postorder_traversal(btree.root)
    print("List rep: ", BinaryTree.get_list_representation(btree.root))