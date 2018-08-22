class Node:

    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:

    def __init__(self, head):
        self.head = head
        self.tail = head

    def insert_to_head(self, val):
        # Insert node
        new_node = Node(val)
        tmp = self.head.next
        self.head.next = new_node
        new_node.next = tmp
        # Move tail
        self.tail = tail.next

    def insert_to_tail(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def print_ll(self):
        # Skip the dummy node
        ptr = self.head.next
        while ptr:
            print(ptr.value)
            ptr = ptr.next

    @staticmethod
    def build_ll_from_list(l):
        dummy_node = Node(-1)
        ll = LinkedList(dummy_node)
        for elem in l:
            ll.insert_to_tail(elem)
        return ll


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    ll = LinkedList.build_ll_from_list(l)
    ll.print_ll()