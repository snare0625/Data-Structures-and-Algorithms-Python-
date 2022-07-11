from array import *


def traverseArray(array):
    for i in array:
        print(i)

def accessElement(array, index):
    if index >= len(array):
        print("There is not any element in this index")
    else:
        print(array[index])

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not in the array"



arr1 = array('i', [1, 2, 3,4])
arr2 = array('d', [1.1, 1.2, 1.3, 1.4])

arr1.remove(1)
print(arr1)


#print(arr2)

arr1.insert(4, 6)
#print(arr1)


#accessElement(arr1, 2)
#traverseArray(arr1)
print(arr1)
print(searchInArray(arr1, 6))