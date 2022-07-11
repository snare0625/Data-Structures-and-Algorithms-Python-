from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        tempSet = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in tempSet:
                currentNode.next = currentNode.next.next
            else:
                tempSet.add(currentNode.next.value)
            currentNode = currentNode.next

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups(customLL)
print(customLL)