#Three in one

class MultiStack:
    def __init__(self, stackSize):
        self.numberOfStacks = 3
        self.customStack = [0] * (self.numberOfStacks * stackSize)
        self.size = [0] * self.numberOfStacks
        self.stackSize = stackSize

    def isFull(self, stackNum):
        if self.size[stackNum] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stackNum):
        if self.size[stackNum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stackNum):
        offSet = stackNum * self.stackSize
        return offSet + self.size[stackNum] - 1

    def push(self, stackNum, item):
        if self.isFull(stackNum):
            return "The stack is full"
        else:
            self.size[stackNum] += 1
            self.customStack[self.indexOfTop(stackNum)] = item

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return "The stack is Empty"
        else:
            value = self.customStack[self.indexOfTop(stackNum)]
            self.customStack[self.indexOfTop(stackNum)] = 0
            self.size[stackNum] -= 1
            return value