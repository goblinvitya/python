class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        node1 = Node(value)
        if self.head is None:
            self.head = node1
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node1

    def get(self, index):
        if index < 0 or self.head is None:
            return None
        curr = self.head
        for i in range(index):
            if curr.next is None:
                return None
            curr = curr.next
        return curr.data

    def remove(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        for i in range(index - 1):
            if curr.next is None:
                return
            curr = curr.next
        if curr.next is None:
            return
        curr.next = curr.next.next

    def insert(self, n, value):
        if n < 0:
            return
        node2 = Node(value)
        if n == 0:
            node2.next = self.head
            self.head = node2
            return
        current = self.head
        for i in range(n - 1):
            if current.next is None:
                return
            current = current.next
        node2.next = current.next
        current.next = node2

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next


list = LinkedList()
list.push(1)
list.push(2)
list.push(3)
list.remove(1)

for i in list:
    print(i)