def findNumber(array, number):
   for i in range(len(array)):
       if array[i] == number:
           return i


myArray = [1, 2, 3, 4, 5 ]
print(findNumber(myArray, 2))
