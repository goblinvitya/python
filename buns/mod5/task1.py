class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        if self.end is None:
            return None

        val = self.end
        self.end = val.pref
        return val

    def push(self, val):
        node1 = Node(val)
        node1.pref = self.end
        self.end = node1

    def print(self):
        node2 = self.end
        while node2:
            print(node2.data)
            node2 = node2.pref


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.print()
print()
