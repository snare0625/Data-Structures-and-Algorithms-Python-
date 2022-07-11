class Stack:
    def __init__(self):
        self.list = []

    def __repr__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #Push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully added"

    #pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    def deleteStack(self):
        self.list = None


def equalStacks(h1, h2, h3):
    s1, s2, s3 = map(sum, (h1, h2, h3))
    while h1 and h2 and h3:
        m = min(s1, s2, s3)
        if s1 > m:
            s1 -= h1.pop()
        if s2 > m:
            s2 -= h2.pop()
        if s3 > m:
            s3 -= h3.pop()
    if s1 == s2 == s3:
        return s1
    else:
        return 0


h1 = Stack()
h1.push(1)
h1.push(1)
h1.push(1)
h1.push(2)
h1.push(3)
print(h1)
print()

h2 = Stack()
h2.push(2)
h2.push(3)
h2.push(4)
print(h2)
print()
h3 = Stack()
h3.push(1)
h3.push(4)
h3.push(1)
h3.push(1)
print(h3)

equalStacks(h1, h2, h3)