class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.last = None
        self.head = None
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def push(self, val):
        if self.last is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = None
            self.last.next.prev = self.last
            self.last = self.last.next
        pass

    def insert(self, n, val):
        if n == 0:
            node1 = Node(val)
            node1.next = self.head
            if self.head:
                self.head.prev = node1
            self.head = node1
        else:
            curr = self.head
            index = 0
            while curr is not None and index < n - 1:
                curr = curr.next
                index += 1
            if curr is None:
                return
            node1 = Node(val)
            node1.prev = curr
            node1.next = curr.next
            if curr.next:
                curr.next.prev = node1
            curr.next = node1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next