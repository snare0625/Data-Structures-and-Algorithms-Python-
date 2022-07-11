class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in LinkedList
    def insertSLL(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head = node
            elif location == 1:
                node.next = None
                self.tail.next = node
                self.tail = node
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = node
                node.next = nextNode
    #traverse Singly Linked List
    def traverseSLL(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    #search for a node in a singly linked list
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
                return "The value does not exist in the list"

    #delete node
    def deleteNode(self, location):
        if self.head is None:
            print("SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next

    #Delete entire SLL
    def deleteEntireSll(self):
        if self.head is None:
            print("SLL does not exist.")
        else:
            self.head = None
            self.tail = None









#DRIVER CODE
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
#singlyLinkedList.traverseSLL()
#print(singlyLinkedList.searchSLL(2))
#print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(1)
print([node.value for node in singlyLinkedList])


