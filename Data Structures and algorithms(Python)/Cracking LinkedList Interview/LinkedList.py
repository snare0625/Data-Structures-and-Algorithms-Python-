from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return "->".join(values)

    def __len__(self):
        node = self.head
        result = 0
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self



#DRIVER CODE
customLL = LinkedList()
customLL.generate(10, 0, 99)
#print(customLL)