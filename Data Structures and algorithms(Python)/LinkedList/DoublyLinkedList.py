class Node:
    def __init__(self, value):
       self.value = value
       self.next = None
       self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #Creation of DoublyLinkedList
    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created"

    #insertion in DDLL
    def insert(self, value, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                newNode.next = currentNode.next
                newNode.prev = currentNode
                newNode.next.prev = newNode
                currentNode.next = newNode

    #Traversal method in DLL
    def traversalDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.next

    #Reverse traversal
    def reverseTraversal(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.prev

    #search
    def searchDLL(self, targetValue):
        if self.head is None:
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == targetValue:
                    return tempNode.value
                tempNode = tempNode.next

            return "The node does not exist in this list."

    #delete a node from DLL
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                nextNode.prev = currentNode

    #delete entire DLL
    def deleteDLL(self):
        if self.head is None:
            print("There is not any node in DLL")
        else:
            currentNode = self.head
            while currentNode:
                currentNode.prev = None
                currentNode = currentNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")






#DRIVER CODE
doublyLinkedList = DoublyLinkedList()
doublyLinkedList.createDLL(5)
doublyLinkedList.insert(0, 0)
doublyLinkedList.insert(2, 1)
doublyLinkedList.insert(6, 2)
#doublyLinkedList.traversalDLL()
#doublyLinkedList.reverseTraversal()
print([node.value for node in doublyLinkedList])
doublyLinkedList.deleteNode(0)
print(doublyLinkedList.searchDLL(5))
doublyLinkedList.deleteDLL()
print([node.value for node in doublyLinkedList])


