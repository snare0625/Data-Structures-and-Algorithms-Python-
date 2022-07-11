class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    #O(N)
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of the queue"

    #O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

#DRIVER CODE
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)

