# Reverse Linked List
# Reverse a singly linked list.
from data_structures.linked_list import LinkedList

def solution(ll):
    prev = None
    cur = ll.head
    if not cur:
        return ll

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return LinkedList(prev)


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    ll = LinkedList.build_ll_from_list(l)
    print("Before: ")
    ll.print_ll()
    reversed_ll = solution(ll)
    print("After: ")
    reversed_ll.print_ll()
