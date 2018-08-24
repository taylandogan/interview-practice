class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, head):
        self.head = head
        self.tail = head

    def insert_to_head(self, val):
        # Insert node
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_to_tail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def print_ll(self):
        ptr = self.head
        while ptr:
            print(ptr.val)
            ptr = ptr.next

    def insert_val_on_index(self, index, val):
        pass

    def insert_dummy_to_head(self):
        self.insert_to_head(-1)

    @staticmethod
    def build_ll_from_list(l):
        ll = LinkedList(None)
        for elem in l:
            ll.insert_to_tail(elem)
        return ll


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    ll = LinkedList.build_ll_from_list(l)
    ll.print_ll()