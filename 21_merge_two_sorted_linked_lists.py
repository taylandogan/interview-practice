# Merge Two Sorted Linked Lists
# Merge two sorted linked lists and return it as a new list.
from data_structures.linked_list import Node, LinkedList

def insertTo(head, tail, val):
    new_node = Node(val)
    if not head:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = tail.next
    return head, tail

def solution(l1, l2):
    if not l1 and not l2:
        return None
    if not l1:
        return l2
    if not l2:
        return l1

    head, tail = None, None
    while l1 and l2:
        if (l1.val < l2.val):
            head, tail = insertTo(head, tail, l1.val)
            l1 = l1.next
        else:
            head, tail = insertTo(head, tail, l2.val)
            l2 = l2.next

    if l1:
        while l1:
            head, tail = insertTo(head, tail, l1.val)
            l1 = l1.next

    if l2:
        while l2:
            head, tail = insertTo(head, tail, l2.val)
            l2 = l2.next

    return head

if __name__ == '__main__':
    list1 = [1, 2]
    list2 = [1, 2, 3, 4]
    l1 = LinkedList.build_ll_from_list(list1)
    l2 = LinkedList.build_ll_from_list(list2)
    merged_head = solution(l1.head, l2.head)
    merged = LinkedList(merged_head)
    merged.print_ll()