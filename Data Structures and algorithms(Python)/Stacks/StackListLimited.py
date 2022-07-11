class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # Push
    def push(self, value):
        if self.isFull():
            return "The Stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully added"


    #peek
    def peek(self):
        if self.isEmpty():
            return "The is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    #pop
    def pop(self):
        if self.isEmpty():
            return "The is not any element in the stack"
        else:
            self.list.pop()
