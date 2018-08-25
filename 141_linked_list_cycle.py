# Linked List Cycle
# Given a linked list, determine if it has a cycle in it.

def solution(head):
    slow, fast = head, head
    while slow and fast:
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
        else:
            return False
        if slow and fast:
            if slow.val == fast.val:
                return True
    return False

def solution2(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False