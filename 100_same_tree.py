# Same Tree
# Given two binary trees, write a function to check if they are the same or not.
from data_structures.binary_tree import BinaryTree

def solution(p, q):
    if p is None and q is None:
        return True
    elif p is None and q is not None:
        return False
    elif p is not None and q is None:
        return False
    else:
        if p.value == q.value:
            return solution(p.left, q.left) and solution(p.right, q.right)
        else:
            return False

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]

    p = BinaryTree.build_tree_from_list(list1)
    q = BinaryTree.build_tree_from_list(list2)
    print("Are trees the same: ", solution(p.root, q.root))