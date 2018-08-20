# Merge Two Binary Trees
# Given two binary trees and imagine that
# when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
from data_structures.binary_tree import BinaryTree
import itertools

def solution(t1, t2):
    l1 = BinaryTree.get_list_representation(t1.root)
    l2 = BinaryTree.get_list_representation(t2.root)
    sum_list = [fail_safe_add(x, y) for x, y in itertools.zip_longest(l1, l2, fillvalue=None)]
    return BinaryTree.build_tree_from_list(sum_list)

def fail_safe_add(x, y):
    if x and y:
        return x + y
    elif x:
        return x
    elif y:
        return y
    else:
        return None

def recursive_solution(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.value = fail_safe_add(t1.value, t2.value)
    t1.left = recursive_solution(t1.left, t2.left)
    t1.right = recursive_solution(t1.right, t2.right)
    return t1


if __name__ == '__main__':
    t1 = BinaryTree.build_tree_from_list([1, 3, 2, 5])
    t2 = BinaryTree.build_tree_from_list([2, 1, 3, None, 4, 7])
    # merged_tree = solution(t1, t2)
    # BinaryTree.level_order_traversal(merged_tree.root)
    BinaryTree.level_order_traversal(recursive_solution(t1.root, t2.root))
