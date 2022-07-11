class Node:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    #Creation of CircularDoublyLinkedList
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode

    #insertion in CDLL
    def insertNode(self, nodeValue,location):
        if self.head is None:
            return "The head reference is none"
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                newNode.next = nextNode
                newNode.prev = currentNode
                nextNode.prev = newNode
                currentNode.next = newNode
            return "The node has been successfully added"

    def traverseCDLL(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            if currentNode == self.tail:
                break
            currentNode = currentNode.next

    #Reverse traversal for CCDLL
    def reverseTraversaCDLL(self):
        if self.head is None:
            return "There is not any element in the CDLL"
        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.value)
                if currentNode == self.head:
                    break
                currentNode = currentNode.prev

    #Search CDLL
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is not any element in the CDLL"
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.value == nodeValue:
                    return currentNode.value
                if currentNode == self.tail:
                    return "The value does not exist in CDLL"
                currentNode = currentNode.next

    #delete a node from a CDLL
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node in the CDLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.head.next = self.tail
                    self.tail.next = self.head
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("The node has been successfully added")

    #delete entire CDLL
    def deleteEntireCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            currentNode = self.head
            self.tail.next = None
            while currentNode:
                currentNode.prev = None
                currentNode = currentNode.next
            self.head = None
            self.tail = None
            print("The entire CDLL has been deleted.")



#DRIVER CODE
cirularDoublyLinkedList = CircularDoublyLinkedList()
cirularDoublyLinkedList.createCDLL(5)
cirularDoublyLinkedList.insertNode(0,0)
cirularDoublyLinkedList.insertNode(1,1)
cirularDoublyLinkedList.insertNode(2,2)
cirularDoublyLinkedList.traverseCDLL()
cirularDoublyLinkedList.reverseTraversaCDLL()

print([node.value for node in cirularDoublyLinkedList])

#print(cirularDoublyLinkedList.searchCDLL(5))
cirularDoublyLinkedList.deleteNode(1)
cirularDoublyLinkedList.deleteEntireCDLL()
print([node.value for node in cirularDoublyLinkedList])

