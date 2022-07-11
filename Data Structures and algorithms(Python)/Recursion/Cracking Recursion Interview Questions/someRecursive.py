def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    if cb(arr[0]) == True:
        return True
    else:
        return someRecursive(arr[1:], cb)

arr = [4, 6, 8]
#print(someRecursive(arr, isOdd(arr[0])))
print([1,2] + [2, 3])