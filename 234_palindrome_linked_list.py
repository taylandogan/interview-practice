# Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

from data_structures.linked_list import LinkedList

def find_len(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def stack_solution(head):
    # Skip dummy node
    head = head.next
    stack = []
    length = find_len(head)
    if length == 0 or length == 1:
        return True

    i = 0
    while i < length:
        if i < (length//2):
            stack.append(head.value)
            head = head.next
        else:
            if head.value == stack[-1]:
                stack.pop()
            head = head.next
        i += 1

    return not stack

if __name__ == '__main__':
    ll = LinkedList.build_ll_from_list([1, 2, 3, 2, 1])
    print(stack_solution(ll.head))