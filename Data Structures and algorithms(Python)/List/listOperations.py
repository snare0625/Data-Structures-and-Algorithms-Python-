myList = [10, 20, 30, 40, 50, 60, 70, 80]


#Searching for an element in a list

#IN Operator
if 20 in myList:
    print(myList.index(20))
else:
    print("The value does not exist in the list")

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 50))

a = 'spam - spam1 - spam2'
delimiter = '-'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))


import numpy as np

myArray = np.array([1,2,3,4,5])
myList = [1,2,3,4,5]
print(myArray/2)
print(myList)




a=[1,2,3,4,5]
print(a[3:0:-1])