def Duplicate(array):
    new_list = []
    for element in array:
        if element not in array:
            new_list.append(element)

    if len(new_list) > 0:
        return False
    return True

from collections import Counter

def Duplicate1(array):
    return len(array) != len(Counter(array))