import collections

from LinkedList import LinkedList

def partition(ll, x):
    currentNode = ll.head
    ll.tail = ll.head

    while currentNode:
        nextNode = currentNode.next #Reference to traverse linkedList
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode

        if ll.tail.next is not None:
            ll.tail.next = None

    return ll

#DRIVER CODE
customLL = LinkedList()
customLL.generate(5, 1, 23)
partition(customLL, 4)
print(customLL)
collections.Counter("Neoeoen")