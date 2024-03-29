class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        curr_node = self.head
        while True:
            if curr_node.next_node is None:
                curr_node.next_node = node
                break
            curr_node = curr_node.next_node

    def delete(self, value):
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next_node
            if curr_node.value == value:
                last_node.next_node = curr_node.next_node
                return 

    def printLL(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value, end =" -> ")
            curr_node = curr_node.next_node
        print(None)
    def delete_mid(self, pos):
        node = self.head
        c = 0
        while node and c != pos:
            node = node.next_node
            c += 1

        if not node or not node.next_node:
            return False

        nxt = node.next_node
        node.value = nxt.value
        node.next_node = nxt.next_node
        return True

    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_node
        return count

    def remove_n_node(self, n):
        curr_node = self.head
        tail = self.length()
        stop = tail - n 
        c = 0
        while curr_node and c != stop:
            curr_node = curr_node.next_node
            c += 1

        if not curr_node or not curr_node.next_node:
            return False

        nxt = curr_node.next_node
        curr_node.value = nxt.value
        curr_node.next_node = nxt.next_node
        return True

l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.remove_n_node(2)
l1.printLL()


