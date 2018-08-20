# Invert a Binary Tree
# "Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so f*** off."
from data_structures.binary_tree import BinaryTree

def solution(root):
    if not root:
        return root

    tmp_node = root.left
    root.left = root.right
    root.right = tmp_node
    solution(root.left)
    solution(root.right)
    return root


if __name__ == '__main__':
    tree = BinaryTree.build_tree_from_list([4, 2, 7, 1, None, 6, 9])
    BinaryTree.level_order_traversal(tree.root)
    inverted_tree = solution(tree.root)
    BinaryTree.level_order_traversal(inverted_tree)
