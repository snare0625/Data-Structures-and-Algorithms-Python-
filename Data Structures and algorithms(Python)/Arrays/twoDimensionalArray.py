import numpy as np

#Day 1 - 11, 15, 10, 6
#Day 2 - 10, 14, 11, 5
#Day 3 - 12, 17, 12, 8
#Day 4 - 15, 18, 14, 9

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

#newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3,4]], axis=1)
#print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)

def accessElements(array, rowIndex, colIndex):
    if len(array)>=0 and len(array[0]) >= 0:
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)

def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse2DArray(newTwoDArray)

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f"The value is located at index {i}, {j}"
    return "The element is not found"

print(searchTDArray(newTwoDArray, 5))

newArray = np.delete(newTwoDArray, 1, axis=1)
print(newArray)