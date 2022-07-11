from LinkedList import LinkedList

def kthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    if ll.head is None:
        return None

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

custom = LinkedList()
custom.generate(5, 1, 6)
print(custom)
print(kthToLast(custom, 2))