from LinkedList import LinkedList

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenA else llA

    longerNode = longer.head
    shorterNode = shorter.head

    diff = len(longer) - len(shorter)

    for i in range(diff):
        longerNode = longerNode.head

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode
